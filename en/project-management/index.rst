QField Project Management
=========================

You will need a portable version of your QGIS project file (.qgs). Portable
means that all paths are relative and datasets are reachable from the device.

Check that :menuselection:`Project --> Project Properties --> General --> Save paths` is set to "Relative" and that all required data files are in the same folder like the .qgs file or a subfolder of it.

For increased productivity, we suggest having a look at the following plugins:

* `QConsolidate plugin <https://plugins.qgis.org/plugins/qconsolidate/>`_
* `Offline Editing plugin <https://docs.qgis.org/2.8/en/docs/user_manual/plugins/plugins_offline_editing.html>`_

Data sources
------------

While many data providers are supported, there are still some stability issues
with the OGR provider (E.g. Shapefile). For best stability you should use
spatialite files or a postgis database.

Vector Layer Settings
---------------------

Most of the settings which QGIS offers are directly supported by QField without any extra effort.

Style
.....

All style settings from QGIS are directly supported by QField. This includes all renderer types like graduated, categorized, rule based, 2.5D as well as data defined symbology.

Forms and Fields
................

QField creates forms similar to, but not equal to QGIS.

Suppress Feature Form
  The setting suppress feature form is directly applied to the QField form.

Remember last values
  QField offers a much more fine-grained control over the last used values and ignores the QGIS setting.

Field settings
  The field settings from QGIS are supported on a beste effort basis and is constantly being improved.

  .. role:: yay
  .. role:: nay
  .. role:: moreorless

  +-------------------+----------+-------------------------------------------------+
  | Field type        | Support  | Notes                                           |
  +===================+==========+=================================================+
  | Text Edit         | :yay:`✔` | - Multiline is always allowed                   |
  |                   |          | - HTML is not supported                         |
  +-------------------+----------+-------------------------------------------------+
  | Check Box         | :yay:`✔` |                                                 |
  +-------------------+----------+-------------------------------------------------+
  | Value Map         | :yay:`✔` |                                                 |
  +-------------------+----------+-------------------------------------------------+
  | External Resource | :nay:`✔` |  Will be combined with shooting photos.         |
  |                   |          |  Contact us for development.                    |
  +-------------------+----------+-------------------------------------------------+
  | Date Time         | :nay:`✔` |  Contact us for development.                    |
  +-------------------+----------+-------------------------------------------------+
  | Others            | :nay:`✔` |  Contact us for development.                    |
  +--------------+----------+------------------------------------------------------+

Custom SVG symbols and settings
===============================

In the about dialog you can see where the shared folders are on your device.

If you want to use custom symbols you need to put them there using a file manager.
