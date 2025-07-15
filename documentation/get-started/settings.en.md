---
title: QField General Settings
tx_slug: documentation_get-started_settings
---

# QField General settings

The general settings screen allows you to control the basic appearance and behavior of QField.

## Map Canvas

### Show scale bar

By switching on "Show scale bar" it will show the scale bar on the map.

### Show bookmarks

When switched on, user's saved and currently opened project bookmarks will be displayed on the map.

### Enable map rotation

When enabled, the map can be rotated by the user.

### Map canvas rendering quality

If high memory use is an issue, the user can reduce the rendering quality and thereby lower the memory usage and the rendering time.
This comes with the cost of rendering precision.

## Digitizing & Editing

### Show digitizing information

When switched on, coordinate information, such as latitude and longitude, is overlayed onto the map while digitizing new features or usting measure tool.

### Fast editing mode

If enabled, the feature is stored after having a valid geometry and the constraints are fulfilled and attributes are committed immediately.

### Use volume keys to digitize

If enabled, pressing the device's volume up key will add a vertex while pressing volume down key will remove the last entered vertex during digitizing sessions.

### Allow finger tap on canvas to add vertices

If enabled, tapping the map canvas with a finger will add a vertex to the tapped location.

### Consider mouse as a touchscreen device

If disabled, the mouse will act as a stylus pen.

## User Interface

### Customize search bar

When pressing the three dots under the general settings section, a new window will open from which you can personalise your search options.

#### Features from active layer

By enabling this option, you will automatically query the layer that is currently active (it is highlighted in the legend).
You can refine your search even further by adding an **'@'** sign when starting your search to only query one attribute
When disabled, you can still access this locator filter typing the prefix **f** in the search bar.

#### Features in all layers

When enabling this option, you can search all features across all layers.
If the 'Features from active layer' option is enabled you can still search through all layers by adding the prefix **af** in the beginning of your search.

#### Go to coordinate

By enabling this option, you can simply copy and paste longitude and latitude values to direct to specific locations that are not part of your feature layers.
If disabled, you can still access this option by typing go at the start of your query.

!!! Tip
    When pressing long on a point of interest anywhere in your map, you can copy the point location to your clip board and directly place it in the search bar.
    Remember to type **go** in advance if the *go to coordinate* setting has not been enabled and remove the information about the coordinate reference system.

#### Spatial bookmarks

By enablig this option you automatically when using the search bar, the list of pre-configured bookmarks (if any) will be queried.
If disabled, you can still access this option by typing **b** at the front of your query.

#### Calculator

By enabling this option, you can do simple calculations and copy the results directly to the clipboard, if necessary.
If disabled, the calculator can still be accessed by typing **=** in the front of the query.

#### QField Documentation
If enabled it will return the corresponding documentation pages matching terms.
When disabled the documentation can still be queried by putting a '?' in the beginning of the query.

### Manage plugins

By pressing the three dots the plugin a new window will open from which you can add, enable and disable customised plugins.

To add a new plugin see the [Plugins Page](../how-to/plugins.md/#qfield-plugins)<!-- markdown-link-check-disable-line -->

### Maximized attribute form

By switching on "Maximized attribute form" it will maximize the attribute form.

### Fixed scale navigation

When fixed scale navigation is active, focusing on a search result will pan to the feature.
With fixed scale navigation disabled, it will pan and zoom to the feature.

### Automatically open form for single feature identification

Sometimes it can be helpful to immediately open the attribute form of an individual selected feature.
When enabling this option, when tapping on an individual feature while being in the *browse mode*, the attribute form will directly be opened.

### Dim screening when idling

To preserve the use, you can change the time when you want your phone to dim the screen when being inactive on QField.
When setting it to *0* the dimming will be disabled completely.

### Appearance
Depending on your preference, you can change the QField interface to *Light* or *Dark* Mode.

### User interface font size

You can choose from the following options:

- Tiny
- Normal
- Large
- Extra-large
### User interface language

QField will by default utilize the language present on your device, if a translation is available.
You are cordially invited to enhance the translation in your native language.

[Translate the app](https://explore.transifex.com/opengisch/qfield-for-qgis/); <!-- markdown-link-check-disable-line -->
## Advanced

### Use native camera

QField has an own internal camera, which provides quite a few options if desirable:

- Geotagging and [EXIF variables](../reference/exif.md)
- Details stamping
- Size and ration adjustment
- Camera selection - front and back


!!! Background information
    If enabled, QField will use the system specific internal camera of the device.
    Unless errors occur when using the QField specific camera, it is recommended to use the one from QField.

### Send anonymized metrics

If enabled, anonymized metrics will be collected and sent to help improve QField for everyone.
No personal account data will be sent to the QField development team.
