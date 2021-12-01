######################
Supported Data Formats
######################

QField supports a wide variety of formats via QGIS data providers and GDAL.
This page offers a non-exhaustive list of supported data formats.

Table
.....

  .. role:: yay
  .. role:: nay
  .. role:: moreorless

+-----------------+-----------------+---------------------------------------+
| Data Format     | Support         | Notes                                 |
+=================+=================+=======================================+
| SpatiaLite      | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| GeoPackage      | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| WMS             | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| WFS             | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| WFS-T           | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| PostGIS         | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| MBTiles         | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| Shapefile       | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| GeoTIFF         | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| JPEG2000        | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| WebP            | :yay:`✔`        |                                       |
+-----------------+-----------------+---------------------------------------+
| ECW             | :nay:`✘`        | License restricts usage.              |
+-----------------+-----------------+---------------------------------------+
| MrSID           | :nay:`✘`        | License restricts usage.              |
+-----------------+-----------------+---------------------------------------+

If you don't find your favorite data format on this table, please check if it
works and `adapt the list above <https://github.com/opengisch/QField-docs/edit/master/en/project-management/dataformat.rst>`_ to share your findings. If it does not work,
please `open an issue <https://github.com/opengisch/OSGeo4A/issues>`_. We will be
happy to help you with the implementation.

Raster data
===========

Raster data can quickly become quite big, especially when working with uncompressed file formats. Storage space being often more limited on mobile devices,
using this kind of file is inefficient. We recommend using the GeoPackage format to deal with raster data. The following commands will convert a file
called :code:`uncompressed.tif` to a file :code:`compressed.gpkg` with pyramids using WebP compression algorithm. Make sure you adjust ``EPSG:21781`` to your desired CRS.

.. code:: bash

  gdal_translate --config OGR_SQLITE_SYNCHRONOUS OFF -co APPEND_SUBDATASET=YES -co TILE_FORMAT=WEBP -a_srs EPSG:21781 -of GPKG uncompressed.tif compressed.gpkg
  gdaladdo --config OGR_SQLITE_SYNCHRONOUS OFF -r AVERAGE compressed.gpkg 2 4 8 16 32 64 128 256

It must be noted that if your data has negative or floating-point values, those will be rounded to the nearest positive integer if you convert
to GeoPackage. This is due to the fact that internally, raster data can only be stored using PNG, JPEG or WebP compression algorithms which all support
only positive integer values. An alternative is to store raster data as tiled GeoTIFF with pyramids using DEFLATE compression algorithm. The following commands will
produce such file.

.. code:: bash

  gdal_translate -co TILED=YES -co COMPRESS=DEFLATE -a_srs EPSG:21781 -of GTiff uncompressed.tif compressed.tif
  gdaladdo -r AVERAGE compressed.tif 2 4 8 16 32 64 128 256