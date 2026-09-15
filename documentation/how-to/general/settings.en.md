---
title: QField general settings
tx_slug: documentation_get-started_settings
---

# QField General Settings

The general settings screen allows you to control the basic appearance and behavior of QField.
You can access the general settings in two ways.

!!! Workflow
    **Access settings from the Welcome Screen:**

    1. Open QField and tap the settings button on the top-left corner of the screen.

    **Access settings inside an active project:**

    1. Open the **Side Dashboard**.
    2. Tap the three-dotted menu *(⋮)* and select **"Settings"**.

The following sections describe available configuration options.

## Map Canvas

- **"Show scale bar":** Displays the scale bar on the map canvas.
- **"Show zoom controls":** Displays zoom buttons (**"+"** / **"-"**) on the map canvas.
- **"Show bookmarks":** Displays locally created bookmarks and project-embedded bookmarks on the map canvas.
- **"Enable map rotation":** Allows you to rotate the map canvas.
- **"Map canvas rendering quality":** Controls rendering resolution to balance memory usage and performance.
Lowering quality reduces memory usage and speeds up rendering at the cost of rendering precision.

## Digitizing & Editing

- **"Show digitizing information":** Displays coordinate details (such as latitude and longitude) beneath the crosshair while digitizing features or using the measuring tool.
- **"Fast editing mode":** Automatically saves feature edits immediately upon modification.
- **"Use volume keys to digitize":** Uses device volume buttons during digitizing sessions.
Pressing **Volume Up** adds a vertex, while pressing **Volume Down** removes the last entered vertex.
- **"Allow finger tap on canvas to add vertices":** Moves the coordinate cursor directly to the tapped location on the map canvas.
This option is useful when mapping features at a larger scale.
- **"Consider mouse as a touchscreen device":** Allows adding new vertices anywhere on the map using mouse clicks.
When disabled, the crosshair remains fixed to the map center while mouse movement shifts the map canvas.

## User Interface

- **"Customize search bar":** Opens search filter settings when tapping the three-dotted menu *(⋮)*.
    - **"Features from active layer":** Queries the currently active layer highlighted in the legend.
    Refine active layer queries by prefixing searches with `@` to search a specific attribute field.
    When disabled, access this filter by typing `f ` in the search bar.
    - **"Features in all layers":** Searches features across all project vector layers.
    When **"Features from active layer"** is enabled, search all layers by prefixing queries with `af `.
    - **"Go to coordinate":** Navigates to coordinates by pasting longitude and latitude values.
    When disabled, access coordinate navigation by typing `go ` at the beginning of a query.

    !!! Tip
        Long-press a point of interest on the map canvas to copy its coordinates to the clipboard, then paste the coordinates into the search bar.
        If **"Go to coordinate"** is disabled, type `go ` before the coordinates and remove coordinate reference system text.

    - **"Spatial bookmarks":** Searches pre-configured spatial bookmarks when using the search bar.
    When disabled, access spatial bookmarks by typing `b ` before a query.
    - **"Calculator":** Evaluates simple arithmetic expressions directly in the search bar and allows copying results to the clipboard.
    When disabled, access the calculator by typing `= ` before an expression.
    - **"QField Documentation":** Searches QField documentation pages matching search terms.
    When disabled, search documentation by typing `? ` before a query.
- **"Manage plugins":** Opens the plugin management screen when tapping the three-dotted menu *(⋮)* to add, enable, or disable custom plugins.
Refer to the [Plugins Page](../../how-to/advanced-how-tos/plugins.md#project-plugins) to add new plugins.
- **"Maximized attribute form":** Expands attribute forms to cover the full screen.
- **"Fixed scale navigation":**
    - **"Active fixed scale navigation":** Pans and highlights selected search results while maintaining the current map scale.
    - **"Disabled fixed scale navigation":** Pans, highlights, and zooms to selected search results.
- **"Automatically open form for single feature identification":** Automatically opens attribute forms when tapping an individual feature in browse mode.
- **"Dim screening when idling":** Sets the inactivity timer before the device screen dims to preserve battery power.
Set the value to `0` to disable screen dimming completely.
- **"Appearance":** Toggles the QField interface theme between **"Light"** and **"Dark"** mode.
- **"User interface font size":** Adjusts interface text sizes using the following options:
    - **"Tiny"**
    - **"Normal"**
    - **"Large"**
    - **"Extra-large"**
- **"User interface language":** Uses the default language configured on your device when a translation is available.
Help translate QField into your native language on the [Transifex Translation Platform](https://explore.transifex.com/opengisch/qfield-for-qgis/). <!-- markdown-link-check-disable-line -->

## Advanced

- **"Use native camera":** Toggles between device native camera applications and the integrated QField camera.
The QField internal camera provides the following integrated capabilities:
    - Geotagging and [EXIF Metadata](../../reference/exif.md)
    - Real-time image stamping
    - Aspect ratio and resolution adjustments
    - Camera selection (front and rear lenses)

!!! Note
    When **"Use native camera"** is enabled, QField delegates photo capture to the device default camera application.
    We recommend using the integrated QField camera unless hardware compatibility issues occur.

- **"Send anonymized metrics":** Collects and transmits anonymized usage metrics to help improve QField.
QField never transmits personal account details or project data.
