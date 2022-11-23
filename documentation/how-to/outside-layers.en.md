---
title: Shared local datasets
tx_slug: documentation_how-to_outside-layers
---

# Shared local datasets

It is possible to use a layer which is stored outside the project folder.

This is useful if a basemap is used in more than one project, for example a large
orthophoto. In this case, you can share this dataset among different projects.

## Add a layer outside of exported project folder
:material-monitor: Desktop preparation

In QGIS, open  *Options > Data Sources > Localized Data Paths*. In there, add the path to the external data.

!![Data Sources](../assets/images/external_path.png)

To use layers from localized data paths on your device, add the datasets to the folder `<drive>:/Android/data/ch.opengis.qfield/files/QField/basemaps`.

!!! note
    Since QField 2 the basemaps files needs to be stored in the app directory `<drive>:/Android/data/ch.opengis.qfield/files/QField/basemaps` instead of the devices main directory `<drive>:/QField/basemaps`.
