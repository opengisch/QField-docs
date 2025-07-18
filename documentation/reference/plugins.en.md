---
title: Plugins
tx_slug: documentation_reference_plugins
---

# QField Plugins Technical Details

This page is a collection of QField plugin framework APIs and behaviors to guide you into writing your own plugins.

To see what's possible and get inspiration from the community, you can browse a list of all available plugins on the [QField Plugin Topic on GitHub](https://github.com/topics/qfield-plugin).

## Hello QField World

Scripting QField plugins require basic knowledge of QML and Javascript.
Qt offers a useful [introductory tutorial](https://doc.qt.io/qt-6/qml-tutorial.html) worth reading.

Once you’ve familiarized yourself with the QML environment, you are set to go.
This is a minimal example that will display a toast message upon successfully loading a QField plugin:

```
import QtQuick
import org.qfield

Item {
  Component.onCompleted: {
    iface.mainWindow().displayToast('Hello world!')
  }
}
```

## Creating a zipped plugin

A valid zipped plugin must contain a main.qml file at the root of the zip archive, which will be used by QField to activate the plugin.
An optional metadata.txt can also be used to provide basic details such as the plugin name, brief description, and author name.
A sample typical `metadata.txt` content would look like this:

```
[general]
name=Hello World Plugin
description=This is simple and brief description.
author=OPENGIS.ch
icon=logo.svg
```

This [QField template plugin](https://github.com/opengisch/qfield-template-plugin) offers a simple skeleton from which you can build plugins from scratch.

## `iface` interface

Much like QGIS plugins, QField offers an `iface` object exposing a number of functionalities plugins can leverage.
The current invokable functions include:

- `iface.mainWindow()`: returns the QML ApplicationWindow instance, where plugins can parent their items via `iface.mainWindow().contentItem` and have access to functionality such as displaying toast messages using `iface.mainWindow().displayToast(text)`.
- `iface.mapCanvas()`: returns the map canvas item, which exposes crucial properties including `iface.mapCanvas().mapSettings` from which the extent, scale, etc. can be retrieved and modified.
- `iface.findItemByObjectName(string)`: returns a item living within the QField application window matching the object name `string`, such as `iface.findItemByObjectName("positionSource")` to reach the positioning item which controls the GNSS device and returns position details.
Additional items' object name strings can be found by viewing the [application window QML code](https://github.com/opengisch/QField/blob/master/src/qml/qgismobileapp.qml).
- `iface.addItemToPluginsToolbar(item)`, `iface.addItemToDashboardActionsToolbar(item)`, `iface.addItemToCanvasActionsToolbar(item)`: adds a given `item` in predefined containers within the QField application window.
Using these functions insure that items added by multiple plugins will happily co-exist.

## Utilities objects

QField ships with a number of utilities objects to manipulate features and geometries, access map layers, read and write project and map layer variables, and much more.

To familiarize yourself with these, visit QField’s source code’s [utilities directory](https://github.com/opengisch/QField/tree/master/src/core/utils) where .h\[eader\] files will provide documentation for all invokable functions.

## Plugin code snippets

### Search bar integration

The plugin framework empowers you to integrate custom searches into the QField search bar through the `QFieldLocatorFilter` item which can be added into a plugin's root item:

```
QFieldLocatorFilter {
  id: locatorFilter

  delay: 1000
  name: "unique_filter_string"
  displayName: "Plugin filter"
  prefix: "plug"
  locatorBridge: iface.findItemByObjectName('locatorBridge')

  parameters: { "parameter_1": "value_1" }
  source: Qt.resolvedUrl('search.qml')

  function triggerResult(result) {
    // result is a QgsLocatorResult object with the following properties:
    // - description, displayString, group, groupScore, score, and userData
  }

  function triggerResultFromAction(result, actionId) {
    // additional actions handled here
  }
}
```

The source property refers to a QML source file which will hold the logic to execute searches and pass on results.
It will be executed off the main thread to allow for non-blocking result fetching operations.

Here's a simple search QML source code:

```
import QtQuick
import org.qfield

Item {
  signal prepareResult(var details)
  signal fetchResultsEnded()

  function fetchResults(string, context, parameters) {
    // string is the search term(s) typed into the search bar
    // context is a QgsLocatorContext object with the following properties:
    // - targetExtent, targetExtentCrs, and transformContext
    // parameters is a map of keys and values attached to the QFieldLocatorFilter parameters properties

    // sample details object
    let result_details = {
      "userData": { "key": "value" },
      "displayString": "display string",
      "description": "description",
      "score": 1,
      "group": "group name",
      "groupScore":1,
      "actions":[{"id": 2, "name": "action", "icon": "icon.svg"}]
    }

    // prepareResult is the signal needed to pass on a result
    // you can trigger the signal as many times as you need to pass on all available results
    prepareResult(result_details);
  }
}
```

This [QField OpenStreetMap Nomination plugin](https://github.com/opengisch/qfield-nominatim-locator) is a good example to learn more about search bar integration.

### Configuration button within the plugin manager

For plugins requiring user configuration, QField allows for these to add a configuration button within its plugin manager.

To do so, you can simply add a `function configure()` invokable function attached to the plugin's root item:

```
import QtQuick
import org.qfield

Item {
  // ...

  function configure()
  {
    optionDialog.open();
  }

  Dialog {
    id: optionDialog
    parent: iface.mainWindow().contentItem
    visible: false
    modal: true
    title: "Configuration"

    // ...
  }
}
```

### Geometry highlighter canvas overlay

Plugins can make use of QField's geometry highlighter item to flash created or fetched geometries through the following code:

```
import QtQuick
import org.qfield

Item {
  // ...

  property var geometryHighlighter: iface.findItemByObjectName('geometryHighlighter')

  function demo() {
    // Flash Null Island geometry
    let geom = GeometryUtils.createGeometryFromWkt("POINT(0 0)")
    let crs = CoordinateReferenceSystemUtils.fromDescription("EPSG:4326")

    geometryHighlighter.geometryWrapper.qgsGeometry = geometry
    geometryHighlighter.geometryWrapper.crs = crs;
  }
}
```
