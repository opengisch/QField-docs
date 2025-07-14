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

## Fixed scale navigation

When fixed scale navigation is active, focusing on a search result will pan to the feature.
With fixed scale navigation disabled, it will pan and zoom to feature.

## Use native camera

If disabled, QField will use a minimalist internal camera instead of the camera app on the device.
Tip: Disable this option to have geo tagged photos and have access to the [EXIF](../reference/exif.md) variables.

## Send anonymized metrics

If enabled, anonymized metrics will be collected and sent to help improve QField for everyone.

## Dim screen when idling

Time of inactivity in seconds before the screen brightness get to be dimmed to preserve the battery.
Set to 0 to disable dim screen.

## User interface appearance

You can choose from three options:

- Follow system appearance
- Light theme
- Dark theme

## User interface font size

You can choose from the following options:

- Tiny
- Normal
- Large
- Extra-large

## User interface language

QField will by default utilize the language present on your device, if a translation is available.
You are cordially invited to enhance the translation in your native language.

[Translate the app](https://explore.transifex.com/opengisch/qfield-for-qgis/); <!-- markdown-link-check-disable-line -->

You can also pick a different language from the drop-down menu.

## Map canvas rendering quality

You can choose from three options:

- Best quality
- Lower quality
- Lowest quality

A lower quality trades rendering precision in favor of lower memory usage and rendering time.
