QField Project Management
=========================

You will need a portable version of your QGIS project file (.qgs). Portable
means that all paths are relative and datasets are reachable from the device. We suggest having a look at the QConsolidate plugin and the Offline Editing plugin.

Data sources
............

While many data providers are supported, there are still some stability issues
with the OGR provider (E.g. Shapefile). For best stability you should use
spatialite files or a postgis database.
