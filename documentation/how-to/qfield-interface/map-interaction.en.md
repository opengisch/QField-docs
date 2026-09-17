---
title: Interact with the map
tx_slug: documentation_how-to_map-interaction
---

# Interact with the map

There is a lot you can do inside QField.
There exists a number of buttons, icons and settings, which may or may not be relevant for your used case.

## Sort layer features

If you'd like to configure the order of features in "Show feature list" in QField, you have the following options to pre-configure this on QGIS:

!!! Workflow

    1. Right-click on any part of a column header and select **Sort** option from the menu.
    2. Enter your desired way of sorting.
    !![](../../assets/images/accesing-sort-feature-list-op1.png)
    3. When being in the form view, you can access the sorting functionality by clicking on the expression button located at the top of the features list and select **Sort**.
    !![](../../assets/images/accesing-sort-feature-list-op2.png)

## Map styling

All style settings from QGIS are directly supported by QField.
This includes all renderer types like graduated, categorized, rule based, 2.5D as well as data defined symbology.

### Display Expression

In QField, objects are identified with a name, which can be customized using expressions.

!!! Workflow

    1. Open the attribute table in QGIS and switch to the form view.
    2. Direct to *Vector Layer Properties* > *Display* > *Attribute*.
    **Note:** The display expression is also used to search in layers.
    !![Configuration of display expression in QGIS.](../../assets/images/define_display_expression.png)

### Read only, non-identifiable and searchable layers

Some layers in a project are just there for pure visual purpose.
Such layers should not show up when a user taps somewhere to identify objects.

Some other layers serve as source of information and shouldn't be modified by the user.
It is possible to protect layers from editing attributes or adding and deleting features.

It is also possible to configure which layers are searchable.

!!! Workflow

    1. Direct to *Project* > *Properties...* > *Data Sources* and activate the checkboxes to match your desired behaviour.
    !![Configuration of layers that will not be identifiable, nor modifiable,  nor searchable.](../../assets/images/project_configuration_readonly.png)

#### Adding additional fonts

QField can adopt all the custom fonts you might want and need.
There are two different possibilities to register additional fonts:

!!! Workflow

    **Addition of fonts through the local directory**

    1. Copy your font file (.ttf or .otf) in the directory **[[App Directory]](../../how-to/project-setup/storage.md#5-qfield-app-directory)/QField/fonts**.Those will be made accessible to all projects and individual datasets.

    **Addition of fonts in subfolder of QGIS file**

    1. Create a subfolder called **fonts** inside the same folder where your given project file (`.qgs` or `.qgz`) is stored. Those fonts will **only** be accessible when viewing that project.

#### Adding subfolder for QFieldCloud Projects

When building a QFieldCloud project that includes additional fonts in a `fonts` subfolder, you must add this directory to the synchronized folders list in your project settings.
This ensures the custom font files are successfully pushed to QFieldCloud and transferred onto mobile devices.

!!! Workflow

    1. Navigate to *Project* > *Properties...* > *QField*.
    2. Under the *Attachments and Directories* configuration tab, add the path to your relative `fonts` subfolder to the directories list as "Data" type.
    !![Configuring custom fonts folder for QFieldCloud synchronization.](../../assets/images/qfc_fonts_directory_setting.png)

### Custom SVG symbols

It is possible to embed SVG symbols directly within a QGIS project.

!!! Workflow

    1. Choose the layer which will support SVG symbology and open its properties dialog.
    2. Open the section Symbology in *Properties* > *Symbology*
    3. In the **Symbol Layer Panel** choose **Simple marker**.
    !![](../../assets/images/symbol_layer_panel.png)
    4. Change the symbol layer type in *Symbol layer type* > *SVG marker*.
    5. Scroll down to the bottom panel.
    6. Click on the right side of the file selection button to open the drop down menu.
    !![](../../assets/images/drop_down_svg_menu.png)
    7. Select **Embed File** and choose the SVG file in the file selection dialog.
    8. Apply the changes and click **OK**.
    !![Embedded custom SVG on QField](../../assets/images/custom_svg_symbols_qfield.png,350px)

## Map themes

The beautiful thing about GIS is that maps are dynamic.
Layers can individually be shown and hidden and information can be presented more or less prominently based on the task at hand.

This is what **Map themes** are for.

### Creating a Map Theme
Creating a Map Theme in QGIS is a very simple task.

!!! Workflow

    1. Style the map and layers to your requirements.
    2. Save it as a named Map Theme.
    3. Load the project on your device and change the active Map Theme.
    ![type:video](../../assets/videos/map_themes_configuration.webm)

See how this looks in QField: [Here](../../fieldwork/qfield-interface/map-interaction.md#map-themes)

## Search bar

QField is equipped with a search bar that allows you to:

- search for features within a project's vector layers
- [navigate to specified coordinates](../navigation-and-positioning/navigation.md#setting-a-destination-point)
- locate spatial bookmarks
- and calculate expressions

See [here](../../fieldwork/qfield-interface/search.md) how to use the search bar in QField

### Configure vector layers search in QGIS
:material-monitor: Desktop preparation

By default, all vector layers are searchable. To exclude specific layers from search queries:

!!! Workflow

    1. Open your project in QGIS.
    2. Navigate to _Project > Properties... > Data Sources_.
    !![Data Sources](../../assets/images/hiding-legend-nodes.png)
    3. Locate the layer capabilities table and uncheck the **Searchable** checkbox for any layers you wish to exclude.
    [Source configuration](../project-setup/data_source_and_project_paths.md#data-source-configuration)

## Measuring Units

In QGIS you can set the units for your QGIS project by navigating to the *Project* > *Properties* > *General* section.
!![](../../assets/images/custom-units-measure.png)


## Project Bookmarks in QGIS
:material-desktop: Desktop preparation

!!! Workflow

    1. Open your project in QGIS and navigate to your target area.
    2. Add a spatial bookmark using **Ctrl + B**, or via *View > New Spatial Bookmark*.
    3. Define the name, group, and optional map extent/rotation in [QGIS Spatial Bookmarks Manager](https://docs.qgis.org/latest/en/docs/user_manual/introduction/browser.html#spatial-bookmarks). <!-- markdown-link-check-disable-line -->
    4. Save and synchronize the project to QField.
    !![Spatial Bookmark QGIS](../../assets/images/bookmarks-qgis.png,600px)

How to work with Bookmarks in QField, click [here](../../fieldwork/qfield-interface/bookmarks.md)
