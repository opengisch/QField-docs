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


Identify features
=================

A long press on a feature will identify it. Pressing the back button will close the identify window.

Exceptions to identified layers
-------------------------------

Often it is not required to be able to query every layer. Some layers are only present as basemap and their attributes are not of interest.

You can manage this layerlist in QGIS desktop in :menuselection:`Project --> Project Properties --> Identify Layers` and uncheck the base layers.

GPS
===

A long press on the GPS button will show the GPS menu.

Digitize
========

To start digitizing new features `Switch modes`_ to digitizing.

A new combobox will appear next to the menu button which lists the layers
available for digitizing.
At the moment (QField 0.6), QField supports point and line layers.

Points
......

Navigate the crosshair in the center of the screen to the desired location and
click the pencil at the lower right of the screen to confirm the creation of a
new point feature.

Lines
.....

Navigate the crosshair in the center of the screen to the desired start of the line
and click the pencil at the lower right of the screen.
Proceed with adding points or removing points until the line is finished and then click save.

Attribute form
--------------

After digitizing a geometry, the attribute form will be displaied if it is not suppressed
and the user will be asked to enter the attributes for the new feature.
The form which appears allows entering attribute values for the new feature. The checkboxes
at the right of every attribute allow for remembering each attribute individually.

Delete Features
===============

To delete a feature, identify it first and tap the trash icon.
