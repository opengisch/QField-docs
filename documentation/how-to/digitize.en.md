---
title: Digitize
tx_slug: documentation_how-to_digitize
---

# Digitize

QField allows to digitize, edit and delete point, line and polygon features while in the field.

## Collect features
:material-tablet: Fieldwork

To start digitizing new features, enable the *Edit mode* by clicking on the *pencil icon*
in the side dashboard and selecting the layer within which you want to add new features.

!![](../assets/images/activate-edit-mode.png)

The current layer within which features are to be added is highlighted in green.

### Adding point features

Navigate the crosshair in the center of the screen to the desired
location and click the *Plus (+) button* at the lower right of the screen to
confirm the creation of a new point feature.

You can use the *lock to position* button to force the crosshair to
center on your location if you have enabled positioning.

### Adding line or polygon features

Navigate the crosshair in the center of the screen to the desired start
of the line or polygon and click the *Plus (+) button* at the lower
right of the screen to add the first node.

Proceed with adding points to form you line or polygon by clicking the
*Plus (+) button* each time you want to add a new node.

Click the *Minus (-) button* to remove the last added node.

When you have added a least 2 nodes for a line or 3 nodes for a polygon,
a *Save button* will appear. Click on it to finish your geometry.

!![](../assets/images/collect_features.webp,250px)

While digitizing, you can click the *(x) button* to cancel the current feature creation.

!!! note
    QField insures that digitized geometries will not have duplicate vertices and respects
    the geometry precision settings from the currently selected layer.

You can use the volume keys for adding or removing vertices while in digitizing mode. This functionality can be activated in Settings in the General tab.

!![](../assets/images/activate-digitize-with-volumen-keys.png)

!!! note
    This feature is available on Android only.

Additionally, QField has a _finger tap_ digitizing mode where vertices are added by tapping on the canvas. Activated through the settings panel, this mode caters to scenarios where rapid data input is crucial.

!![](../assets/images/activate_finger_tap_digitizing.png)

### Attribute form

After digitizing a geometry, the attribute form will appear allowing you
to edit attribute values for the newly-added feature.

!!! note
    You can supress the attribute form upon feature addition via a configuration option
    for a given layer via its properties dialog in QGIS

Moreover, you have the option to digitize the form using the scanning QR or Bar Code reader functionality available within the feature form's text edit widget.

!![](../assets/images/digitizing-with-qr-code-1-attribute-form.png)

Upon clicking the three-dot icon button, a menu will be presented offering three distinct actions: "Copy," "Paste," and "Scan Code".

!![](../assets/images/digitizing-with-qr-code-2-selecting-scan-code.png)

Opting for the "Scan Code" action will trigger QField's code reader, initiating the scanning process to decode the code.

!![](../assets/images/digitizing-with-qr-code-3-code-reader.png)

Once the codes have been successfully scanned, users can validate their choice by clicking the checkmark (✔️) OK button. This action will populate the attribute with the decoded value, streamlining the digitization process.

!![](../assets/images/digitizing-with-qr-code-4-it-worked.png)

In addition, the Code Reader offers the capability to read NFC text tags.

!![](../assets/images/code-reader-nfc-text-tag.png)

!!! note
    Both the QR code camera and the NFC text tag detector are enabled by default when you open the Code Reader. You have the flexibility to disable either of these features to ensure that your device's battery is not used unnecessarily by using hardware that you may not need at the moment.

#### Remember attribute values

For quick collection of rather homogeneus datasets, it is crucial to not
having to enter the same attribute values over an over. The checkboxes
at the right of every attribute allow remembering of the last entered value for
each attribute individually so that the next time you will add a feature on the same
layer, these attributes will be automatically pre-filled.

!![](../assets/images/remember_checkboxes.webp,250px)

## Geometry editing
:material-tablet: Fieldwork

To edit the geometry of pre-existing features, enable the *Edit mode* by tapping on
the *pencil icon* in QField's side dashboard.

Once in edit mode, a new *Edit geometry* button will appear in the title bar of an identified
feature form. Clicking on the button will activate the geometry editor environment which offers
four tools:

- A vertex editor tool;
- A geometry split tool;
- A geometry reshape tool; and
- A geometry ring tool.

### Vertex tool

The vertex editor allows you to move or delete pre-existing vertices as well as adding new
vertices to geometries.

### Split tool

The split tool allows you to split line and polygon geometries into two halves, one of which will
become a new feature of its own.

### Reshape tool

