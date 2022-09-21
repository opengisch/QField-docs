---
title: Supported Data Formats
---

# Supported Data Formats

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
tiff files it's often several Gb of data. Especially on mobile devices,
this is inefficient.

### Use COG (Cloud Optimized GeoTIFF)

COG format will offer best user experience for offline basemap.
Combine with JPEG compression, it will reduce the raster size.

The following commands will convert a file called `raster.tif` to a COG file `raster_cog.tif` using JPEG compression. Make sure you adjust `EPSG:21781` to your desired CRS and `NUM_THREADS` (for example : 6) if you do not want to use all your computer ressources.

``` bash
gdal_translate raster.tif raster_cog.tif -a_srs EPSG:21781 -of COG -co BLOCKSIZE=512 -co COMPRESS=JPEG -co QUALITY=75 -co NUM_THREADS=ALL_CPUS -co BIGTIFF=YES
```

If you have several files to assemble, first, you need to create a VRT files with QGIS or trough following commands to index all TIF files inside a directory.

``` bash
gdalbuildvrt raster_mosaic.vrt TIF_Directory/*.tif -addalpha -hidenodata -a_srs EPSG:21781
```

Then convert VRT file to COG.

``` bash
gdal_translate raster_mosaic.vrt raster_cog.tif -of COG -co BLOCKSIZE=512 -co COMPRESS=JPEG -co QUALITY=75 -co NUM_THREADS=ALL_CPUS -co BIGTIFF=YES
```

If the raster data is too low quality, adjust the compression level and set QUALITY=85.
