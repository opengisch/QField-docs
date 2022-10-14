---
title: Standalone datasets
tx_slug: documentation_how-to_standalone-datasets
---

# Standalone datasets

QField is able to directly open vector data and raster datasets without the need for a QGIS project.

## Supported standalone dataset formats

The supported vector formats are:

- Geopackage datasets (.gpkg);
- GeoJSON (.geojson, .json);
- KML (.kml, .kmz);
- Shapefile (.shp);
- GPS Exchange (.gpx);
- Geography Markup Language (.gml);
- MapInfo (.mif);
- Spatialite (.db, .sqlite); and
- FlatGeoBuf (.fgb)

The supported raster formats are:

- GeoTIFF (.tif, .tiff);
- Georeferenced PDF / GeoPDF (.pdf);
- JPEG2000 (.jp2);
- JPEG (.jpg, .jpeg);
- PNG (.png); and
- WebP (.webp)

!!! note
    QField can handle several standalone datasets compressed into one ZIP archive; in this scenario, each dataset will be added as individual layers in QField.

## Opening an vector or raster dataset

:material-tablet: Fieldwork

Please read the [storage access documentation](/get-started/storage/) to learn more on how standalone datasets are opened on your specific device.

## Using a project as "base map" for standalone datasets

:material-tablet: Fieldwork

By default, the datasets will be overlaying an OpenStreetMap XYZ layer. It is however possible to customize that by selecting a project stored onto the device QField is running that will act as a base map.

To use an existing project as base map, do a long press on a project in the recent projects list and check *Base Map Project*.

![type:video](https://player.vimeo.com/video/604849182)
