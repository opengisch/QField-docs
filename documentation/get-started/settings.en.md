---
title: QField General Settings
tx_slug: documentation_get-started_settings
---

# QField General settings

The general settings screen allows you to control basic appearance and behavior of the app.

## Customize search bar

You can change what you want or not be able to search from the search bar.

- **Features from active layer**

Returns a list of features from the active layer with matching attributes.
Restricting matching to a single attribute is done by identifying its name with an `@`.

When disabled, this locator filter can still be used by typing the prefix **f** in the search bar.

Check the box "Enable **Features from active layers** locator by default".

- **Features in all layers**

Returns a list of features across all searchable layers with matching display name.

Check the box "Enable **Go to coordinate** locator by default".

- **Spatial bookmarks**

Returns a list of user and currently open project bookmarks with matching names.

Check the box "Enable **Spatial bookmarks** locator by default".

- **Calculator**

Returns a list of locations and addresses within Finland with matching terms.

When disabled, this locator filter can still be used by typing the prefix **fia** in the search bar.

Check the box "Enable **Calculator** locator by default".

- **Finnish address search**

Returns the value of an expression typed in the search bar.

Check the box "Enable **Finnish address search** locator by default".

## Show scale bar

By switching on "Show scale bar" it will show the scale bar on the map.

## Maximized attribute form

By switching on "Maximized attribute form" it will maximize the attribute form.

## Fixed scale navigation

When fixed scale navigation is active, focusing on a search result will pan to the feature.
With fixed scale navigation disabled, it will pan and zoom to feature.

## Show digitizing information

When switched on, coordinate information, such as latitude and longitude, is overlayed onto the map while digitizing new features or usting measure tool.

## Show bookmarks

When switched on, user's saved and currently opened project bookmarks will be displayed on the map.

## Use native camera

If disabled, QField will use a minimalist internal camera instead of the camera app on the device.
Tip: Enable this option and install the open camera app to create geo tagged photos.

## Fast editing mode

If enabled, the feature is stored after having a valid geometry and the constraints are fulfilled and attributes are committed immediately.

## Use volume keys to digitize

If enabled, pressing the device's volume up key will add a vertex while pressing volume down key will remove the last entered vertex during digitizing sessions.

## Consider mouse as a touchscreen device

If disabled, the mouse will act as a stylus pen.

## Send anonymized metrics

If enabled, anonymized metrics will be collected and sent to help improve QFiled for everyone.

## Dim screen when idling

Time of inactivity in seconds before the screen brightness get to be dimmed to preserve the battery. Set to 0 to disable dim screen.

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

[Translate the app](https://www.transifex.com/opengisch/qfield-for-qgis/); <!-- markdown-link-check-disable-line -->

You can also pick a different language from the drop-down menu.

## Map canvas rendering quality

You can choose from three options:

- Best quality
- Lower quality
- Lowest quality

A lower quality trades rendering precision in favor of lower memory usage and rendering time.
