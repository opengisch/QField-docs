---
title: Standalone datasets
tx_slug: documentation_how-to_standalone-datasets
---

# Standalone datasets

QField is able to directly open vector data and raster datasets without the need for a QGIS project.

## Supported standalone dataset formats

The supported vector formats are:

- GeoPackage datasets (.gpkg);
- GeoJSON (.geojson, .json);
- KML (.kml, .kmz);
- Shapefile (.shp);
- GPS Exchange (.gpx);
- Geography Markup Language (.gml);
- MapInfo (.mif);
- SpatiaLite (.db, .sqlite); and
- FlatGeoBuf (.fgb)

The supported raster formats are:

- GeoTIFF (.tif, .tiff);
- Geospatial PDF (.pdf);
- JPEG2000 (.jp2);
- JPEG (.jpg, .jpeg);
- PNG (.png); and
- WebP (.webp)
- VRT (Virtual Raster) (.vrt)

Supported point cloud formats:

- LAS/LAZ (.las, .laz)
- COPC (Cloud Optimized Point Cloud)

!!! note
    QField can handle several standalone datasets compressed into one ZIP archive; in this scenario, each dataset will be added as individual layers in QField.

## Opening an vector or raster dataset
:material-tablet: Fieldwork

Please read the [storage access documentation](../../how-to/project-setup/storage.md) to learn more on how standalone datasets are opened on your specific device.

## Using a project as "base map" for standalone datasets
:material-tablet: Fieldwork

By default, the datasets will be overlaying an OpenStreetMap XYZ layer. It is however possible to customize that by selecting a project stored onto the device QField is running that will act as a base map.

!!! Workflow

     1. Direct to your project landing page.
     2. Press long on the project you want to have as a basemap
     !![](../../assets/images/choose_basemap.png,300px)
