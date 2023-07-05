---
title: Projects
tx_slug: documentation_reference_qfieldcloud_projects
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

## File versions

QFieldCloud uses file versioning that allows you to restore to a previous version of the modified files. The files and file versions can be found in in **Files** section of your project. Each subscription plan has different default number of versions stored for each file. Check the qfield.cloud [https://qfield.cloud/pricing.html](pricing page for further details).

### How to remove old versions of the files

The saved versions, can be deleted. If there is a specific file or versions that like to remove, this can manually be delete from the project's **File** section. This can help free up space and ensure that only relevant versions files are retained.

To delete versions of files in QFieldCloud, follow these steps:

1. Go to the "Files" section of your project.![Project files](../../assets/images/files_versions_for_deleting.png)
2. Locate the layer for which you want to delete versions.![Layer selected](../../assets/images/files_versions_for_deleting_2.png)
3. Click on the three dots next to the layer name.![Clickable option](../../assets/images/files_versions_for_deleting_three_dots.png)
4. You will see a list of versions for that specific layer.![List of files versions](../../assets/images/files_versions_for_deleting_files_versions.png)
5. Identify the version you want to delete and click on the red trash bin icon next to it.![Thrash icon](../../assets/images/files_versions_for_deleting_deleting_a_version.png)
6. Confirm the deletion when prompted, if you want to delete all versions before a specific version, you can do it activating the option "Also delete `n` version(s) older than the selected version.".![Deleting files versions](../../assets/images/files_versions_for_deleting_also_delete.png)
7. After deleting a pop up message will appear with the success and the list of versions will show just the versions that was not selected for deletion.![List of versions after deleting 2 versions before](../../assets/images/files_versions_for_deleting_version_remain.png)

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
