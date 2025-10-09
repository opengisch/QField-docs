---
title: Advanced Setup
tx_slug: documentation_get-started_tutorials_advanced-setup-qfc
---

# Advanced setup guide

## Supported vector providers

Currently, QFieldCloud supports GeoPackage and PostGIS layers for collaborative editing.
Other formats supported by QGIS should also work but are not officially supported.

## Working with GeoPackages

Using GeoPackages is usually the best choice for a simple setup to centralize data collected by your QField users to one single file.

If you would like to set up a relation, add a UUID field and use that as the primary or foreign key.

!!! Note
    Do not use the default `fid` field for relations (as primary or foreign key).
    It will lead to errors over time.

### Example workflow (GeoPackage)

:material-monitor: Desktop preparation

1. Create a new project.
2. Create GeoPackage layers, save it in the same folder than the QGIS project.
3. Set the GeoPackage to "Offline editing" in the QFieldSync plugin.
4. Upload the project to QFieldCloud.

:material-tablet: Fieldwork

1. Sign in to QFieldCloud and download the project to your device.
2. Collect and edit some data and upload the changes.

:material-monitor: Desktop

1. Using QFieldSync, download the updated files (the GeoPackage file should have changed).

!!! warning
    This workflow does not support changing the GeoPackage on the desktop, as being file-based, the whole GeoPackage will be replaced.
    This means that data can only be digitized using QFieldCloud.

## PostGIS

Using PostGIS layers is a good choice if your data should directly be editable for multiple users through QFieldCloud when they sync their work without any further steps.

It requires your database to be publicly accessible, and credentials must be saved unencrypted in the QGIS project.
Please be aware of the security implications of such requirements, and remember to have backups.

### Example workflow (PostGIS)

:material-monitor: Desktop preparation

1. Create a new project.
2. Create add a PostGIS layer, making sure to store the credentials in the project.
3. Make sure the PostGIS database connection is publicly accessible (public IP or domain name, it will not work with `127.0.0.1` or `localhost`).
4. In the QFieldSync project settings, set the GeoPackage to "Offline editing" if your QField users will not have a reliable internet connection in the field or "Direct database access".
5. Upload the project to QFieldCloud.

:material-tablet: Fieldwork

1. Sign in to QFieldCloud and download the project.
2. Collect some data
3. Push or synchronize the changes once back at the office if you were using `offline editing`.

:material-monitor: Desktop

1. All changes should be directly visible inside the PostGIS database.

!!! note
    When using `direct database access`, QFieldCloud will directly edit data in the PostGIS database.
    This will only work with a reliable internet connection in the field, but has the advantage that all data is directly visible to all users and allows to use any PostGIS specific setup (triggers, generated fields, etc).

!!! note
    When using `offline editing`, QField will work on a local copy of the database in a GeoPackage, which will be synced by QFieldCloud to the original database once synchronized by the user.
    We recommend to use this option to avoid unnecessary data losses in case of lost data connection.

    Changes will only be visible to users once the Synchronisation via QFieldCloud has been applied on the different devices.
    When a local copy is created, advanced PostGIS operations (like triggers) will not be available on QField.

You can find more information on [QFieldCloud technical reference](../../reference/qfieldcloud/jobs.md).

## Restriction of Project Files

To prevent any modification to the core QGIS project file, **the project administrators** can restrict the access to these files.
This can be achieved under the settings section in QFieldCloud.

1. From the QFieldCloud homepage direct to *Settings*
2. Enable the **`Restrict project files`** button

!![](../../assets/images/restric_qfc_project_files.png)

Once set, only administrators and managers will be able to push changes to the files listed above.
Other project collaborators can still upload and modify other project files, such as data in GeoPackages, but they cannot alter the main project file or its core components.

### Restricted Files

When enabled, the following files can only be modified or uploaded by a user with an "admin" or "manager" role for the project:

- The primary **QGIS project file** (e.g., `my_project.qgz`).
- The **attachments zip archive** associated with the project (e.g., `my_project_attachments.zip`).
- **QGIS auxiliary data files** that store information like label positions (e.g., `my_project.qgd`).
- **QField style files** (`.qml`) that share the same name as the project file.


