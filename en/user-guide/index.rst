#################
QField User Guide
#################

**************
Basic workflow
**************

Switch modes
============

Modes are switched via :menuselection:`Menu button --> mode`

Opening a project
=================


Identifying features
====================

A long press on a feature will identify it. Pressing the back button will close the identify window.

Exceptions to identified layers
-------------------------------

Often it is not required to be able to query every layer. Some layers are only present as basemap and their attributes are not of interest.

You can manage this layerlist in QGIS desktop in :menuselection:`Project --> Project Properties --> Identify Layers` and uncheck the base layers.

GPS
===

A long press on the GPS button will show the GPS menu.

Digitizing
==========

To start digitizing new features `Switch modes``_ to digitizing.

A new combobox will appear next to the menu button which lists the layers
available for digitizing. At the moment (QField 0.5), QField only supports point
layers.

navigate the crosshair in the center of the screen to the desired location and
click the check at the lower right of the screen to confirm the creation of a
new point feature. If the feature form is not suppressed (in the QGIS project
vector layer properties), the user will be asked to enter the attributes for
the new feature.

Attribute form
--------------

The form which appears allows entering attribute values for the new feature. The checkboxes
at the right of every attribute allow for remembering each attribu. The checkboxes
at the right of every attribute allow for remembering each attribute individually.
