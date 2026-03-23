---
title: 3D Terrain View
tx_slug: documentation_how-to_3d-terrain-view
---

# 3D Terrain View

QField allows you to view and interact with your spatial data in 3D.
By utilizing elevation data, 2D map layers are draped as textures over the 3D surface, providing enhanced spatial context for navigation and field editing.

## Configuring the Terrain

There are two ways QField handles 3D elevation data:

- Using a custom Digital Elevation Model (DEM) from your QGIS project
- A default online DEM.

### Option 1: Custom DEM (Recommended)
:material-monitor: Desktop preparation

For offline fieldwork and the highest accuracy,
you should configure your own elevation data directly within the [QGIS project](https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#elevation-properties).

!!! Workflow
    1. Open your project in QGIS.
    2. From the main menu, select Project > Properties
    3. In the Project Properties dialog box, select the Terrain tab.
    4. Here, you can select your Terrain type:

        1. Flat terrain (default): Assumes an elevation of 0m for all layers.
        2. DEM (Raster Layer): Allows you to select an existing raster layer (like a GeoTIFF) in your project to serve as the elevation source for the entire project.
        3. Mesh layer: Uses an irregular mesh (TIN, for example) as the elevation source.

### Option 2: Online Fallback DEM
:material-tablet: Fieldwork

If no custom elevation data is configured in your QGIS project, QField will automatically attempt to use a global online DEM to generate the 3D view on the fly.

!!! note

    **Important Constraints for the Online DEM:**

      - **CRS Requirement:** For this automatic fallback to function correctly, your QGIS project's Coordinate Reference System (CRS) **must** be set to **Pseudo-Mercator (EPSG:3857)**.
      - **Connectivity:** Your mobile device must have an active internet connection while in the field to load the terrain tiles.

## Navigating the 3D View
:material-tablet: Fieldwork

QField allows for interactive extent manipulation when viewing data in the 3D view.
You can actively pan and zoom directly within the 3D mode rather than relying on a static, locked extent.

Depending on your device, you can interact with the 3D extent in the following ways:

**Touch Interactions:**

- **Extent Mode Toggle:** Once you have enabled the 3D mode, it will only give you the extent in 3D that your original map extent was on.
This can be changed when you tap the *4-arrowed* toggle button to change the map extent.
Once it is activated, you can pan the terrain extent by dragging your fingers, or zooming in and out by pinching your fingers.

**Mouse Interactions:**

- **Pan Extent:** Hold the `Shift` key and drag the mouse to move the 3D terrain extent geographically.
    The terrain mesh translates in real-time for visual feedback.
- **Zoom Extent:** Hold the `Shift` key and use the mouse scroll wheel to scale the terrain extent in or out around its center point.

## Digitizing in 3D
:material-tablet: Fieldwork

When editing layers, you can view your active edits directly within the 3D terrain view.
The digitizing "rubberbands" (the temporary lines and vertices you draw while creating or modifying a feature) are dynamically rendered in 3D.

These visual guides conform to the terrain's elevation and respect any height offsets applied to the layer,
ensuring you have accurate spatial context while digitizing in a 3D environment.

## 2D and 3D Extent Synchronization

When you close the 3D view to return to the 2D map canvas, QField automatically updates the 2D map's bounding box to match your newly navigated 3D extent.
This ensures your view remains perfectly synchronized between modes.

![type:video](../../assets/videos//3D_Map_View.mp4)