## Automatic push to QFieldCloud

With this functionality, you can enforce automatic pushing of pending changes to QField devices in the field, as well as specify the interval in between automated pushes.
The functionality is activated through a project setting, allowing remote activation.

:material-monitor: Desktop preparation

1. **Access Project Settings**: Direct to *Project* > *Properties...* > *QField* > *QFieldCloud Packaging*
2. **Enable Auto-Push**: Toggle the "Automatically push pending changes on the following interval" option and establish your preferred interval.

!![Auto push QFieldSync](../../assets/images/auto-push-pending-changes-qfieldsync.png)

!![Auto push QField](../../assets/images/auto-push-pending-changes-qfield.png,400px)

!!! note
    **Benefits:**
    - *Real-Time Updates*: Ensures prompt Synchronisation of field data with the QFieldCloud project.
    - *Streamlined Workflow*: Minimizes manual intervention and ensures surveyors do not need to worry about Synchronisation, helping them focus on data quality.
    **Considerations:**
    - *Network Stability*: Ensure stable internet connectivity for auto-push functionality.
    - *Battery Optimization*: Implement strategies to mitigate battery consumption on QField devices during prolonged fieldwork.

## Project creation in an organisation

How to create a project in an organization:

### Option 1: Using QField Sync

1. Follow the steps [configure your cloud project](../../get-started/tutorials/get-started-qfc.md#project-creation-and-configuration), until you get to the "Project details".

2. Change the owner of the project to your Organization.

    ![Project files over view in QFieldCloud](../../assets/images/converting-project-to-organization-01.png)

3. Click on "Create" to start the conversion and Synchronisation.
    When finished the project will appear in the list of projects of your Organization in QFieldCloud.

    ![Project files overview in QFieldCloud](../../assets/images/converting-project-to-organization-02.png)


### Option 2: Using QFieldCloud

1. In the QFieldCloud landing page direct to your organization.

    ![Entering into Organization](../../assets/images/project_organization_01_entering_into_organization.png)

2. Click on "Create a project".

    ![Creating Project](../../assets/images/project_organization_02_creating_project.png)

3. Select "Create a new empty project"

    ![New empty project](../../assets/images/project_organization_03_new_empty_project.png)

4. You can see the new project in the overview.

    ![New project created](../../assets/images/project_organization_04_new_project_created.png)

5. In QGIS open QFieldSync and you will see the new project listed, click on "Edit Selected Cloud Project".

    ![QFieldSync](../../assets/images/project_organization_05_qfield_sync.png)

6. Choose the folder where you want to save the project.

    ![Selecting folder](../../assets/images/project_organization_06_selecting_folder.png)

7. In the selected folder, you can either paste an already worked-on project or save a new one.

    ![Copy to project folder](../../assets/images/project_organization_07_copy_project_to_folder.png)

8. Once the folder contains the project, you can synchronize it.

    ![QFieldSync Overview](../../assets/images/project_organization_08_qfield_sync_overview.png)

9. Finally, push the changes to the cloud.

    ![Pushing changes to QFieldCloud](../../assets/images/project_organization_09_pushing_changes_to_cloud.png)

10. You can verify that the files are present in the Organization project.

    ![Project files over view in QFieldCloud](../../assets/images/project_organization_10_files_overview_in_cloud.png)

### Option 3: Changing the Ownership of a project

1. On the QFieldCloud landing page, click on your project of concern.
2. Direct to the *Settings* and select "Transfer ownership of this project" and choose the desired Organization for the transfer.

    ![Transferring to Organization](../../assets/images/project_organization_11_transfering_to_organization.png)

3. A pop-up window will appear to confirm the transfer. To proceed, you will need to type the requested text and click "Transfer project".

    ![Confirm transfer](../../assets/images/project_organization_12_confirming_transfer.png)

## Activate email notifications for QFieldCloud changes

If you wish to be notified by QFieldCloud what happens to your team(s) and your projects, you can activate the email notification option.

1. On your QFieldCloud landing page direct to *settings*.
2. Navigate to the notifications section.
    Here, you can customize the frequency of notifications you wish to receive at the email address registered with your account.

![Synchronize](../../assets/images/frequency_notifications_settings.png)

The events you get notified about are:

- User created
- Organization created
- Organization deleted
- Organization membership created
- Organization membership deleted
- Team created
- Team deleted
- Team membership created
- Team membership deleted
- Project created
- Project deleted
- Project membership created
- Project membership deleted

You will receive notifications for events in which you are not the actor.
These notifications are specifically for events that are initiated by other members of your organization or collaborators on your projects.

## Enhance your project with the "Optimized Packager"

We recommend using the new "Optimized Packager" over the deprecated "QGIS Core Offline Editing" for all your projects.
The "Optimized Packager" supports consolidating filtered layers of same datasource into a single offline layer, respecting distinct symbology but also using less storage.

1. On the QFieldCloud landing page and select the project of concern
2. Direct to *Settings* and set the packager under "Packaging Offliner" in the "Settings" tab of your project.

Here is an example to illustrate this feature:

**Example Configuration:**

- **Layer 1.1:**
  - Data Source: `layers.gpkg`
  - Table: `layer1`
  - Filter: `id % 2 = 1`

- **Layer 1.2:**
  - Data Source: `layers.gpkg`
  - Table: `layer1`
  - Filter: `id % 2 = 0`

**Result:**

For the new offliner:

- A single layer is generated in the offline GeoPackage, combining data from `layer1` with the specified filters.

For the old (QGIS) offliner:

- Two separate layers are created, each representing the filtered datasets:
  - Layer 1: Filtered with `id % 2 = 1`
  - Layer 2: Filtered with `id % 2 = 0`

!![](../../assets/images/qfc_offline_packager.png,700px)

!!! note
    This configuration must be set in the Settings page of each project in [QFieldCloud](https://app.qfield.cloud/).

## Configuration of Attachment Folders

If your project contains photos, documents or other attachments, you have to configure your QGIS project accordingly to ensure that the data are downloaded to your QField device.

1. In QGIS navigate to *Project* > *Properties...* > *QField*.
2. Add your folder's path to the "Attachments and Directories" list.
    The path you enter must be relative to the location of your project file.

!!! example
    You used pictures for a specific symbology.
    These are stored in a folder named "assets" located inside your project home folder.
    Add them under the folder name to the list.

!![](../../assets/images/attachments_and_directories_list.png)

## On-Demand Attachment Downloads

For projects with many attachment files, you can enable on-demand downloading in QField.
This is useful for saving storage space on field devices and reducing data transfer over limited network connections.

To enable this feature:

1. From the QFieldCloud landing page, select your project.
2. Direct to *Settings*.
3. Enable the "On demand attachment files download" option.

!!! note
    This feature can be activated during project creation or enabled at any time for existing projects.

!![](../../assets/images/activating_on_demand_attachments_download.png)

## Connect to a custom QFieldCloud server in QField and QFieldSync

QField and QFieldSync connect to the QFieldCloud service [app.qfield.cloud](https://app.qfield.cloud/) by default.

You can modify the default that QField and QFieldSync connect to:

1. Open the login screen in QField or QFieldSync.
2. Double-tap on the Nyuki icon (the QFieldCloud logo).
3. This action will reveal a field where you can enter the preferred QFieldCloud server address.
4. Enter the details of the desired server in the provided field.
(Leaving the field empty will automatically connect to the default [QFieldCloud server](https://app.qfield.cloud/))

!![Revealing server in QFieldSync](../../assets/images/changing_default_qfieldcloud_server_qfield_sync.png,250px)

!![Revealing server in QField](../../assets/images/changing_default_qfieldcloud_server_qfield.png,250px)

!!! note
    QField will remember the last entered URL for future sessions.
    It's important to note that QFieldSync does not support the same cloud project in multiple QGIS profiles.
    As a recommendation use a single QGIS profile for your QFieldCloud projects to avoid Synchronisation issues.
