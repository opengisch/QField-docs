QField Project Management
=========================

You will need a portable version of your QGIS project file (.qgs). Portable
means that all paths are relative and datasets are reachable from the device.

Check that :menuselection:`Project --> Project Properties --> General --> Save paths` is set to "Relative" and that all required data files are in the same folder like the .qgs file or a subfolder of it.

For increased productivity, we suggest having a look at the following plugins:

* `QConsolidate plugin <https://plugins.qgis.org/plugins/qconsolidate/>`_
* `Offline Editing plugin <https://docs.qgis.org/2.8/en/docs/user_manual/plugins/plugins_offline_editing.html>`_

Data sources
............

While many data providers are supported, there are still some stability issues
with the OGR provider (E.g. Shapefile). For best stability you should use
spatialite files or a postgis database.
