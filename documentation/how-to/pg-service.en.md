---
title: PostgreSQL service
tx_slug: documentation_how-to_pg-service
---

# PostgreSQL service

A `pg_service.conf` file allows to use an named alias for a PostgreSQL server connection. Instead of storing hostname, port, database name and more into the QGIS Project file, these can be stored separately. It is even possible to store username and password in a `pg_service.conf` file, to avoid having this stored in clear text in the QGIS Project.

Read more about PostgreSQL services in the [QGIS documentation](https://docs.qgis.org/3.22/en/docs/user_manual/managing_data_source/opening_data.html#postgresql-service-connection-file).

# QField - Direct Connection

If you directly connect from QGIS to your database you can make use of a `pg_service.conf` file by placing it in the QField data folder. You can place your file either on the Internal Device Storage or on the SD Card Storage. You can check the path for the QField data folder in the bottom of the `About QField` screen in the app.

Usually the path on Android devices looks something like this: `/Android/data/ch.opengis.qfield/files/QField`.

!!! note
    Unlike on *NIX systems where the file is named `.pg_service.conf`, the file on Android is named `pg_service.conf` without a leading dot sign (`.`).

# QFieldCloud

QFieldCloud support `pg_service.conf` configurations too. You need to configure your PostgreSQL layers with "Offline editing" cloud action and store your service settings on QFieldCloud Project's Secrets page.

Read more [how to configure PostgreSQL service](../reference/qfieldcloud/secrets.md) in the QFieldCloud documentation.

## Creating a `pg_service.conf` File for PostgreSQL Connection in QGIS and Secrets

Before beginning, ensure that you have allowed connections to QFieldCloud. Refer to [Technical specs](../reference/qfieldcloud/specs.md) for instructions.

1. **Create a Text File**: Open your preferred text editor and create a new text file to define PostgreSQL service connection parameters. Save this file in your user's home directory, typically `~/.pg_service.conf`.

   ```
   ~/.pg_service.conf
   ```

2. **Add Connection Parameters**: Define the connection parameters for your PostgreSQL database within this file. Use the following structure:

   ```
   [MY_SERVICE_NAME]
   host=your_host_or_ip
   port=your_port
   dbname=your_database_name
   user=your_username
   password=your_password
   ```

   Replace placeholders (`your_host_or_ip`, `your_port`, `your_database_name`, `your_username`, `your_password`) with actual PostgreSQL connection details. For example:

   ```
   [NINJA_DB]
   host=my_db_for_ninja.ch
   port=5432
   dbname=my_database
   user=my_username
   password=my_password
   ```

!![Parameters](../assets/images/service_config_file_001.png)

3. **Save the File**: Save the file after adding connection parameters.

4. **Environment Variable**: To ensure QGIS recognizes `pg_service.conf`, set the `PGSERVICEFILE` environment variable to point to its location. Add the following line to your shell's startup file (e.g., `~/.bashrc`, `~/.bash_profile`, `~/.zshrc`, etc.):

   ```
   export PGSERVICEFILE="~/.pg_service.conf"
   ```

   Save the file and either source it or restart your shell for changes to take effect.

For Windows:

- Set the `PGSERVICEFILE` environment variable under "Environment Variables."
- Navigate to "This PC" or "My Computer" > Properties > Advanced system settings > Environment Variables.
- Add a new variable:
  - Variable name: `PGSERVICEFILE`
  - Variable value: `C:\Users\<YourUsername>\AppData\Roaming\postgresql\pg_service.conf` (or your `pg_service.conf` file path).

Alternatively, set environment variables directly in QGIS via Settings > Options > System > Environment. Refer to [QGIS System Settings](https://docs.qgis.org/3.28/en/docs/user_manual/introduction/qgis_configuration.html#system-settings) for details.

!![QGIS System Environment Variables](../assets/images/service_config_file_002.png)

1. **Test the Connection in QGIS**: Open QGIS and set up a new PostgreSQL connection using the service name defined in `pg_service.conf` (e.g., `[MY_QGIS_DB]`) in the connection details. QGIS will read configuration from `pg_service.conf` automatically.

   - Open QGIS.
   - Go to "Layer" > "Add Layer" > "Add PostGIS Layers..."
   - In "Create a New PostGIS Connection," select "Service" from the drop-down menu.
   - Enter the service name from `pg_service.conf` (e.g., `[NINJA_DB]`) in the "Service" field.
   - Click "OK" to connect to your PostgreSQL database using configurations from `pg_service.conf`.

!![Test your connections](../assets/images/service_config_file_003.png,350px)

1. **Add Parameter to QFieldCloud Secrets**: Navigate to the project's secrets page and copy the service directly from `.pg_service.conf` to the secret. Follow [Secrets](../reference/qfieldcloud/secrets.md) for guidance.

!![Add the secret](../assets/images/service_config_file_004.png,350px)
