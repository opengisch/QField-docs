---
title: Projects
---

Projects are the main data container within QFieldCloud. Each user can create one or more QFieldCloud projects. Each project contains a single `.qgs`/`.qgz` QGIS project file, the geospatial files - GeoPackages, Shapefiles, TIFs, and additional data such as photos, PDFs etc. All project data files must be within a single QFieldCloud project.

Each QFieldCloud project has a name and an owner. The owner of a project is a QFieldCloud user or an organization. The owner name and project name must be a unique combination within QFieldCloud, which means a user cannot have two projects with the same name.

Projects can be marked as public or private. Private projects are accessible only by users that are added as project collaborators. The public projects are visible to anyone on QFieldCloud and they can download the project on their QField device.

## Creating a project

A project can be created in two different ways: either using the QFieldCloud web interface or using QFieldSync in QGIS.

## Files

Files are the skeleton on which QFieldCloud project works. To make a QFieldCloud project alive you need to upload at least a single QGIS project file in the `.qgs` or `.qgz` file format. All geospatial files need to be uploaded with the same relative paths as on your computer. If external SVG or raster symbology is used, you need to upload these files too.

!!! note
    QFieldCloud does not support projects stored in a GeoPackage (`.gpkg`) files.

A typical file structure of a QGIS file might look something like this:
```
project
├── data
│   ├── basemap.tif
│   ├── bees.gpkg
│   └── fields.gpkg
├── symbology
│   ├── icon.svg
│   └── line-pattern.png
├── DCIM
│   ├── bees-20220404121212.jpg
│   ├── bees-20220405040506.jpg
│   └── fields-20220405040607.jpg
└── project.qgs
```

## Collaborators

A project collaborator is another QFieldCloud user invited to contribute to a project. One project may have multiple collaborators. Collaborators with role **owner** or **admin** can add more users as collaborators. If the project is owned by an organization, you can also add **teams** as collaborators. Read more about [collaborator roles](permissions.md).

## Changes

Changes made on vector layers and pushed to QFieldCloud from a QField device will appear here. Each change stores the changed attributes and geometries.

Changes have one of the three methods:

- `create` - a new feature has been created.
- `delete` - an existing feature has been deleted.
- `patch` - an existing feature has been modified.

Features that have been created and later deleted without being pushed to QFieldCloud will never appear in project changes.

!!! note
    Changes on online vector layers (PostGIS, WFS) that does not have "Offline editing" cloud layer action will not generate a change, but will directly modify the original data source.

!!! note
    Changes to vector layers done in QGIS will not appear here.

## Jobs

Read more about [project jobs](jobs.md).

## Secrets

Secrets are settings that are securely stored in encrypted way. Project jobs will automatically have access to their secrets. Once added, a secret can only be removed, but cannot be edited.

There are two types of secrets:

- **Environment variables** - Environment variables will be available to QGIS while your project jobs are running.
- **pgservice connection** - A PostgreSQL/PostGIS connection as defined in the <code>.pg_service.conf</code> configuration file. If you use multiple service definitions, you should add multiple secrets for each of them.

## Settings

Project settings are available only for project owners and collaborators with elevated permissions. From here a user can access some sensitive project settings or unrecoverable actions.

- Change the project visibility to public.
- Change the project owner.
- Permanently delete a project.
- etc

!!! warning
    The actions taken on the project settings page might lead to data loss!