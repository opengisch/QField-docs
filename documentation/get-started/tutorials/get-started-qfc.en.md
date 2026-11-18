---
title: Get started
long_title: Get started with QFieldCloud
tx_slug: documentation_get-started_tutorials_get-started-qfc
---

# Get started with QFieldCloud

## What is QFieldCloud

QFieldCloud is the cloud service that allows you to syncronize data between your mobile device for fieldwork and your desktop workstation.
You can manage teams, collaborate within organizations, assign different editing permissions, and centralize project storage.

## Register to [QFieldCloud](https://app.qfield.cloud/accounts/signup/)

!!! Workflow
    1. Navigate to the [Sign up page](https://app.qfield.cloud/accounts/signup/), enter your details, and create a new QFieldCloud account.
    2. (Optional) If you received a referral code, enter it in the corresponding field.
        !![Registration form](../../assets/images/qfieldcloud_registration.png,250px)

## QFieldCloud overview

Once registered, your personal QFieldCloud landing page will show all the projects that you have access to in the center of the window.
In case that you have many projects, you can search in the search bar at the top of the page.

It is also possible to create a new empty project from this menu.
All further configuration of that project, however, needs to be done inside QGIS.
Under your profile name, you are able to edit and manage your account details and get an overview of what organizations you are a member of, as well as what collaborations you have.
Finally, once you have subscribed to a [QFieldCloud subscription plan](https://qfield.cloud/pricing), you can manage it from here.

Before getting started, familiarize yourself with the [basic concepts](../tutorials/concepts.md) of QFieldCloud.

!!! Tip
    In the project overview page, the two names indicate the project "Owner" and the project "Name".

!![QFieldCloud projects overview](../../assets/images/overview_projects_qfcloud.png, 800px)

### Filtering projects

When managing a large number of cloud projects, you can refine your project list using the **Filters** dropdown button located next to the search bar.

!![](../../assets/images/qfc_web_project_filters.png, 800px)

The dropdown menu allows you to filter projects by three primary criteria:

- **Ownership:** *(User accounts only)*:
    - **My own projects:** Displays only projects where your account is the primary owner.
    - **Shared with me:** Displays projects owned by collaborators or organizations where you have been granted access.
- **Project type:**
    - **Regular projects:** Standard QGIS mapping projects created for field data collection.
    - **Shared datasets:** Centralized datasets stored in the dedicated `shared_datasets` project repository.
    - **Template Projects:** Projects locked for fieldworkers and used exclusively as project templates.

When any filter option is active, clicking the **Clear** button immediately resets all active filter parameters and restores the full project view.

![type:video](../../assets/videos/type_filters_1.webm)

## Project creation

There are several ways to create and initialize a new project in QFieldCloud depending on your workflow.
You can convert an existing QGIS project, start from a blank template on the web, or clone an existing project.

Read more under the [Project Creation Guide](../../fieldwork/create-project.md).

## From QFieldCloud to QGIS Desktop

In order to connect to QFieldCloud, you need the QFieldSync plugin in QGIS.
The following steps show how to install the plugin and synchronize your data to and from QFieldCloud.

!!! Workflow

    1. Open the QGIS plugin manager by navigating to _Plugins > Manage and Install Plugins..._.
    2. Under **All**, find **QFieldSync** in the list and install the latest version by clicking the **Install Plugin** button.
        !![Successful installation](../../assets/images/install_qfieldsync.png)
        After a successful installation, a new toolbar appears:
        !![Toolbar](../../assets/images/qfieldsync_toolbar.png,200px)
    3. Click the <span style="color:blue"> :material-cloud: </span>  in the QFieldSync toolbar to display the login screen:
        !![](../../assets/images/qfieldsync_login_dialog.png, 250 px)
    4. Enter your account credentials created during registration.
!!! Warning
    If you use a password in QGIS for the first time, QGIS prompts you to set a master password to manage all stored passwords.
    Read more about the master password in the [QGIS documentation](https://docs.qgis.org/latest/en/docs/user_manual/auth_system/auth_overview.html#master-password). <!-- markdown-link-check-disable-line -->

## Project overview in QFieldSync

The QFieldSync project overview displays all QFieldCloud projects that you have access to from your account.
The dialog includes the following interface elements:

- The **active username** underlined in blue at the top left.
- **Your user avatar** in the top right corner to access account details or sign out.
- A <span style="color:blue"> :material-cloud: </span> to create a new QFieldCloud project at the bottom left.
- A refresh button on the right to reload your project list at the bottom right.

!![Projects overview example in QFieldSync](../../assets/images/project_overview_all_colors_tooltip.png)

Newly registered users will see an empty project table.

### Editing project properties

!!! Workflow

    1. Double-click on the name of the project for which you wish to change the properties.
    2. Make any adjustments and click save.


!!! Tip
    **Synchronize Directly from the Project List**

    You do not need to open a project in QGIS before synchronizing it with QFieldCloud.

    In the QFieldSync Project Overview list, select any locally stored project and click the Synchronize button to push or pull changes directly without loading the project in the QGIS canvas first.
    This is especially useful when you need to synchronize multiple projects at the end of a work session.

    ![type:video](../../assets/videos/qfieldsync_sync_from_project_list.webm)


### Project status

Icons in the project overview indicate both the local storage state and cloud processing status of each project:

- **Local status:**
    - ![Status](../../assets/images/cloud_project_remote.svg){Width="20px"} Indicates that only a remote cloud project exists.
    - ![Status](../../assets/images/cloud_project.svg){Width="20px"} Indicates that the cloud project is also stored locally.
- **Cloud status:** Three color-coded statuses display the current state of your cloud project.
    A tooltip shows the status of each project.
    - **Red Status:** The project is invalid and not ready for field use.
        The status message on your QFieldCloud landing page provides details to address the issue.
    - **Brown Status:** The project is currently being updated or edited.
    - **Green Status:** The project is ready for field use.
        You can download the project to QField.

### QField project settings

After installing the QFieldSync plugin, a new section appears under _Project > Properties..._.
Access these settings from the QFieldSync toolbar ![](../../assets/images/project_properties.svg){Width="20px"} using the **Settings** icon.
You can access the settings from the QFieldSync toolbar ![](../../assets/images/project_properties.svg){Width="20px"} using the **Settings** icon.
Configure the following parameters in these settings:
You can adjust the following parameters in these settings:

- Define how project layers are treated in the cloud (see the [QFieldSync Get Started Guide](./get-started-qfs.md) for details on **Packaging Actions**).
- Enable [**geofencing**](../../how-to/navigation-and-positioning/geofencing.md).
- Assign a digitizing log layer.
- Specify the layer that will be active for editing after selecting a [Map Theme](../../how-to/qfield-interface/map-interaction.md#map-themes)

We recommend using GeoPackages, especially when collaborating in teams.
Read more about supported vector formats in the [Advanced Setup Guide](advanced-setup-qfc.md).

!!! Important
    If you use experimental data sources without a primary key field (such as Shapefiles or GeoJSON), you must include a lowercase `fid` field as a primary key to uniquely identify each feature.

### Project upload

Once your project is configured in QGIS, upload it to QFieldCloud:

!!! Workflow
    1. Click the <span style="color:blue"> :material-cloud: </span> with arrows in the QFieldSync toolbar.

    Select your preferred upload method:
      - **The Local file:** Replaces your cloud file with the new local version of the project.
          When working with GeoPackages, the cloud file version is replaced by your local file version.
      - **The Cloud file:** Amends your local datasets and replaces your local project file with the current cloud version.


You can now view your project and files on your [QFieldCloud project overview page](https://app.qfield.cloud/).

## From QFieldCloud to QField

When you are ready for fieldwork, set up QField on your mobile device.

!!! Workflow

    :material-tablet: Fieldwork

    1. Download and install the latest version of QField from the Google Play Store, Apple App Store, or [download the latest release](https://github.com/opengisch/QField/releases) for Windows, Linux, or macOS.
    2. Navigate to **Cloud Projects** and log in to your QFieldCloud account on your mobile device.
        !![Welcome](../../assets/images/getting_started_splashscreen.png,250px)
        !![Login](../../assets/images/getting_started_login.png,250px)
    3. Tap a project to download it to your device.
        !![Download](../../assets/images/getting_started_download_project.png,250px)

### Advanced project searching and filtering
:material-tablet: Fieldwork

To manage a large number of projects, QField features a search-and-filter panel directly on the QFieldCloud projects screen.
The **Filter** button is located to the right of the project search bar.

#### 1. Predefined filter presets

Quick preset buttons appear at the top of the filter panel (such as **My Own Projects** or **{org_name}'s projects**).
Tapping a preset populates the criteria form and automatically filters the underlying list.

#### 2. Form-based filtering criteria

Refine your project search using the form fields in the filter pane:

- **Search term:** Selects every project title or description containing the provided term.
- **Owner:** Displays a list of unique project owners available to your account in an editable dropdown menu.
- **Include public projects:** Toggles community public projects on or off.

!!! Note
    **Public projects** are projects marked as public by any project owner.
    Public projects are viewable by all QFieldCloud users.
    if the project owner adds them as project collaborators.
    You do not need an organization account to collaborate on public projects.

#### 3. Power-User search syntax

The main search bar allows users to type advanced filter parameters directly using key-value syntax.
Key parameters are dynamically recognized and highlighted inside the text input box.

Supported syntax tokens include:

- `owner:name` — Filters the list to show projects belonging to a specific user or organization account name.
- `include:public` — Forces public projects to be included in the query evaluation.

> **Example Query:** Typing `owner:My_Organization include:public Forestry` into the search field isolates public projects matching the keyword "Forestry" owned by "My_Organization".

!![](../../assets/images/qfc_project_filters.png)

### Synchronization with QFieldCloud
:material-tablet: Fieldwork

QField will indicate whether your project has changes locally that are not yet uploaded to QFieldCloud or a new version of your project is available on QFieldCloud.

!!! Note

    1. To get notified about the project update on the cloud, you need to be online and logged in.
    2. If a new version is available, you should synchronize your project as soon as possible.

There are two ways in which you can see whether your project is up-to-date with the version on QFieldCloud.

- **Cloud Icon Badge:** A green bubble with an exclamation mark appears on the cloud button in the **Side Dashboard**.
!![](../../assets/images/qfield_cloud_sync_status_1.png)
- **Synchronize Project Card Badge:** A green badge appears on the right side of the **Synchronize project** section within the cloud synchronization.

!![](../../assets/images/qfield_cloud_sync_status_2.png,350px)


After completing field data collection, synchronize your changes back to QFieldCloud.

!!! Workflow
    1. Open the **Side Dashboard** in QField.
    2. Tap the <span style="color:blue"> :material-cloud: </span> (a badge indicates your number of pending local changes).
        !![Cloud button](../../assets/images/getting_started_blue_button.png,400px)
    3. Tap the appropriate action card for your data:
        - **Upload local changes:** Sends your edits and attachments to the cloud without downloading updates from other collaborators.
        This option is fast and saves internet bandwidth.
        - **Synchronize project:** Uploads your local edits, then downloads the latest project version from QFieldCloud to keep everything up to date.
        - **Upload history:** Tap this button below the main action cards to view a log of past uploads, including timestamps and statuses (such as **Applied**, **Pending**, **Conflict**, or **Error**).
        - **Danger zone:** Tap this button to access options for discarding un-uploaded local changes or restoring the cloud version of the project.
        Tap **Discard local changes** to remove un-uploaded local edits, or tap **Reset project** to re-download the cloud project if your local copy becomes corrupted.

        !![](../../assets/images/getting_started_actions.png,800px)

Your synchronized changes are now available to all collaborators with access to the project on QFieldCloud.

Read more in the [Advanced QFieldCloud Setup Guide](./advanced-setup-qfc.md) and [QFieldCloud Technical Reference](../../reference/qfieldcloud/workflow.md).
