---
title: My first project
long_title: My first project using QGIS and QField with QFieldCloud
tx_slug: documentation_get-started_tutorials_myfirstproject
---

# My first project

This page will go through a step by step example of how to prepare a simple QGIS project containing a GeoPackage and a basemap.
It will include the configuration of a simple attribute form and the styling of the feature layer.

## Step-by-step Example

**Used case**

[Maya Mielena](../../assets/images/maya_waving.gif)

*Hi, my name is Maja Mielena, I am a retired GIS Specialist and I will show you how to prepare a simple QGIS project so that you can use it inside the QField application*
*We will create a Geopackage containing a point layer and a line layer.*
*This will allow you to go out into nature and record your personal points of interests and track yourself using the line layer.*

*Let's get started!*

### QGIS Project - Adding new data

1. Open a new QGIS Project on your desktop.
2. Add a basemap of your choice to the project.

    1. Under the browser on the top left of the QGIS window you will find the dropdown *XYZ Tiles*.
    2. From there you can add the OpenStreetMap basemap, which is the most commonly used basemap.
3. We will now locate our area of interest.
There exists a very useful QGIS plugin called *OSM Place Search*, which allows you to browse through the different place features available in the OpenStreetMap data.
    1. Under *Plugins* in the Menu toolbar direct to *Manage and Install Plugins*
    2. In the search bar type *OSM Place Search* and install the plugin
    3. A new window should appear in the side panel where you can enter your place of interest
    4. Add it to your project as a feature by clicking on the middle button at the bottom of the plugin interface.
    5. A new feature layer will be available as a temporary layer in your project.
4. Adding a new layer

        Great, now that we have located our area of interest, we can add a new feature layer to the project.

    1. Click on *Layer* and  create a new *Vector Layer*
    2. Give your Gpkg a general name.
    Additionally give a name to the table (which we are about to create).

        **To Note**: A Gpkg can consist of several layers, including points, lines, polygons and raster layers.
    3. Select *Point* as your geometry type and select the *EPSG:3857 WGS84/Pseudo-Mercator* as your coordinate system

        We will add a few fields to our layer including a name, a date, a field for a photo, a field for categorizing the point and a boolean field, which we will use to indicate whether it is worth to revisit the point or not.
        Finally, we will add another field where you can add general notes.
    4. Add the following:

        1. Name - *string*
        2. Entrydate - *date*
        3. Visit - *Boolean*
        4. Category - *string* --- We will use this to create a dropdown list from which you can select the point of interest category
        5. Attachment - *string*
        6. Notes - *string*
5. Adding a Line layer

    We will create another layer within the GPKG corresponding to a line layer.
    You can use it to track yourself when going into the field.

    1. Add a new layer as previously
    2. Select the same GPKG as *file name* but give the *table* a different name.
    3. Add the following fields:

        1. Name - *string*
        2. Date - *date*


6. Saving the temporary layer in GPKG

    Remember that we have added our area of interest as a *temporary layer* meaning that after closing the project we will not be able to access the layer anymore.
    Therefore, we will save the layer within the just newly created GPKG.

    1. Right-click on the layer and select *Make Permanent*
    2. Find the GPKG file that you just created and add an appropriate name to the PoI layer.

### QGIS Project - Attribute configuration

Now we have all the essential data in the QGIS project that we need for the data collection.
However, in order to have a well structured form we need to configure the attribute form, via the file properties.

1. Open the project properties of the *PoI* Layer
2. Direct to *Attributes Table* and select *Drag and Drop Designer* from the dropdown.

    From here you can control the appearance of your form.
    We do not need to edit the *fid* field. QGIS creates this for every GPKG by default.
3. Remove the *fid* field from the visible fields by pressing the *red minus* on the window.
4. *Name*: Click on *Name* and look and see the Widget Display options on the right-hand side.
