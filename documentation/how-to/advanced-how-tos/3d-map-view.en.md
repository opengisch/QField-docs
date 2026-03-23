---
title: 3D Map View
tx_slug: documentation_how-to_3d-map-view
---

# 3D Map View

QField allows you to view your spatial data in 3D.
By utilizing elevation data, map layers are draped as textures over the 3D surface, providing enhanced spatial context for navigation.

## Configuring Elevation Data

There are two ways QField handles 3D elevation data, ranging from an automatic online layer to a fully offline custom model:

- A default online DEM (injected automatically by QField)
- A custom Digital Elevation Model (DEM) bundled with your QGIS project

### Option 1: Online DEM
:material-tablet: Fieldwork

If no custom elevation data is configured in your QGIS project, QField will automatically attempt to use a global online DEM to generate the 3D view on the fly.

!!! note

    **Important Constraints for the Online DEM:**

      - **CRS Requirement:** For this automatic online DEM to function correctly, your QGIS project's Coordinate Reference System (CRS) **must** be set to a non-degree projection (for example, Pseudo-Mercator EPSG:3857, or UTM projections).
      - **Connectivity:** Your mobile device must have an active internet connection while in the field to load the terrain tiles.

### Option 2: Custom DEM
:material-monitor: Desktop preparation

For offline fieldwork and the highest accuracy,
you should configure your own elevation data directly within the [QGIS project](https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#elevation-properties).<!-- markdown-link-check-disable-line -->

!!! Workflow
    1. Open your project in QGIS.
    2. From the main menu, select Project > Properties
    3. In the Project Properties dialog box, select the Terrain tab.
    4. Here, you can select your Terrain type:
        1. Flat terrain (default): Assumes an elevation of 0m for all layers.
        2. DEM (Raster Layer): Allows you to select an existing raster layer (like a GeoTIFF) in your project to serve as the elevation source for the entire project.

## Navigating the 3D View
:material-tablet: Fieldwork

QField allows for interactive extent manipulation when viewing data in the 3D view.
You can actively pan and zoom directly within the 3D mode rather than relying on a static, locked extent.

Depending on your device, you can interact with the 3D extent in the following ways:

**Touch Interactions:**

- **Extent Mode Toggle:** Once you have enabled the 3D mode, it will originally give you the 3D extent that your 2D map extent was on.
This can be changed when you tap the *4-arrowed* toggle button to change the map extent.
Once it is activated, you can pan the map extent by dragging your fingers, or zooming in and out by pinching your fingers.

**Mouse Interactions:**

- **Pan Extent:** Hold the `Shift` key and drag the mouse to move the 3D map extent geographically.
    The 3D mesh translates in real-time for visual feedback.
- **Zoom Extent:** Hold the `Shift` key and use the mouse scroll wheel to scale the map extent in or out around its center point.

## 2D and 3D Extent Synchronization

When you close the 3D view to return to the 2D map canvas, QField automatically updates the 2D map's bounding box to match your newly navigated 3D extent.
This ensures your view remains perfectly synchronized between modes.

![type:video](../../assets/videos/3D_Map_View.mp4)
