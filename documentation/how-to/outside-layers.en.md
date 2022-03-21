---
title: Outside Layer
---

# Outside Layer
In a QField project it is possible to use a layer outside the project
folder, like a basemap.

It is useful if a basemap is used in all your project, no need to copy
it everytime in the project folder.

## Add a layer outside of exported project folder
:material-desktop-mac:{ .device-icon } Desktop preparation

In QGIS, open  *Options > Data Sources > Localized Data Paths*. There add the path to the folder where are the external data.

!![Data Sources](../assets/images/external_path.png)

To make it works in the device, add the layers in the folder `<drive>:/Android/data/ch.opengis.qfield/files/QField/basemaps`.

!!! note
    Since QField 2 the basemaps files needs to be stored in the app directory `<drive>:/Android/data/ch.opengis.qfield/files/QField/basemaps` instead of the devices main directory `<drive>:/QField/basemaps`.