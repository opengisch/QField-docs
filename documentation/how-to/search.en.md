---
title: Search
tx_slug: documentation_how-to_search
---

# Search

QField allows to search in layers, into a value list and to go to coordinates with the search tool.

## Configure search in QGIS
:material-monitor: Desktop preparation

1.  Choose the layers which are searchable in
    *Project > Project Properties > Data Sources*
2.  Define the *display expression* for the concerned layers, this will
    be used for searching for features. This is configured under
    *Vector Layer Properties > Display*

## Usage
:material-tablet: Fieldwork

Tap on the *Search button* on the top-right corner of the screen to
search for features in the current project.

1.  Tap on the *name* in the result to pan the map on the feature (the
    feature will be highlighted in yellow).
2.  Tap on the *attributes button* to open its attributes.

### GoTo Coordinate

It is possible to go to coordinates with the search tool.

Tap on the *coordinates* in the result to go to the coordinates. It is
always possible to search WGS84 coordinates (*longitude, latitude*) or
current map CRS (*x,y*).

![type:video](https://player.vimeo.com/video/499566922)

### Search in value relation and relation reference widget

It is possible to search value in a *value relation* or *relation reference* widget using the magnifying
glass next to the field.

![type:video](https://player.vimeo.com/video/604661919)

#### Autocompleter
In the *value relation* widget you even can use the "completer" functionality. You have to activate it in the widget settings.

### Search in layers

You can search for features in vector layers. The search is currently
performing the same as the *all layers locator filter* in QGIS
(accessible in QGIS locator bar using `af` prefix).
