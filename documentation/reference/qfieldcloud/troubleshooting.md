---
title: Troubleshooting
---

Sometimes users can experience difficulties using QFieldCloud due to job failures. While QFieldCloud tries it's best to inform you what went wrong, there is a list of common errors and solutions to them.


## Jobs

When running a job, usually you can find a step called "Check project layers" that prints a table with all the project layers and status next to them.


The possible statuses are:

- **ok** - The layer loads correctly on QFieldCloud.
- **invalid_dataprovider** - the layer's data provider is invalid. Usually additional information is shown in the "Provider Summary".
- **invalid_layer** - This errors should happen very rarely if ever. The data is loaded correctly, but for some reason QGIS reports the layer as invalid.


### Unable to connect to service "`{SERVICE}`".

QFieldCloud tries to connect to a PostgreSQL service that is not available.

!!! warning
    QFieldCloud does not support `.pgservice` files yet. You need to store your PostGIS credentials within the QGIS project file.


### Unable to connect to host "`{HOST}`".

QFieldCloud cannot establish a connection to the given `{HOST}`. Your service is not accessible from the QFieldCloud server. You might been to ask your IT department to whitelist the QFieldCloud IP.

### Unable to connect to host "localhost".

You have uploaded a layer that connects to a database/service on your local machine. Either remove that layer or replace it with a layer source accessible by QFieldCloud.

### File "`{FILENAME}`" missing.

The file `{FILENAME}` (e.g. `/tmp/rndstr/files/data.gpkg`) is not found on the QFieldCloud server and cannot be opened. There are two things that should be checked:

- Whether the file has been uploaded to the cloud. You can check this in **Project Settings -> Files** page on QFieldCloud or QFieldSync.
- Making sure the file is uploaded with the same relative path as on your PC. Please note that **all** project files should be within the same project directory or subdirectory as the `.qgs`/`.qgz` QGIS project file. Please also note the directory names should be preserved too, for example if a file is stored in `data/data.gpkg`, make sure the `data` directory exists on QFieldCloud too.
