---
title: My first project
long_title: My first project using QGIS and QField with QFieldCloud
tx_slug: documentation_get-started_tutorials_myfirstproject
---

# My first project

This page will go through a step by step example of how to prepare a simple QField project containing a points layer, a line layer and a basemap.
It will include the configuration of a simple attribute form and the styling of the feature layer.

## Step-by-step Example

**Used case**

!![Maya Mielena](../../assets/images/maya_waving.gif, 100px)

*Hi, my name is Maya Mielena, I am a retired GIS Specialist and I will show you how to prepare a simple QGIS project so that you can use it inside the QField application*
*We will create a GeoPackage (Gpkg) containing a point layer and a line layer.*
*This will allow you to go out into nature and record your personal points of interests and track yourself using the line layer.*

*Let's get started!*

### QGIS Project - Adding new data

1. Open a new QGIS Project on your desktop.
2. Add a basemap of your choice to the project.

    1. Under the browser on the top left of the QGIS window you will find the dropdown *XYZ Tiles*.
    2. From there you can add the OpenStreetMap basemap, which is the most commonly used basemap.

    !![Adding a basemap](../../assets/images/new-project-empty-window.png, 800px)

3. We will now locate our area of interest.
There exists a very useful QGIS plugin called *OSM Place Search*, which allows you to browse through the different place features available in the OpenStreetMap data.
    1. Under *Plugins* in the Menu toolbar direct to *Manage and Install Plugins*
    2. In the search bar type *OSM Place Search* and install the plugin
    !![OSM Place Search Plugin](../../assets/images/new-project-osmplugin.png)
    3. A new window should appear in the side panel where you can enter your place of interest
    4. Add it to your project as a feature by clicking on the middle button at the bottom of the plugin interface.
    !![New PoI](../../assets/images/new-project-poi.png, 800px)
    5. A new feature layer will be available as a temporary layer in your project.
4. Adding a new layer:
    1. Click on *Layer* and  create a new *Vector Layer*
    !![New Vector layer](../../assets/images/new-project-vectorlayer.png)
    2. Give your Gpkg a general name.
    Additionally give a name to the table (which we are about to create).
    **To Note**: A Gpkg can consist of several layers, including points, lines, polygons and raster layers.
    3. Select ***Point*** as your geometry type and select the *EPSG:3857 WGS84/Pseudo-Mercator* as your coordinate system.
    We will add a few fields to our layer including a name, a date, a field for a photo, a field for categorizing the point and a boolean field, which we will use to indicate whether it is worth to revisit the point or not.
    Finally, we will add another field where you can add general notes.
    4. Add the following:

        | Attribute | Data type|
        | --- | ---|
        | Name | *string* |
        | Entrydate | *date*|
        | Visit | *Boolean*|
        | Category | *string* --- We will use this to create a dropdown list from which you can select the point of interest category|
        | Attachment | *string* |
        | Notes | *string* |

5. Adding a Line layer

    We will create another layer within the Gpkg corresponding to a line layer.
    You can use it to track yourself when going into the field.

    1. Add a new layer as previously
    2. Select the same Gpkg as *file name* but give the *table* a different name.
    !![Line Layer](../../assets/images/new-project-anotherlayer.png, 800px)
    3. Add the following fields:

        | Attribute | Data type|
        | --- | ---|
        | Name | *string* |
        |Date | *date* |


6. Saving the temporary layer in Gpkg

    Remember that we have added our area of interest as a ***temporary layer*** meaning that after closing the project we will not be able to access the layer anymore.
    Therefore, we will save the layer within the just newly created Gpkg.
    !![Make permanent](../../assets/images/new-project-make-permanent.png, 800px)

    1. Right-click on the layer and select ***Make Permanent***
    2. Find the Gpkg file that you just created and add an appropriate name to the PoI layer.
    Watch out: QGIS will ask you whether you wish to ***add new*** or to ***overwrite*** the layer.
    Of course, you choose to ***add new*** the layer.


### QGIS Project - Attribute configuration

Now we have all the essential data in the QGIS project that we need for the data collection.
However, in order to have a well structured form we need to configure the attribute form, via the file properties.

1. Open the project properties of the *PoI* Layer
!![Vector properties](../../assets/images/new-project-properties.png)
2. Direct to *Attributes Table* and select *Drag and Drop Designer* from the dropdown.
    From here you can control the appearance of your form.
!![Default Attribute Form](../../assets/images/new-project-properties-attribute.png)
We do not need to edit the *fid* field. QGIS creates this for every Gpkg by default.

3. Remove the *fid* field from the visible fields by pressing the *red minus* on the window.
4. *Name*: Click on *Name* and look at the Widget Display options on the right-hand side.
!![Widget Display](../../assets/images/new-project-properties-attri-overview.png, 800px)
    The widget display let`s you customise the appearance of your form.
    You can keep it simple or set complex rules and constraints depending on your use case.
    Today, we will keep it simple.
    1. Here you can decide whether you want to display the name of your field inside the attribute form.
    2. If you have a technical fieldname with underscores or other special characters you can add an ***Alias*** to make it nicer for the data user.
    3. There exist several types of [widgets](how-to/attributes-form.en.md). <!-- markdown-link-check-disable-line -->
*Maya does not want to enter the date new every time.*
*What a good thing one can set default values in QGIS*
5. Open the widget display of the ***entrydate*** attribute.
    1. If not already done, change the widget type to date/time.
    You can customise the appearance of your date by changing the custom display format.
    2. To not have to add a new date every time, add a default value using the following expression ***format_date(now(),'dd MMMM yyyy')***.
    This will populate the field with the time when the data point is created.
    !![Date widget](../../assets/images/new-project-properties-attri-date.png, 800px)
6. For the field ***Visit*** you can just change the Alias name to something more readable like *"Worth the visit?"*

    *The **Category** field is a bit more interesting.*
    *Maya wants to have a dropdown list from which she can select what type of location it is.*
    *Luckily, there is a widget type called value map, where we can enter some categories.*

7. Open the widget display for the ***Category*** field and change the widget type to ***Value map***
8. Enter some relevant categories to the value map

    | Key | Description|
    | ---| ---|
    |Photo_point| Photo point |
    |Restaurant| Good Restaurant|
    |Accommodation| Hotel |
    |Attraction| Tourist Spot|
    |Nature| Nature Spot|
    | Other | Other |

    !![Value map](../../assets/images/new-project-properties-attri-valuemap.png)

9. Change the widget type of the ***Attachment*** field to ***Attachmendt***.
This will save the path of the where the image is stored.
**NOTE:** Change the path to *relative path* so that it is relative to the project folder that you are working in and not the *absolute path*.