The reshape tool allows you to change line and polygon geometries by drawing shapes which will
result in a reshaped line following the edge of the drawn shape or a polygon with the drawn shaped
used to clip or expand the geometry.

### Reshape eraser tool

The reshape eraser tool is designed to ease the removal of parts of a line or polygon geometry. The tool mimics eraser tools from 2D drawing programs and works best with a stylus.

Suppose you have a polygon representing a building footprint, but there's an unwanted protrusion. You can use the erase tool to precisely remove that portion of the polygon, ensuring accuracy in your geometry representation.

![type:video](../assets/videos/new-erase-reshape-tool.webm)

### Ring tool

The ring tool allows you to digitize rings (i.e. holes) into polygon geometries. Once a ring
is created, QField will offer the possibility of filling the ring with a new feature.

### Demonstration of geometries editing

A video demonstration of some editing possibilities:

!![](../assets/images/edit_geom.webp,250px)

## Merging features

QField allows you to merge features and their geometries into a single feature. To do so, identify two (or more)
features on the map, select them in the features list and merge them by selecting
the *Merge Selected Features* in the *Menu (⁝) Button*.

To execute merging within QField, ensure the following conditions:

1. **Editable Vector Layer:**
   - The target layer must be an editable layer.

2. **Multi-Type Geometry:**
   - Ensure that the geometry type of the layer is multi-type.

3. **Data Provider's Abilities:**
   - Verify that the data provider associated with the layer (preferably GeoPackage) possesses the capability to:
      - Modify geometries: The ability to make changes to existing geometrical structures.
      - Delete features: The capability to remove individual features from the dataset.

## Freehand digitizing

The freehand digitizing mode allows you to "draw" lines and polygons
using their stylus pen or mouse. The mode is available for line and polygon
feature additions as well as the above-mentioned geometry editor's rings,
split, and reshape tools.

The freehand digitizing mode is activated through a new toolbar button
which appears when QField is set to editing mode and a stylus pen or
a mouse is hovering the map canvas while a line or polygon vector is selected.

![type:video](https://player.vimeo.com/video/537673220)<!-- markdown-link-check-disable-line -->

## Topological editing

If topological editing is activated on the project QGIS before exporting
for QField, shared nodes of neighbouring geometries are modified
together when moving / deleting vertices and additional vertices are
added to segments when a new node is added from neighbouring
geometries.

!![](../assets/images/edit_topo.webp,250px)

### Multi-editing of attributes

QField allows you to select multiple features and edit their attributes all at once.
In some cases, it can result in very efficient workflows. To do so, identify two (or more)
features on the map, select them in the features list and merge them by selecting
the *Edit feature* button in the list's title bar.

![type:video](https://player.vimeo.com/video/499565955)<!-- markdown-link-check-disable-line -->

## Delete features
:material-tablet: Fieldwork

Deleting a feature is done by selecting the *Delete feature* action in the
feature form's *3-dot menu*.

!![](../assets/images/delete-single-feature.png)

QField also allows you to delete multiple features at a time. To do so, first
identify the features by short tapping on the relevant parts of the map. Then activate
the multi-selection mode by long pressing on one of the features you want to delete.
When checkbox appears next to the feature names, select further features
to delete (you can tap on the map to add more features too). Once done, select the *Delete Selected Feature(s)*
action in the features list *3-dot menu*.

!![](../assets/images/delete-multiple-features.png)

## Snapping
:material-monitor: Desktop preparation

While digitizing new features, new points can be snapped to existing
geometries.

All configuration can be done in *Project > Snapping Settings*

### Snapping Types

It is possible to snap new points

-   only to nodes of existing geometries
-   only to segments of existing geometries
-   to nodes and segments of existing geometries

### Snapping to layers

It is also possible to only snap to one or a few layers.

### Snapping tolerance

The snapping tolerance can be specified in map units or pixels.

In almost any case, the units should be set to pixels. We made good
experiences with a tolerance value of 20.

## Snap to Common Angle

The Snap to Common Angle feature enhances the precision and efficiency of digitizing geometries by allowing to snap to predefined common angles: 10°, 15°, 30°, 45°, and 90°. This functionality is similar to the advanced digitizing tool in QGIS.

To activate Snap to Common Angle, open the geometry editor and tap on the Snap to Common Angle icon in the toolbar to bring up a menu of common angles. Choose the desired angle from the menu. Then, start digitizing your geometry or adding vertices, and the functionality will automatically align your input to the selected angle. QField will remember the angle relative to the last segment situation for consistent snapping behavior during subsequent edits.

![type:video](../assets/videos/snap-to-common-angles.webm)
