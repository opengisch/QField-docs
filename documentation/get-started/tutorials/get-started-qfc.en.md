---
title: Get Started
tx_slug: documentation_get-started_tutorials_get-started-qfc
---
# Getting started guide

!!! help
    We have a [community discussion platform](https://github.com/opengisch/qfield/discussions) to discuss your questions, doubts and ideas. Do not hesitate to check it out.

## Get a QFieldCloud account

:material-monitor: Desktop preparation

Go to the [registration page](https://app.qfield.cloud/accounts/signup/), enter your details and create a new QFieldCloud account.

!![Registration form](../../assets/images/qfieldcloud_registration.png,250px)

### Edit Profile

Change your personal settings. Add a profile picture or get an overview about your ownerships and memberships in organizations.

### Organizations

Your organizations are listed here. Find out more about teams, members and their roles in [concepts of the QField Ecosystem](https://docs.qfield.org/reference/qfieldcloud/concepts/).

### Projects

Search and choose a project from the list or start to create a new project.

!![QFieldCloud projects overview](../../assets/images/overview_projects_qfcloud.png)

## Connection to QFieldCloud on QGIS Desktop

:material-monitor: Desktop preparation

In order to connect to QFieldCloud, you need the Plugin “QFieldSync” in QGIS. The next steps show you how you can install and synchronize your data to and from QFieldCloud.

### Install QFieldSync

Open the QGIS plugin manager by going to the `Plugins -> Manage and install Plugins…` menu.

Find QFieldSync in the list of plugins and install the latest version by clicking the `Install Plugin` button.

!!! note
    Since QFieldCloud is still in beta phase, there are frequent updates and fixes. Please upgrade your QFieldSync plugin often. In case of an issue, please try upgrading to the latest release before reporting.

!![Successful installation](../../assets/images/install_qfieldsync.png)

After successful installation, a new toolbar appears:

![Toolbar](../../assets/images/qfieldsync_toolbar.png)

### Login to QFieldCloud

Click the cloud icon ![](../../assets/images/cloud.svg){Width="20px"} in the QFieldSync toolbar.
A new login screen will appear:

!![Login screen](../../assets/images/qfieldsync_login_dialog.png,250px)

Enter your credentials previously created during account registration.

!!! Note
    If you use a password in QGIS for the first time, it will ask you to set a master password that manages all the other passwords used in QGIS. More information about the master password here: [QGIS documentation](https://docs.qgis.org/3.4/en/docs/user_manual/auth_system/auth_overview.html#master-password)

Explore the projects overview screen: your current user underlined and blue, a logout button down-left, a cloud button to create a new project and, on the right, a refresh button to grab the freshest project list. Newly registered users will see an empty table and as soon as they create new projects, the list will grow. The projects overview screen looks like this:

!![Projects overview in QFieldSync](../../assets/images/project_overview_all_colors_tooltip.png)

The icons indicate the cloud and local status of the different projects.

Local status:

![Status](../../assets/images/cloud_project_remote.svg){Width="20px"} indicates that there is only a remote cloud project existing.
![Status](../../assets/images/cloud_project.svg){Width="20px"} indicates that the cloud project is also locally stored.

Cloud status:

Red: status failed —> the project is invalid and is not understood by the cloud. The user needs to fix/upload their .qgs/.qgz project.
Brown: status busy —> we are working on your project, please be patient. You cannot do much with the project in the meanwhile.
Green: status ok —> the project is successfully undestood by the cloud. You can try to download on QField, but the success is not guaranteed.

The status of each project is shown with a tooltip.

By double-clicking on a project in the list, you can see and edit the specific project properties.

!![Project properties in QFieldCloud](../../assets/images/project_properties_settings.png)

### Change the default QFieldCloud server in QField and QField Sync

QField and QFieldSync connect to the QFieldCloud service on [app.qfield.cloud](https://app.qfield.cloud/) by default.

You can modify the default QFieldCloud server QField and QFieldSync connect to:

1. Open the login screen in QField or QFieldSync.
2. Double-tap on the Nyuki icon (the blue bee QFieldCloud logo).
3. This action will reveal a field where you can enter the preferred QFieldCloud server address.
4. Enter the details of the desired server in the provided field.
(Leaving the field empty will connect to the default QFieldCloud server at app.qfield.cloud.)

!![Reveling server in QField Sync](../../assets/images/changing_default_qfieldcloud_server_qfield_sync.png,250px)

!![Reveling server in QField](../../assets/images/changing_default_qfieldcloud_server_qfield.png,250px)

### Create and configure your Cloud project

Create a new project by clicking the cloud button, down-left. First, you will need to choose how to create the new project between

* "Convert currently open project to cloud project"
  A new QFieldCloud-compatible project is created from the currently opened QGIS project. In order to do so, datasets will be copied into an export directory that will act as your local mirror. Vector datasets will be converted to geopackage format to facilitate data synchronization from multiple devices while other dataset types will be copied to the new project lotation.

To convert a current project, a completely empty directory is mandatory.

* "Create a new empty QFieldCloud project"
  A new blank QFieldCloud project will be created. You will be responsible to move all the project-related files within the selected local directory, with the project file at its root. Project files will only be uploaded when you click the synchronize button. Make sure the selected contains no more than one QGIS project file.

!![Project details](../../assets/images/create_project.png)

A form will ask you for project name, description and local directory. In the local directory you can get different situations:

* The entered path does not contain a QGIS project file yet.
* The entered path contains one QGIS project file.
* Please select local directory where the project to be stored.
* The entered path is a relative path. Please enter an absolute directory path.
* The entered path is not an directory. Please enter a valid directory path.
* The entered path is not an existing directory. It will be created after you submit this form.
* Multiple project files have been found in the directory. Please leave exactly one QGIS project in the root directory.

### Configure your project layers for QField

Configure the project layers by clicking the fifth icon in the QFieldSync toolbar ![](../../assets/images/project_properties.svg){Width="20px"}. Here you can configure QFieldCloud layer actions. Most of the time you need to configure a preference either to online or offline layers. For more fine grained control, in the advanced settings you can configure the action layer by layer. Get more information about how to configure your layers in the [Get Started guide for QFieldSync](./get-started-qfs.md)!.

It is recommended to use GeoPackage layers for collaborative editing. See the [advanced setup guide](advanced-setup-qfc.md) for more information about vector formats support.

!!! note
    If you use experimental data sources without a primary key field (e.g. Shapefiles, GeoJSON etc), you must have a lowercase `fid` field that will be used as a primary key that uniquely identifies each feature.

Any QField supported raster and vector layer formats may be used as read-only data.

!![Project properties](../../assets/images/getting_started_project_properties.png)

### Upload a project

Once configured, you can press the cloud button to open the synchronization dialog. Here you have to decide what do you prefer: the local file or the file on the cloud.

!![Synchronize](../../assets/images/getting_started_synchronize.png)

Now you should see your project and files on [QFieldCloud](https://app.qfield.cloud/)

## Field device

:material-tablet: Fieldwork

### Install QField

Download and install the latest version of [QField from the play store](https://play.google.com/store/apps/details?id=ch.opengis.qfield_dev). Scroll to the bottom and enable beta testing.
Do not use this version in production!

!!! note
    Since QField 2.0 is still in beta phase, there are regular updates and fixes at least on a weekly basis. Please upgrade your experimental QField at least once a week. In case of an issue, please try to reproduce on the latest release before reporting.

### Start working on your project

!![Welcome](../../assets/images/getting_started_splashscreen.png,250px)

Login with your username and password

!![Login](../../assets/images/getting_started_login.png,250px)

Select a project to download on your device:

!![Download](../../assets/images/getting_started_download_project.png,250px)

### Synchronise your changes

Make a change to your project. Either create a new feature, delete a feature, or modify the geometry or attributes.
Open the blue cloud button on the top left of the screen:

!![Cloud button](../../assets/images/getting_started_blue_button.png,250px)

Choose an action with the change you made to your project. Each of the actions have an explanation what you should expect to happen:

!![Actions](../../assets/images/getting_started_actions.png,250px)

Your changes are now available to everyone who has access to your project on the cloud.

You can find more information on [Advanced QFieldCloud setup](./advanced-setup-qfc.md) and [QFieldCloud technical reference](../../reference/qfieldcloud/concepts.md).
