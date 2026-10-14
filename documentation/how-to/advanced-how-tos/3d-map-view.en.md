---
title: 3D Map view
tx_slug: documentation_how-to_3d-map-view
---

# 3D Map View

QField allows you to view your spatial data in 3D.
By utilizing elevation data, map layers are draped as textures over the 3D surface, providing enhanced spatial context for navigation.
The 3D view also utilizes Eye Dome Lighting (depth shading) to enhance the visual perception of ridges, valleys, and terrain features.

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
      - **Connectivity:** Te mobile device must have an active internet connection while in the field to load the terrain tiles.

### Option 2: Custom DEM

For offline fieldwork and the highest accuracy,
you should configure your own elevation data directly within the [QGIS project](https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#elevation-properties).<!-- markdown-link-check-disable-line -->

!!! Workflow
    1. Open your project in QGIS.
    2. From the main menu, select _Project > Properties >Terrain_
    3. Select your **Terrain type**:
        1. Flat terrain (default): Assumes an elevation of 0m for all layers.
        2. DEM (Raster Layer): Allows you to select an existing raster layer (like a GeoTIFF) in your project to serve as the elevation source for the entire project.

See [here](../../fieldwork/qfield-interface/3d-map-view.md) how 3D looks in QField.
