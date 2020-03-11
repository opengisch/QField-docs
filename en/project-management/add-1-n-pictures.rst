
Add 1:n pictures
====================

You can add one or more pictures to a feature. Below you find an exemple how to proceed.

Creating tow tables
--------------------

**hive (Sprengungen in the screenshots)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* id (UUID)
* geometry
* ...

**hive_picture (sprengung_bild in the screenshots)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* id
* hive_id (UUID)
* path (TEXT)
* ...

Relations
----------

create a relation with:

* ``hive`` Referenced layer
* ``id`` Referenced field
* ``hive_picture`` Referencing layer
* ``hive_id`` Referencing field

.. container:: clearer text-center

    .. image:: /images/add-1-n-pictures-relations.png
       :width: 600px
       :alt: Relations

Widgets
--------

hive
~~~~~

set default value of id to ``uuid()``. No need to show it in the form.

.. container:: clearer text-center

    .. image:: /images/add-1-n-pictures-widgets.png
       :width: 600px
       :alt: widgets
set the relation widget to ``Many to one relation``

.. container:: clearer text-center

    .. image:: /images/add-1-n-pictures-widgets2.png
       :width: 600px
       :alt: widgets2

picture
~~~~~~~

set widget type of path to ``attachment``

.. container:: clearer text-center

    .. image:: /images/add-1-n-pictures-widget_picture.png
       :width: 600px
       :alt: widget picture

