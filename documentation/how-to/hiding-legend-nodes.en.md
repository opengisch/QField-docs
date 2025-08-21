---
title: Hiding legend nodes
tx_slug: documentation_how-to_hiding-legend-nodes
---

# Configure Data Sources
:material-monitor: Desktop preparation

It is possible to configure your QGIS projet to allow hiding legend nodes or information.

In the [**Data Sources**](https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#data-sources-properties) tab of a QGIS project properties,
you can set "Layer Capabilities" for each layer.
These settings primarily control how layers behave in the project.

## Identifiable

An **Identifiable** layer allows users to retrieve attribute information from its features.

When you use the "Identify Features" in a QGIS project, you can click on an object from this layer and see its data.
If this box is unchecked, the layer is visible on the map, but cannot tap on its features or query or search by their information.

- **Use it for:** Layers where users need to see details, like clicking on a parcel to see owner information.
- **Disable it for:** Basemap or background layers where individual feature data is irrelevant.

## Read-Only

A **Read-Only** layer cannot be edited.

This is a security feature to prevent accidental or unauthorized changes to a layer's data.
You can view and query the layer, but the features can't be modify, add, or delete its features.

- **Use it for:** Authoritative data that should not be altered, such as administrative boundaries, official infrastructure, or a satellite imagery basemap.

## Searchable

A layer marked as **Searchable** makes its attributes available for search queries or expressions.

For example, a user could search for a specific address or parcel ID, and the QField would look for matches within all layers marked as "Searchable".

- **Use it for:** Layers containing data that users are likely to search for, like addresses, city names, or points of interest.

## Required

A **Required** layer is always visible and cannot be turned off by an user in the map canvas.

This ensures that essential contextual information is always displayed in the map, the aye checkbox for this layer will be greyed out in the layer list, forcing it to remain on.

- **Use it for:** Essential layers like a basemap, legal boundaries, or points watermark that must always be part of the map canvas.

## Private

A **Private** layer is hidden from the project's legend or layer tree.

The layer is still drawn on the map, but it won't appear in the list of available layers for the user to toggle on or off. This is perfect for cleaning up a cluttered legend or hiding technical layers that the a user doesn't need to interact with directly.

- **Use it for:** Hiding the individual layers that make up a complex base map group or for layers used only for styling or labeling purposes.

!![Configuring Layers Data Sources](../assets/images/hiding-legend-nodes.png)
