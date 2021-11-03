---
title: Supported Data Formats
---

QField supports a wide variety of formats via QGIS data providers and
GDAL. This page offers a non-exhaustive list of supported data formats.

| Data Format | Support          | Notes                    |
|-------------|------------------|--------------------------|
| Spatialite  | :material-check: |                          |
| Geopackage  | :material-check: |                          |
| WMS         | :material-check: |                          |
| WFS         | :material-check: |                          |
| WFS-T       | :material-check: |                          |
| Postgis     | :material-check: |                          |
| MBTiles     | :material-check: |                          |
| Shapefile   | :material-check: |                          |
| Tiff        | :material-check: |                          |
| JPEG2000    | :material-check: |                          |
| WEBP        | :material-check: |                          |
| ECW         | :material-close: | License restricts usage. |
| MrSID       | :material-close: | License restricts usage. |

If you don't find your favorite data format on this table, please check
if it works and [adapt the list above](https://github.com/opengisch/QField-docs/edit/master/en/project-management/dataformat.rst)
to share your findings. If it does not work, please [open an issue](https://github.com/opengisch/OSGeo4A/issues). We will be happy to
help you with the implementation.

### Raster data

Raster data can become quite big quickly, when working with uncompressed
tiff files it\'s often several Gb of data. Especially on mobile devices,
this is inefficient.

## Use GeoPackage

We recommend to us the geopackage format to deal with raster data. The
following commands will convert a file called `raster.tif` to a file
`raster.gpkg` with pyramids. Make sure you adjust `EPSG:21781` to your
desired CRS.

``` bash
gdal_translate --config OGR_SQLITE_SYNCHRONOUS OFF -co  APPEND_SUBDATASET=YES -co TILE_FORMAT=WEBP -a_srs EPSG:21781 -of GPKG raster.tif raster.gpkg
gdaladdo --config OGR_SQLITE_SYNCHRONOUS OFF -r AVERAGE raster.gpkg 2 4 8 16 32 64 128 256
```
