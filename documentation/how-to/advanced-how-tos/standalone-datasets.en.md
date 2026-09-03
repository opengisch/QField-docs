---
title: Standalone datasets
tx_slug: documentation_how-to_standalone-datasets
---

# Standalone Datasets

QField can open vector, raster, and point cloud datasets directly without requiring a QGIS project file.

## Supported Standalone Dataset Formats

Supported vector dataset formats:

- **GeoPackage** (`.gpkg`)
- **GeoJSON** (`.geojson`, `.json`)
- **KML / KMZ** (`.kml`, `.kmz`)
- **ESRI Shapefile** (`.shp`)
- **GPS Exchange Format** (`.gpx`)
- **Geography Markup Language** (`.gml`)
- **MapInfo Interchange Format** (`.mif`)
- **SpatiaLite Database** (`.db`, `.sqlite`)
- **FlatGeobuf** (`.fgb`)

Supported raster dataset formats:

- **GeoTIFF** (`.tif`, `.tiff`)
- **Geospatial PDF** (`.pdf`)
- **JPEG 2000** (`.jp2`)
- **JPEG** (`.jpg`, `.jpeg`)
- **PNG** (`.png`)
- **WebP** (`.webp`)
- **Virtual Raster Header** (`.vrt`)

Supported point cloud dataset formats:

- **LAS / LAZ** (`.las`, `.laz`)
- **Cloud Optimized Point Cloud** (`.copc.laz`, `.copc.las`)

!!! Note
    QField opens compressed ZIP archives containing multiple standalone datasets, adding each file as an individual map layer.

## Opening Vector or Raster Datasets
:material-tablet: Fieldwork

Refer to the [Storage Access Documentation](../../how-to/project-setup/storage.md) for instructions on transferring and opening standalone files on mobile devices.

## Using a Project as a Base Map for Standalone Datasets
:material-tablet: Fieldwork

Standalone datasets display over a default OpenStreetMap XYZ tile layer.
Set any QGIS project stored on your mobile device as a custom background base map.

!!! Workflow
    1. Open QField and navigate to the project selection screen.
    2. Long-press the QGIS project file you want to use as a base map.
    3. Select **"Use as Base Map"** in the context menu.

!![](../../assets/images/choose_basemap.png,300px)
