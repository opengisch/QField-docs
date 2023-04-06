---
title: Supported Data Formats
tx_slug: documentation_reference_data-format
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

The [Cloud Optimized Geotiff (COG)](https://www.cogeo.org/) format will offer best user experience for offline basemaps.
Combined with JPEG compression, it will reduce the raster size.

The following commands will convert a file called `raster.tif` to a COG file `raster_cog.tif` using JPEG compression.

``` bash
gdal_translate raster.tif raster_cog.tif -of COG -co BLOCKSIZE=512 -co COMPRESS=JPEG -co QUALITY=75 -co BIGTIFF=YES
```

### Advanced examples with COG

If you have several files to assemble, first, you need to create a VRT files with QGIS or trough following commands to index all TIF files inside a directory.  Make sure you adjust `EPSG:2056` to your desired CRS.

``` bash
gdalbuildvrt raster_mosaic.vrt TIF_Directory/*.tif -addalpha -hidenodata -a_srs EPSG:2056
```

Then convert VRT file to COG.

``` bash
gdal_translate raster_mosaic.vrt raster_cog.tif -of COG -co BLOCKSIZE=512 -co COMPRESS=JPEG -co QUALITY=75 -co BIGTIFF=YES
```

If the raster data is too low quality, adjust the compression level and set QUALITY=85.

Some extra parameters can be set :

- `a_srs` can be used also in gdal_translate command when CRS is not define in the source raster dataset.
- `OVERVIEW_RESAMPLING` offer different renderer when zooming out. The default value is NEAREST but you can try also BILINEAR or AVERAGE.
- `NUM_THREADS` will help you to balance between use all your CPU ressources or only part. Set ALL_CPUS or define the number of thread you want to use.

Combining all extra parameters, command line may look like this :

``` bash
gdal_translate raster.tif raster_cog.tif -a_srs EPSG:2056 -of COG -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=BILINEAR -co COMPRESS=JPEG -co QUALITY=75 -co NUM_THREADS=6 -co BIGTIFF=YES
```
