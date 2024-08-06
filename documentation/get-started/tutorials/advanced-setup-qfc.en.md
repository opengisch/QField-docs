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
    4. Upload the project to QFieldCloud.
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


## Enabling automatic pushing of changes to QFieldCloud

With this functionality, users and managers of QFieldCloud projects can enforce automatic pushing of pending changes to QField devices in the field, as well as specify the interval in between automated pushes. The functionality is activated through a project setting, allowing remote activation.

1. **Access Project Settings**: Navigate to the QField panel in the Project Settings dialog provided by the QFieldSync plugin.

2. **Enable Auto-Push**: Toggle the "Automatically push pending changes on the following interval" option and establish your preferred interval.

!![Auto push QFieldSync](../../assets/images/auto-push-pending-changes-qfieldsync.png)

!![Auto push QField](../../assets/images/auto-push-pending-changes-qfield.png,400px)

!!! Note
    **Benefits:**

    - **Real-Time Updates**: Ensures prompt synchronization of field data with the QFieldCloud project.
    - **Streamlined Workflow**: Minimizes manual intervention and ensures surveyors do not need to worry about synchronization, helping them focus on data quality.

    **Considerations:**

    - **Network Stability**: Ensure stable internet connectivity for auto-push functionality.
    - **Battery Optimization**: Implement strategies to mitigate battery consumption on QField devices during prolonged fieldwork.

## Create a project in an organization

How to create a project in an organization:

**Option 1: Directly convert your local project to an Organization QFieldCloud project:**

1. Follow the steps [configure your cloud project](#create-and-configure-your-cloud-project), until you get the "Project details".

2. Change the owner of the project to your Organization.

    ![Project files over view in QFieldCloud](../../assets/images/converting-project-to-organization-01.png)

3. Click on "Create" to start the conversion and synchronization. When finish you will see the project is in your Organization in QFieldCloud.

    ![Project files over view in QFieldCloud](../../assets/images/converting-project-to-organization-02.png)

!!! note
    QField Sync 4.6 or newer is required for this functionality

**Option 2: Uploading directly to the organization:**

1. Select your organization.

    ![Entering into Organization](../../assets/images/project_organization_01_entering_into_organization.png)

2. Once you get into the organization, click on "Create a project".

    ![Creating Project](../../assets/images/project_organization_02_creating_project.png)

3. Select "Create a new empty project".

    ![New empty project](../../assets/images/project_organization_03_new_empty_project.png)

4. You can see the new project in the overview.

    ![New project created](../../assets/images/project_organization_04_new_project_created.png)

5. On QGIS in QFieldSync, you will see the new project listed, click on "Edit Selected Cloud Project".

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

**Option 3: Moving the project from your own account to the Organizations:**

1. If you already have a project in QFieldCloud (refer to [configure your cloud project](#create-and-configure-your-cloud-project)). In the project, click on "Settings" and select "Transfer ownership of this project" to choose the desired Organization for the transfer.

    ![Transferring to Organization](../../assets/images/project_organization_11_transfering_to_organization.png)

2. A pop-up window will appear to confirm the transfer. To proceed, you will need to type "Here be dragons" and click "Transfer project".

    ![Confirm transfer](../../assets/images/project_organization_12_confirming_transfer.png)

## Activate email notifications for QFieldCloud changes

1. Access the Settings of your account.
2. Navigate to the Notifications section. Here, you can customize the frequency of notifications you wish to receive at the email address registered with your account.![Synchronize](../../assets/images/frequency_notifications_settings.png)

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

You will receive notifications for events in which you are not the actor. These notifications are specifically for events that are initiated by other members of your organization or collaborators on your projects.

## Enhance your project with the "Optimized Packager"

We recommend to use the new "Optimized Packager" over the deprecated "QGIS Core Offline Editing" for all your projects. Set the packager under "Packaging Offliner" in the "Settings" tab of your project.

The "Optimized Packager" supports consolidating filtered layers of same datasource into a single offline layer, respecting distinct symbology but also using less storage. Here is an example to illustrate this feature:

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
- A single layer is generated in the offline geopackage, combining data from `layer1` with the specified filters.

For the old (QGIS) offliner:
- Two separate layers are created, each representing the filtered datasets:
  - Layer 1: Filtered with `id % 2 = 1`
  - Layer 2: Filtered with `id % 2 = 0`

!![](../../assets/images/qfc_offline_packager.png,700px)

!!! note
    This configuration must be set in the Settings page of each project in [QFieldCloud](https://app.qfield.cloud/).

## Connect to a custom QFieldCloud server in QField and QFieldSync

QField and QFieldSync connect to the QFieldCloud service on [app.qfield.cloud](https://app.qfield.cloud/) by default.

You can modify the default QFieldCloud server QField and QFieldSync connect to:

1. Open the login screen in QField or QFieldSync.
2. Double-tap on the Nyuki icon (the blue bee QFieldCloud logo).
3. This action will reveal a field where you can enter the preferred QFieldCloud server address.
4. Enter the details of the desired server in the provided field.
(Leaving the field empty will connect to the default QFieldCloud server at app.qfield.cloud.)

!![Reveling server in QField Sync](../../assets/images/changing_default_qfieldcloud_server_qfield_sync.png,250px)

!![Reveling server in QField](../../assets/images/changing_default_qfieldcloud_server_qfield.png,250px)

!!! Note
    It's important to note that QFieldSync does not support the same cloud project in multiple QGIS profiles. As a recommendation use a single QGIS profile for your QFieldCloud projects to avoid synchronization issues.
