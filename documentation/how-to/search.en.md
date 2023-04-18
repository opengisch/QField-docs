---
title: Search bar
tx_slug: documentation_how-to_search
---

# Search bar

QField is equipped with a nifty search bar which allows you to search for
features within project's vector layers, to go to entered coordinates and more.

## Usage
:material-tablet: Fieldwork

Tap on the *Search button* in the top-right corner of the screen to
open expand the search bar.

### Vector layers search

The value entered in the search bar will be used to find features with
matching attribute values. A minimum of three characters is required to
start the search.

!![image](../assets/images/search-bar.png)

Matching features will show in the results list offering you two possible
actions :

1.  Tap on the *name* in the result to pan the map on the feature (the
    feature will be highlighted in yellow).
2.  Tap on the *attributes button* to open its attributes.

### Go to coordinate

It is possible to go to a given coordinates through the search bar by entering
*latitude, longitude* coordinates (in WGS84). You will also be able to enter
coordinates in the CRS of the opened project.

Once QField identifies the entered value as a coordinate, tap on the *coordinates*
in the result to move the map canvas to that point.

### Go to spatial bookmark

The search bar also matches saved spatial bookmarks. The entered text will be
matched against user-saved bookmarks as well as embedded bookmarks with the
currently opened project.

The matching bookmarks will appear in the results list. Tapping on one bookmark
will re-center the map canvas to match the bookmark's extent.

### Expression calculator

QField's search bar also acts as a nifty calculator, whereas entered text can be
treated as expressions, with their returned value shown in the result list
with the possibility of copying the value to the clipboard.

To trigger the calculator, a *= * (i.e. equal sign followed by a space) prefix is
needed. For example, *= 20 + 5* would return a value of 25.

Pro-tip: use the aggregate() expression function to calculate statistics against
vector layers. For example, calculating the total area covered by a polygon layers
can be done by typing *= aggregate('my_layer','sum', $area)*.

## Configure vector layers search in QGIS
:material-monitor: Desktop preparation

By default, all vector layers are searchable. When configuring your project in QGIS,
it is possible to exclude vector layers from search results. To do so, open the
project properties dialog and switch to the *Data Sources* panel, where you will
be presented with a layers capabilities table widget. From there, use the *Searchable*
checkbox to include/exclude specific layers.
