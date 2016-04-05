Supported data formats
======================

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
  | Spatialite      | :yay:`✔`        |                                       |
  +-----------------+-----------------+---------------------------------------+
  | WMS             | :yay:`✔`        |                                       |
  +-----------------+-----------------+---------------------------------------+
  | Postgis         | :yay:`✔`        |                                       |
  +-----------------+-----------------+---------------------------------------+
  | Shapefile       | :moreorless:`~` | May occasionally produce crashes      |
  +-----------------+-----------------+---------------------------------------+
  | Tiff            | :moreorless:`~` | JPEG compression not yet supported    |
  |                 |                 | Sponsoring welcome.                   |
  +-----------------+-----------------+---------------------------------------+
  | ECW             | :nay:`✘`        | License restricts usage.              |
  +-----------------+-----------------+---------------------------------------+
  | MrSID           | :nay:`✘`        | License restricts usage.              |
  +-----------------+-----------------+---------------------------------------+

If you don't find your favorite data format on this table, please check if it
works and adapt the list above to share your findings. If it does not work,
please `open an issue <https://github.com/opengisch/OSGeo4A/issues>`_. We will be
happy to help you with the implementation.
