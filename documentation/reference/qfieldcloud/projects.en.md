---
title: Projects
tx_slug: documentation_reference_qfieldcloud_projects
---

# Projects

Projects are the main data containers on QField and QFieldCloud.
Users can create any number of projects.
Projects must contain a single `.qgs`/`.qgz` QGIS file, and may in addition contain any combination of geospatial files -- GeoPackages, Shapefiles, TIFs -- or data files such as photos, PDFs etc.
To ensure optimal performance, is recommend keeping file sizes under 2GB.
Larger files than this may take significantly longer to process.
Files cannot be shared between projects, unless [localized layers](../../how-to/outside-layers.md) are used.

QFieldCloud projects have a name and an owner.
The owner of a project is a QFieldCloud user or an organization.
No two projects can use the same pair `owner_name` and `project_name`.

Projects can be marked as either public or private.
Private projects are accessible only to users added to a project as project collaborators.
Public projects are visible to, and can be downloaded by, any QFieldCloud user.


## Creating a project

A project can be created in multiple ways:

- via QFieldCloud web interface;
- via QFieldSync in QGIS;
- via QFieldCloud-SDK;


## Files

Files are the skeleton on which QFieldCloud projects work.
To make a QFieldCloud project alive users need to upload at least a single QGIS project file in the `.qgs` or `.qgz` file formats.
All geospatial files must be uploaded using the same relative paths as on one's computer.
If external SVG or raster symbology is used, users must upload the corresponding files too.

!!! note
    QFieldCloud does not support projects stored in a GeoPackage (`.gpkg`) files (but users can still use GeoPackage files to store datasets for their projects).

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
├── project.qgs
├── project_attachments.zip
└── project.qml
```


The files in a QGIS project can be in one of the following groups by their purpose:

- **QGIS project file** - a `.qgs` or `.qgz` project file.
- **QGIS sidecar files** - the utility files to the QGIS project file, such as `*_attachments.zip` or other sidecar files.
- **Data source files** - all your vector and raster data, such as `.gpkg`, `.tif`, `.mbtiles` or other data source files.
- **Attachments** - all your additional project data, such as `.jpg`, `.pdf` or other files.
- **QField plugins** - all your QField plugins, usually `.qml` files.


## File versions

QFieldCloud uses file versioning.
This allows users to restore to a previous version of any modified file.
Files and file versions can be found under the **Files** section of one's projects.
Subscriptions plans allow a different number of versions per file. See the qfield.cloud [pricing page for further details](https://qfield.cloud/pricing.html).

### Deleting old file versions

To ensure that only relevant file versions are kept, and to reduce the amount of storage needed by accounts, users can delete obsolete file versions.
One can manually delete file versions from the project's **File** section.
Each file and version can be linked to a specific QFieldCloud user who uploaded it.

To delete file versions in QFieldCloud, follow these steps:

1. Go to the "Files" section of your project.![Project files](../../assets/images/files_versions_for_deleting.png)
2. Locate the layer for which you want to delete versions.![Layer selected](../../assets/images/files_versions_for_deleting_2.png)
3. Click on the three dots next to the layer name.![Clickable option](../../assets/images/files_versions_for_deleting_three_dots.png)
4. You will see a list of versions for that specific layer.![List of files versions](../../assets/images/files_versions_for_deleting_files_versions.png)
5. Identify the version you want to delete and click on the red trash bin icon next to it.![Thrash icon](../../assets/images/files_versions_for_deleting_deleting_a_version.png)
6. Confirm the deletion when prompted, if you want to delete all versions before a specific version, you can do it activating the option "Also delete `n` version(s) older than the selected version.".![Deleting files versions](../../assets/images/files_versions_for_deleting_also_delete.png)
7. After deleting a pop up message will appear with the success and the list of versions will show just the versions that was not selected for deletion.![List of versions after deleting 2 versions before](../../assets/images/files_versions_for_deleting_version_remain.png)

## Collaborators

A project collaborator is QFieldCloud user invited to contribute to a project.
A single project may have multiple collaborators.
Collaborators with roles **owner** or **admin** can add more users as collaborators.
Projects owned by an organization allow adding **teams** as collaborators. Read more about [collaborator roles](permissions.md).

## Changes

Changes made on vector layers and uploaded to QFieldCloud from a QField device will appear here.
A _change_ stores the difference between attributes or geometries before and after the upload.

Changes register which method was used for uploading; it can be one of:

- `create` - a new feature has been created.
- `delete` - an existing feature has been deleted.
- `patch` - an existing feature has been modified.

Features that have been created and later deleted without being pushed to QFieldCloud do not appear in project changes.

!!! note
    Changes to online vector layers (PostGIS, WFS) that do not have "Offline editing" cloud layer action do not generate a change, but instead modify the original data source _directly_.

!!! note
    Changes to vector layers done in QGIS will not appear here.


## Jobs

Read more about [project jobs](jobs.md).


## Secrets

Secrets are Project settings that are securely stored in an encrypted way.
Jobs will automatically have access to project's secrets.

Read more about [project secrets](secrets.md).


## Settings

Project settings are available only to project owners and collaborators with "admin" roles. _Settings_ should be handled carefully as users can modify sensitive project settings and perform unrecoverable actions.

- Change the project visibility to public.
- Change the project owner.
- Permanently delete a project.
- etc

!!! warning
    Actions issued from a project' settings page can lead to data loss!
