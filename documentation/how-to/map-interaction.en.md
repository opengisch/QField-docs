---
title: Interact with the map
tx_slug: documentation_how-to_map-interaction
---

# Interact with the map

Here are some of the possible interactions with the map in QField.

## Map legend
:material-tablet: Fieldwork

Open the *Main menu* and expend the layers list to display the legend
of the map.

On double-tap or long-press on a layer, you get offered the following possibilities.

!![](../assets/images/howto_legendoptions.png)

- *Show on map* to control visibility.
- *Show labels* to control the visibility of the labels.
- *Expand legend item* to show/hide the layer's sub-items.
- *Zoom to layer* to have all the layer items on the map.
- *Reload data* to get the current data of a layer with remote sources.
- *Show feature list* to show all the layer's features in the identification list.

## Identify features
:material-tablet: Fieldwork

Tap on a feature on the map to identify it. If several features are
located where you tapped (either because there are multiple features
really close one to another, or because several layers are overlapping),
they will all be listed in the menu that opens on the right of the
screen.

!![](../assets/images/howto_identification.png)

Tap on one of the listed features to access its attributes.

1.  Tap the *arrows* to scroll through all the identified features.
2.  Tap the *centre button* to centre the map on the selected feature.
3.  Tap the *edit button* to edit the attributes of the selected
    feature.
4.  Scroll through the *sub-menus* to access all the attributes.

!![](../assets/images/howto_featureinfo.png)

### Select identified features

With long-press, you can toggle the feature selection.

!![](../assets/images/howto_selection.png)

When features are selected, you can perform the actions in the three-dot menu on the top right.

!![](../assets/images/howto_identification_options.png)


### Exceptions to identified layers

Often it is not required to be able to query every layer. Some layers
are only present as basemap, and their attributes are not of interest.

You can manage this layer list in QGIS desktop in
*Project > Project Properties > Identify Layers* and uncheck the base layers.
