---
title: Advanced Setup
tx_slug: documentation_get-started_tutorials_advanced-setup-qfc
---

# Advanced setup guide

!!! help
    We have a [community discussion platform](https://github.com/opengisch/qfield/discussions) to discuss your questions, doubts and ideas. Do not hesitate to check it out.


## Supported vector providers

Currently, QFieldCloud supports GeoPackage and PostGIS layers for collaborative editing. Other formats supported by QGIS should also work but are not officially supported.

## Working with GeoPackages

Using GeoPackages is usually the best choice for a simple setup to centralize data collected by your QField users to one single file.

If you would like to set up relations, it is recommended to add a UUID field on your tables, and to use that as a foreign key instead of geoPackage's `fid`, as they are subject to change to avoid conflicts if two users create new records at the same time.

### Example workflow (GeoPackage)

1. Setup on QGIS desktop:
    1. Create a new project.
    2. Create a GeoPackage layers, save it in the same folder than the QGIS project.
    3. Set the GeoPackage to "Offline editing" in the QFieldSync plugin.
    4. Upload the project to QField cloud.
2. Collect data on the device with QField:
    1. Open QFieldCloud and import the project.
    2. Collect some data and upload the changes.
3. Download results on QGIS desktop:
    1. In QFieldSync, download the updated files (the GeoPackage file should have changed).

!!! attention
    This workflow does not support changing the GeoPackage on the desktop, as being file base, the whole GeoPackage will be replaced. This means that data can only be digitized using QFieldCloud.


## PostGIS

Using PostGIS layers is a good choice if you want data from your QField users to be updated directly in your database by QFieldCloud when they sync their work without further step.

It requires your database to be publicly accessible and credentials must be saved unencrypted in the QGIS project. Please be aware of the security implications of such requirements, and remember to have backups.

### Example workflow (PostGIS)

1. Setup on QGIS desktop:
    1. Create a new project.
    2. Create add a PostGIS layer, making sure to store the credentials in the project.
    3. Make sure the PostGIS database connection is publicly accessible (public IP or domain name, it will not work with 127.0.0.1 or localhost).
    4. In the QFieldSync project settings, set the GeoPackage to `Offline editing` if your QField users will not have a reliable internet connection in the field or `Direct database access`.
    5. Upload the project to QField cloud.
2. Collect data on the device with QField:
    1. Open QFieldCloud and import the project.
    2. Collect some data (and upload the changes once back at the office if you were using `Offline editing`).
3. See results on QGIS desktop:
    1. All changes should be directly visible on the PostGIS database.

!!! note
    When using `direct database access`, QFieldCloud will directly edit data on the PostGIS database. This will only work with a reliable internet connection in the field, but has the advantage that all data is directly visible to all users and allows to use any PostGIS specific setup (triggers, generated fields, etc).

!!! note
    When using `offline editing`, QField will work on a local copy of the database in a GeoPackage, which will be synced by QFieldCloud to the original database. This is the best choice if the connection in the field is not reliable. Changes will only be visible to users once they sync to QFieldCloud. As a local copy is created, advanced PostGIS features will not be available on QField. Just like for regular GeoPackages, if you define relationships, it is recommended to use UUIDs instead of integer primary keys to avoid conflicts if multiple users create data at the same time.

You can find more information on [QFieldCloud technical reference](../../reference/qfieldcloud/concepts.md).
