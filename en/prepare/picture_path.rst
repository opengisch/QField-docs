
Configurable picture path
=========================

QFieldSync gives the possibility to configure the path of picture attachments.

1. Go to QFieldSync plugin --> Project configuration
2. Select the table "Photo Naming"
3. Choose the layer, the field and configure the expression 

Use expressions to configure the path of the attachments. Usually DCIM is used as the main folder and it's the default.

.. container:: clearer text-center

    .. image:: /images/picture_path.png
       :width: 600px
       :alt: picture_path


Synchronize files of DCIM folder
--------------------------------
On import copy files from DCIM folder to original project path and on export to offline project path.

Subfolders are created if they don't exist and existing files are overwritten.

Fix adding project folder
------------------------
If it's already defined on export, it does not create a project folder again.
