---
title: Jobs
tx_slug: documentation_reference_qfieldcloud_jobs
---

Jobs on QFieldCloud perform heavy operation with project files and layers within QGIS. Jobs are created in response to certain user actions.

Once a job is created, it is added to the project's job queue and waits for available QFieldCloud resources to run. At any given moment only one job can run per project. The rest of the queued jobs will perform in the same order as in they entered the queue.

Each job consists of one or more steps and each step is responsible for one self contained task on the project. QFieldCloud supports three predefined job workflows: `process_projectfile`, `package` and `delta_apply`.

While running, jobs are writing log messages which are available on project's jobs page for jobs that have reached a final status `FINISHED` or `FAILED`.

Jobs have access to [project secrets](projects.md#secrets).

!!! note
    All jobs can be triggered using the QFieldCloud API.

!!! warning
    - Any of the triggering conditions described on this page might change without notice.
    - All jobs must finish within 10 minutes or they will result in a timeout error and will be terminated.

## Job types

### Process project file (`process_projectfile`) job

The process project file job is used to extract details about the project configuration and project layers, such as project CRS, layer CRS, layer name, layer validity etc. QFieldCloud validates the uploaded QGIS project file (`.qgs`/`.qgz`), as well as the supporting GeoPackages, TIFFs and other data source files. It also validates remote connection to PostGIS, WFS, WMS and other online data sources. QFieldCloud will open the project file in a QGIS instance on the server to extract all the necessary information.

#### Triggers

This job is triggered every time a file is uploaded to QFieldCloud, unless at least one of the following condition are valid:

- No QGIS project file (`.qgs`/`.qgz`) has been uploaded yet.
- The uploaded file is within the `DCIM` directory. Those files are assumed to be irrelevant to project validity.
- There is already a `process_projectfile` job in `PENDING` status.

#### Troubleshoot

A `process_projectfile` job might result in `FAILED` status. Check the non-exhaustive list of causes below:

- The uploaded QGIS project file (`.qgs`/`.qgz`) is unreadable, incomplete, broken or wrong. Try to reupload the QGIS project file.
- QGIS is crashing after opening the project file. Try to identify the layer that is causing the crash by removing one layer at time from the project and reuploading the QGIS project file.

!!! NOTE
    Even if a `process_projectfile` job results in a `SUCCESS` status, it does not mean the project is properly configured. The `SUCCESS` status just states the project has been successfully opened and all the needed information has been extracted.

### Package (`package`) job

The `package` job convert a QGIS project to a QField project, the same way it is done on QGIS via QFieldSync. The `package` job will prepare all layers marked as "Offline editing" to a single GeoPackage.

#### Triggers

This job is triggered every time the **Download** or **Synchronize** buttons are pressed on QField. Unless at least one of the following condition are valid:

- The project has never run a `process_projectfile` job that resulted in `SUCCESS` status.
- There is already a `package` job in `PENDING` status.
- The project does not contain online vector layers (PostGIS, WFS etc), the latest `package` job result was `SUCCESS` and there were no file uploads, nor change uploads.
#### Troubleshoot

A `package` job might result in `FAILED` status. Check the non-exhaustive list of causes below:

- The project has never run a `process_projectfile` job that resulted in `SUCCESS` status.
- Some of the project layers are inaccessible from QFieldCloud. Make sure all files are uploaded and all credentials to online layers (PostGIS, WFS etc) are stored within the QGIS project file.

### Delta apply (`delta_apply`) job

Delta apply jobs is responsible to make all pushed QField changes permanent.

#### Triggers

This job is triggered every time a **Synchronize** or **Push changes** button is pressed on QField, or **Apply pending changes** button is pressed on the **Changes** project page. If any of the following condition are valid:

- The project never run a `process_projectfile` job that resulted in `SUCCESS` status.
- There is already a `delta_apply` job in `PENDING` status.

#### Troubleshoot

A `delta_apply` job might result in `FAILED` status. Check the non-exhaustive list of causes below:

- At least one of the online databases (PostGIS/WFS) used in the QGIS project reset the connection.
- The project is too big and the job has failed to run.
- There are hidden files and directories within the project that are preventing the normal work of QFieldCloud. Hidden files and directories are those starting with a leading dot (`.`).


## Troubleshoot job logs

When running a job, usually you can find a step in the logs called "Check project layers" that prints a table with all the project layers and status next to them.

The possible statuses are:

- **ok** - The layer loads correctly on QFieldCloud.
- **invalid_dataprovider** - the layer's data provider is invalid. Usually additional information is shown in the "Provider Summary".
- **invalid_layer** - This errors should happen very rarely if ever. The data is loaded correctly, but for some reason QGIS reports the layer as invalid.


### Unable to connect to service "`{SERVICE}`".

QFieldCloud tries to connect to a PostgreSQL service that is not available. You should need to create a new pgservice [secret](projects.md#secrets) so QFieldCloud can connect to the PostGIS service.

### Unable to connect to host "`{HOST}`".

QFieldCloud cannot establish a connection to the given `{HOST}`. Your service is not accessible from the QFieldCloud server. You might been to ask your IT department [to whitelist the QFieldCloud IP](specs.md#firewall-configuration).

### Unable to connect to host "localhost".

You have uploaded a layer that connects to a database/service on your local machine. Either remove that layer or replace it with a layer source accessible by QFieldCloud.

### File "`{FILENAME}`" missing.

The file `{FILENAME}` (e.g. `/tmp/rndstr/files/data.gpkg`) is not found on the QFieldCloud server and cannot be opened. There are two things that should be checked:

- Whether the file has been uploaded to the cloud. You can check this in **Project Settings -> Files** page on QFieldCloud or QFieldSync.
- Making sure the file is uploaded with the same relative path as on your PC. Please note that **all** project files should be within the same project directory or subdirectory as the `.qgs`/`.qgz` QGIS project file. Please also note the directory names should be preserved too, for example if a file is stored in `data/data.gpkg`, make sure the `data` directory exists on QFieldCloud too.
