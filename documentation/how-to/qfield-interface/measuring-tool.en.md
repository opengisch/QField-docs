---
title: Measuring tool
tx_slug: documentation_how-to_measuring-tool
---

# Measuring Tool

QField offers built-in measurement tools with customizable distance and area units.
Customize measurement units in QGIS when preparing projects.

!!! Workflow
    :material-monitor: Desktop preparation

    1. In QGIS, navigate to _Project > Properties... > General_.
    2. Configure distance and area units under the **"Measurements"** section.

!![](../../assets/images/custom-units-measure.png)

Enable the measuring tool in QField using the **Side Dashboard**.

!!! Workflow
    :material-tablet: Fieldwork

    1. Open the **Side Dashboard**.
    2. Tap the ruler icon in the main menu bar.

!![](../../assets/images/measuring_tool.png)

Once enabled, use the digitizing controls in the bottom-right corner of the screen to add and remove vertices.
By default, QField measures line geometries.
To measure polygon areas, connect the coordinate cursor back to the first entered vertex.

For the segment formed by the last two vertices, QField displays segment length and azimuth.
For line geometries, QField displays total line length.
For polygon geometries, QField displays total perimeter and area.

## Elevation Profiling

When the measuring tool is enabled, an **"Elevation Profile"** button appears in the top-left corner of the screen.
Toggling this button opens the elevation profile panel, displaying terrain elevation and intersecting vector features along the measured geometry.

!![](../../assets/images/elevation_profiling.png)

By default, QField uses the Mapzen Global Terrain dataset to provide worldwide 30-meter resolution elevation profiles.
Customize terrain settings in QGIS through project and individual map layer properties.
