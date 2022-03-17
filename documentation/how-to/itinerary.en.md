---
title: Advanced itinerary
---

# Advanced Itinerary

This feature is used to inspect a list of objects that match a certain
criteria. You may then navigate through these features with arrows and
verify their status or adjust attributes as required.


## Configure An Itinerary
:material-desktop-mac:{ .device-icon } Desktop preparation

To define an itinerary to review you will need to use the python console
for the moment. You can use any `QgsExpression` to define the review list.
Select the desired layer in the legend and use the following python code
to add the itinerary to the QGIS project.

``` python
l=iface.activeLayer()
l.setCustomProperty('qgisMobile/itinerary', 'status <> 1')
```
