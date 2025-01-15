# Architecture overview

QFieldCloud has a containerized architecture with multiple containers and volumes.


!![QFieldCloud architecture: Rounded rectangles represent containers, ellipses represent volumes. The text in the square brackets is the service name found in the `docker-compose.yml` file, the rest of the text is the function of the container. Arrows between containers shows who initiates the communication. Arrows between a container and a volume represents whether the container reads (arrow pointing to container) or writes (arrow pointing to volume) data. Arrows and containers in gray represent deprecated services.](../../assets/images/qfc_server_architecture_light.svg)

See an interactive version of [the drawing above](https://excalidraw.com/#json=Mb0cenWqFcnixbKRLv4Ft,7g6FloTTCCmGQAOeQYajjw).

!!! NOTE
  For simplicity and clarity all graphs show the so called "happy path" without detailing the error handling through the process.


## Docker containers

### Containers

#### `[nginx]` Reverse proxy

The reverse proxy that sits in front of QFieldCloud.
Hard requirement on [`nginx`](https://nginx.org/en/) for this purpose as the [`X-Accel-Redirect` HTTP header](https://nginx.org/en/docs/http/ngx_http_core_module.html#internal) is heavily used in production to serve files directly from the **[minio] File Storage**.

Requires a SSL certificate to be present - self-signed, Let's Encrypt or other.


#### `[app]` QFieldCloud App

The main software that runs QFieldCloud, including authentication, permissions management, data models, static files, administrative interface and more.

It consists of multiple Django apps, namely:

- `authentication` - responsible for API authentication.
- `core` - data models, permissions, job queue management, REST API, administrative interface, and everything else in QFieldCloud that is not managed by the other Django Apps.
- `filestorage` - responsible for project file management and respective REST API.
- `notifs` - notifications module.
- `subscription` - management of user's plans, subscription and storage quota.


#### `[memcached]` In-memory cache

Uses [`memcached`](https://memcached.org/) for in-memory cache of Django settings and other computed values.


#### `[ofelia]` CRON runner

Uses [`ofelia`](https://github.com/mcuadros/ofelia) for CRON runner.


#### `[mkcert]` Self-signed certificate creator

Automatically create self-signed SSL certificate for local development and test deployments.


#### `[certbot]` Letsencrypt manager

Uses [`certbot`](https://certbot.eff.org/) for managing Let’s Encrypt certificates.
It automatically recreate expiring SSL certificate and they are automatically reloaded by **[`nginx`] Reverse Proxy**.


#### `[worker_wrapper]` Queue Consumer

One or more containers to consume and manage Jobs from the queue.
The **[worker_wrapper] Queue Consumer** regularly polls the **[db] App Database** for new pending Jobs.
Once a Job in `PENDING` status is encountered, the **[worker_wrapper] Queue Consumer** sets it to `QUEUED` status and starts processing it.
Then the container will set a bunch of metadata on the Job object in the **[db] App Database** and start a completely new temporary **[qgis] Worker** container.
It waits the **[qgis] Worker** container to finish, gets the logs and stores them in the **[db] App Database**.

Finally, it updates a bunch of other Job's metadata in the **[db] App Database** based on the exit code and the logs from the **[qgis] Worker**, and sets the Job's status to `FINISHED` or `FAILED`.

The container runs the very same Django code used in **[`app`] QFieldCloud App**.

Read how the **`[worker_wrapper]` Queue Consumer** works in the [Job Queue section](#job-queue).


#### `[qgis]` Worker

The Worker container is the actual place where the Jobs created by the **[`app`] QFieldCloud App** are executed.
Each Worker container is created dynamically by the **[`worker_wrapper`] Queue Consumer** to execute a single job for a single project and deleted right after.
The typical execution of a Worker consists of starting a headless QGIS application, downloading project files, process the project files and reuploading the resulting processed files.

The **`[qgis]` Worker** container gets environment variables, including a temporary QFieldCloud authentication token, from the **`[worker_wrapper]` Queue Consumer**, and send back data to the it by writing logs to the `STDERR` and writing files in the temporary shared volume, primarily `feedback.json`.


### Volumes

#### `[cerbot_www]`

Stores the SSL certificates created by **`[mkcert]` Self-signed certificate creator** or **`[certbot]` Letsencrypt manager**.


#### `[transformation_grids]`

Contains all transformation grids available, downloaded from https://cdn.proj.org/ and made available for all Jobs.


#### `[static_volume]`

Contains all static assets such as fonts, CSS, JS or image files.


#### `[media_volume]`

Warning! Deprecated, might be removed at any time.

The default location for User uploaded files. It should be never used.


## Job Queue

QFieldCloud runs very heavy operations to make Project synchronization work smoothly for users.
Therefore such operations are executed using the [Jobs](jobs.md) that run in the background.

Here we have a sequence diagram of the stages each Job run follows.

=== "Simplified"

    Some of the steps are intentionally shortened for clarity.

    ``` mermaid
    sequenceDiagram
        autonumber
        participant DB as QFieldCloud DB
        participant Queue as QFieldCloud Queue

        loop poll database
          Queue->>DB: select the oldest Job with `PENDING` status
          Queue->>DB: set the status of Job to `STARTED` status

          Queue->>DB: create a new temporary authentication token

          create participant Worker
          Queue->>Worker: create the worker and pass the authentication token

          note over Worker: job specific processing...

          destroy Worker
          Queue-xWorker: get worker's structured and free text logs and exit code

          Queue->>DB: set job's structured logs, free text logs and exit code

          alt Worker has zero exit status
            Queue->>DB: set the Job  status to `FINISHED`
          else Worker has non-zero exit status
            Queue->>DB: set the Job  status to `FAILED`
          end

          break when any of the steps above fails
              Queue-->DB: set the status Job to `FAILED`
          end
        end
    ```

=== "Detailed"

    While some of the steps are still simplified, this diagram contains much more information about the Job's attribute lifecycle.

    ```mermaid
    sequenceDiagram
        autonumber

        participant DB as QFieldCloud DB
        participant Queue as QFieldCloud Queue

        loop [every few seconds]
          Queue->>DB: select the oldest job with `PENDING` status

          Queue->>DB: set the status of current job to `QUEUED`
          Queue->>DB: set the status of current job to `STARTED` and `started_at` to `now()`

          Queue->>DB: create a new temporary authentication token
          Queue->>DB: set `docker_started_at` to `now()`


          create participant Worker
          Queue->>Worker: - mount `transformation_grids` volume <br> - set shared data volume <br> - set the environment variable with the authentication token <br> - set the environment variables from secrets <br> - set the `pgservice` file from secrets <br><br> Create the worker
          activate Worker

          par run worker
            Worker->>API: Download files
            API->>Worker: Files downloaded

            note over Worker: job specific processing...

            Worker->>API: Upload files
            API->>Worker: Files uploaded

            deactivate Worker

          and wait for Worker to finish on Queue
            Queue->>DB: set `container_id` to the newly created Docker container id
            Queue->>Queue: wait until the Worker is finished or timeout reached
          end

          Queue->>DB: set `docker_finished_at` to `now()`


          destroy Worker
          Queue-xWorker: - get Worker's `stdout` logs <br> - get Worker's structured logs from the `feedback.json` in the shared volume <br> - get Worker's exit status code <br><br> Remove the container and cleanup all Job data

          Queue->>DB: set job's `output` and `feedback`

          alt [Worker has zero exit status]
            Queue->>DB: set the status of current job to `FINISHED` and `finished_at` to `now()`
          else [Worker has non-zero exit status]
            Queue->>DB: set the status of current job to `FAILED`
          end

          break when any of the steps above fails
              Queue-->DB: set the status of the current job to `FAILED`
          end

        end

        participant API as QFieldCloud App
    ```
