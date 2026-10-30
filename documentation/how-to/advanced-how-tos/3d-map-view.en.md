---
title: 3D Map view
tx_slug: documentation_how-to_3d-map-view
---

# 3D Map View

QField displays spatial data in 3D by draping map layers as textures over terrain surfaces.
The 3D view uses Eye Dome Lighting (depth shading) to enhance visual perception of terrain features, ridges, and valleys.

## Configuring Elevation Data

QField processes 3D elevation data using two methods:

- **Online DEM:** Default elevation service fetched automatically over mobile networks.
- **Custom DEM:** Offline Digital Elevation Model raster dataset configured within your QGIS project.

### Option 1: Online DEM
:material-tablet: Fieldwork

If no custom elevation data is configured in your QGIS project, QField attempts to fetch a global online DEM to generate 3D terrain on the fly.

!!! note

    **Important Constraints for the Online DEM:**

      - **CRS Requirement:** For this automatic online DEM to function correctly, your QGIS project's Coordinate Reference System (CRS) **must** be set to a non-degree projection (for example, Pseudo-Mercator EPSG:3857, or UTM projections).
      - **Connectivity:** Te mobile device must have an active internet connection while in the field to load the terrain tiles.

### Option 2: Custom DEM

Configure custom elevation data directly in QGIS for offline fieldwork and high-accuracy terrain rendering.
Read more in the [QGIS Elevation Properties Documentation](https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#elevation-properties). <!-- markdown-link-check-disable-line -->

!!! Workflow
    1. Open your project in QGIS.
    2. From the main menu, select _Project > Properties >Terrain_
    3. Select your **Terrain type**:
        1. Flat terrain (default): Assumes an elevation of 0m for all layers.
        2. DEM (Raster Layer): Allows you to select an existing raster layer (like a GeoTIFF) in your project to serve as the elevation source for the entire project.

See [here](../../fieldwork/qfield-interface/3d-map-view.md) how 3D looks in QField.
