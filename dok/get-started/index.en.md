---
title: Get started
---

# Get started with QField, QFieldCloud and QFieldSync

## QField - your mobile [Q]GIS solution

QField allows you to efficiently work on your GIS data outdoor.

QField's optimized user interface hides the full power of
[QGIS](https://qgis.org) under the hood.

![type:video](https://player.vimeo.com/video/376372805)

### Concepts

QField was designed with a few key concepts in mind.

#### Keep it simple

The requirements on the field are not the same as on a desktop. The
screen is smaller, the input devices are different and the tasks are
different.

QField aims to help users to perform the tasks they need to do without
cluttering the user interface. This means, that only tasks which need to
be done on the field are availble from the interface. Everything else is
not.

This means that everything like layer styling, form definitions and
other project setup steps should be done on a computer with QGIS
installed first.

#### Be compatible with QGIS

QField is based on QGIS. It is not a rebuild of QGIS it really *does*
use QGIS libraries. The rendering engine is exactly the same as in QGIS
for desktop and your project will therefore look exactly the same on
your mobile device as it does on your computer.

If something is already available as a configuration option in a QGIS
project, it should not be re-invented. QField therefore uses the same
edit widgets as QGIS desktop does. If a project is already configured
for the desktop, it should just run on mobile as well.

Remember, this is just the *concept*. This is what we have in mind when
we develop QField. It does not mean that it is already completely there
yet.

#### Mode based

QField is built around *modes*. Modes are similar to a *map tool* in
QGIS desktop. A mode defines the task which a user is currently doing.
Either a user is *browsing* through the data or she is *digitizing*
something new.

## QFieldCloud

Seamlessly integrate your team's field work, QFieldCloud's unique
technology allows your team to focus on what's important, making sure
you efficiently get the best field data possible.

Thanks to the tight integration with QField, your team will be able to
start surveying and digitising data in no time.

!!! tip

    Subscribe now at: <https://qfield.cloud>

## QFieldSync plugin

The QFieldSync plugin helps preparing and packaging QGIS projects for
QField.

QFieldSync supports your project preparation with automating the
following:

-   Required steps for project setup (e.g.
    `portable_project`)
-   Creating basemaps from a single raster layer or from a style defined
    in a map theme.
-   Configuring the offline editing functionality and synchronizing
    changes back.

### Workflow

To get a quick overview of the process, here is a list of typical steps:

1.  Create a QField package. This is a working copy in a separate
    folder.
2.  Copy the QField package to the target device.
3.  Go out and collect data.
4.  Copy the modified data back to your desktop computer.
5.  Synchronize the modified data with your database or files.

### Installation

In QGIS, open the plugin library and search for **qfield sync**. Select
the plugin in the list and click on **Install**.

!![image](../assets/images/qfield-sync_install.png)

### Configuration

The project configuration is saved in the master .qgs project file. This
way it is possible to pre-configure a project once and use it
repeatedly.

!![image](../assets/images/qfield-sync_configmenu.png)

#### Layer configuration

!![image](../assets/images/qfield-sync_config.png)

In the project configuration dialog, an *action* can be defined for each
layer individually. Depending on the layer type, different types of
actions are available.

Copy

:   The layer will be copied to the package folder. This is only
    available for file-based layers.

No action

:   The layer source will be left untouched. This is only available for
    non-file-based layers like WMS, WFS, Postgis\...

Offline editing

:   A working copy of the layer is copied into the package folder. Every
    change which is done in the packaged project during work is recorded
    in a changelog. When synchronizing the changes back later on, this
    log will be replayed and all changes also be applied to the main
    data base. There is no conflict handling in place.

Remove

:   The layer will be removed from the working copy. This is useful if a
    layer is used in the basemap and will not be available in the
    packaged project.

#### Base map configuration

A base map is a raster layer which is added as the bottommost layer to
the packaged project file.

If the base map option is enabled, a base map will be rendered, whenever
the project is packaged. The area of interest - the extent which will be
rendered -will be chosen at packaging time.

There are two possible sources for a base map:

Layer

:   A raster layer. This is useful to take an offline copy of an online
    layer like a WMS or to take a working copy of an unsupported format
    like an ECW or MrSID layer.

Map Theme

:   A map theme. This is useful to create a base map based on a
    combination of several layers with styling. These layers can then be
    removed from the working package and do not need to be rendered on
    the device. This can save some disk space and battery on the device.

The tile size defines the spatial resolution. It determines the number
of map units per pixel. If the map canvas CRS has meters as units and
tile size is set to 1, each raster pixel will have a spatial extent of
1x1 m, if it is set to 1000, each raster pixel will have a spatial
extent of 1 square kilometer.

#### Offline editing configuration

If *only synchronize features in area of interest* is checked, only
features which are within the extent of the map canvas as packaging time
will be copied to the offline editing working copy.

### Package for Qfield

Once the project is configured, package it in a folder. This folder will
contain the .qgs and the data used in it.

!![image](../assets/images/qfield-sync_package.png)

Copy the folder on your device. Open Qfield, open the project and start
collecting data.

Make also sure to save the QGIS project using the regular Save As of
QGIS as you'll have to re-open it later when you want to synchronize
the changes.

### Synchronize from Qfield

When you want to synchronize what you have collected, re-open the
project in QGIS (the one you saved with a regular Save As).

Copy the project folder from your device to your computer and use the
**Synchronize from Qfield** menu to synchronize your changes from the
protable project to the main project.

!![image](../assets/images/qfield-sync_sync.png)

Make sure that you synchronize your data back only once. That means, if
you go out again to collect more data, you should create a new QField
package before to avoid sync problems later on (like e.g. duplicates).
