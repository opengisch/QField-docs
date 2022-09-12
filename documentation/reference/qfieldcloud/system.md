---
title: System Documentation
---

# QFieldCloud System Documentation
  The aim of this document is to provide an overview of the QFieldCloud system to
  understand the underlaying logic and technology.

## Entities and Concepts

### QGIS Project
A QGIS project is a *.qgs* or *.qgz* file. A Project is created on
QGIS Desktop and uploaded to QFieldCloud using the QGIS's plugin
QFieldSync. Before the uploading of the QGIS project, it is necessary
for each layer of the QGIS project an "action" that determines how
QFieldSync and QField should treat the layer. There are the two types
of actions that can be setup - one for QFieldCloud and one for the
traditional cable export.

This information is saved within the QGS project as layer's
*customProperty*, with the *QFieldSync/action* key.

The available actions are:

| Action internal name | Name showed in the UI |
|----------------------|-----------------------|
| OFFLINE              | Consolidate           |
| NO_ACTION            | Live layer            |
| REMOVE               | Ignore layer          |
| COPY                 | Copy                  |
| KEEP_EXISTING        | Keep Existing         |

This would be the behavior of QFieldSync with the different
layer actions:

| Action        | File based layer                                                 | Not file based layer                   |
|---------------|------------------------------------------------------------------|----------------------------------------|
| OFFLINE       | Create a consolidated copy of the data                           | Create a consolidated copy of the data |
| NO_ACTION     | N/A                                                              | No action on the layer                 |
| REMOVE        | Remove the layer from the project                                | Remove the layer from the project      |
| COPY          | Make source path relative and copy the file                      | N/A                                    |
| KEEP_EXISTING | Make source path relative and copy the file if it does not exist | N/A                                    |

 This is the behavior of QFieldCloud (`libqfieldsync`) with the
 layers:

| Action        | File based layer                                                                                                | Not file based                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| OFFLINE       | Create consolidated copy of the data on pull, apply delta file on push to original data source                  | Create consolidated copy of the data on pull, apply delta file on push to original data source |
| NO_ACTION     | N/A                                                                                                             | No action on the layer                                                                         |
| REMOVE        | Remove the layer from the project                                                                               | Remove the layer from the project                                                              |
| COPY          | Make source path relative and create copy of the data on pull, apply delta file on push to original data source | N/A                                                                                            |
| KEEP_EXISTING | Make source path relative and create copy of the data on pull, apply delta file on push to original data source | N/A                                                                                            |

This is the behavior of QField with the layers:

| Action        | File based layer                   | Not file based layer                       |
|---------------|------------------------------------|--------------------------------------------|
| OFFLINE       | Create and push deltafile          | N/A (it's always file based at this point) |
| NO_ACTION     | N/A                                | Edit the online (live) database            |
| REMOVE        | N/A (the layer is no longer there) | N/A (the layer is no longer there)         |
| COPY          | Create and push deltafile          | N/A                                        |
| KEEP_EXISTING | Create and push deltafile          | N/A                                        |

In summary, for with QFieldCloud:

- *NO_ACTION* is used for online layers that are located on a server
  accessible via the Internet and that are modified directly by
  QField.
- *HYBRID* means that a geopackage will be generated on the
  server (or directly on the desktop for file-based layers) and
  downloaded by clients. The client will generate deltafiles of the changes.
- *OFFLINE* is used for example to work with local databases not
  visible by QFieldCloud which are consolidated before being
  loaded from the desktop to the server and are not synchronized
  with the original data by QFieldCloud.
- *REMOVE* will simply remove the layer from the project.
- *KEEP_EXISTENT* will not be used for QFieldCloud syncronizations.

From QFieldSync it will be possible to update a project already
loaded on QFieldCloud. In the event that the changes concern only
styles, forms etc. but not the structure of the layers, the
project on the server will simply be updated.
If there are changes in the layers structure, the project will be
reset on the server (delta files will be deleted) and for each
client it will be necessary to download the updated version of the
project before being able to push new changes.

### QFieldCloud Project
    Is composed of one and only one QGIS project and the possible
    related files (e.g. geopackages, images, ...) included the offline
    or hybrid data package.

## Use Cases

### Hybrid
Hybrid editing mode with synchronization on the server

!![Hybrid editing mode](../../assets/images/hybrid-schema.png)

### Offline database
Offline editing mode with desktop synchronization

!![Offline editing mode](../../assets/images/offline-schema.png)
