---
title: Digitize and edit
tx_slug: documentation_how-to_digitize
---

# Digitize and Edit

With QField you can digitize, edit and delete points, lines and polygons and their according attributes while being in the field.
Similar to QGIS, QField has two modes.
The **Browse mode** and the **Digitize mode**.

## Snapping

If spatial precision and topological rules are important in your daily work, you can set the rules in QGIS before going into the field.
New features, new points can be snapped to existing geometries.

There is multiple ways in which new points can be snapped:

- **Snaping types**
    - To nodes of existing geometries.
    - To segments of existing geometries.
    - To nodes and segments of existing geometries.
- **Snapping to selected layers**: This option allows you to set the rule to only snap to selected layers.
- **Snapping Tolerance**: You can specify the tolerance upon when the snapping action takes place, either in pixels or in your set map units.

### Enable Snapping Rules

!!! Workflow

    1. Direct to the **Snapping Toolbar** in QGIS
    2. Open the **Project Snapping Settings**
    3. Set your snapping rules depending on your needs.

    Read more about snapping [Here](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#snapping-and-digitizing-options)

## Topological editing

To enable topological editing in QField, you have to activate in the QGIS project, before transferring or synchronizing your project.

!!! Workflow

    1. Direct to the **Snapping Toolbar** in QGIS.
    2. Activate the topological rule(s) as needed.
    !![Setting Topological rule in QGIS](../../assets/images/topological-setting.png,300px)
    Read more about Topological Rules [Here](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#topological-editing)
![type:video](../../assets/videos/edit_topo.webm)
