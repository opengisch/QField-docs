---
title: Storage
tx_slug: documentation_get-started_storage_qfield
---

# QField Storage Management

On the QField homescreen, users are presented with two options to open a project.

- **QFieldCloud projects**: The first option is to [access a project stored on QFieldCloud](../../get-started/tutorials/get-started-qfc.md)
How to set up and work with QFieldCloud is explained in the next chapter.
- **Open local file**: The second option involves copying a working copy of the QGIS project file from a laptop or PC (the source device) to the phone or tablet (the target device).
On the target device, users can access and edit this local copy using QField and eventually copy the edited version back to the desktop or to an alternative cloud storage service.

There are various possibilities to export copies of project files and datasets from the source device running QGIS and importing them on to a target device for field-data collection.

## 1. Exporting QGIS project files for use in QField

QField supports a [wide range of data formats](../../reference/data-format.md).
There are two ways of preparing and copying a project in QGIS for use in QField.

* [Storing files in a designated folder](#storing-files-in-a-designated-folder)

### Storing files in a designated folder

One way of compiling all necessary parts of a QGIS project is to store them in a folder.
This folder can contain individual files such as a

* QGIS project file (.qgs or .qgz)
* Vector data (Shapefiles, GeoJSON or GeoPackage)
* Raster data (GeoTIFFs, JPEGs and others)
* Auxiliary files, which includes additional files used for styling (.qml or .sld) and any other files referenced by the project

### Saving the project within a GeoPackage

The simplest and most efficient way to save a QGIS project and its corresponding geospatial data in one file is to use a [GeoPackage](https://www.geopackage.org/).
We recommend using the GeoPackage file format for projects in QField.
