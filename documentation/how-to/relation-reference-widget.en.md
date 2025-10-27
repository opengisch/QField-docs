---
title: Relation Reference Widget
tx_slug: documentation_how-to_relation-reference-widget
---

# Relation Reference Widget

Sometimes it can be useful to relate different layers with each other when they are depending on each other or when you want to add more than one record to a feature.

!!! Example

    *In a building there are several appartments with different owners.
    We can create a relation between the building and the appartments and between the appartments and the owners.*

In such a case we make use of the relation reference widget to be able to add new children or to select a child from the existing ones.

## Relation configuration

Before adding, editing or viewing the related features you have to set up a relation between the two layers.
Here it is important that you add an id (`primary key`) field to the parent layer (`Reference Layer`) that can be  used as a `foreign key` in the child layer (`Referencing layer`).
These fields are used for creating the link between the two layers.
Therefore, they must be unique.
**Note:** It is good practice to use `uuid's` as "unique ids" given they are 36 characters long and also contain non-numerical characters making them much safer to use over ordinary numerical ids.

!!! Workflow

    **Creating the relation**

    1. Direct to *Project* > *Properties* > *Relations*
    2. Press the green plus to add a new relation
    3. Set your *Reference* and your *Referenced* Layer in addition to the corresponding fields that will be used for the linking.
    For more details please refer to the [official QGIS documentation](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/joins_relations.html#many-to-many-n-m-relations)

    **Attribute Form Configuration - Reference Layer**

    1. Direct to the *Layer Properties* > *Attribute Form*
    2. Find your `reference field`, set the widget type to UIID generator and set a default value to *uuid('WithoutBraces')
    3. Find your relation under the "Relations Section" and add it to the form layout
    4. Set the *Cardinality* to *"Many to one relation"*
    5. Under the widget you can define whether children can be:
        - linked
        - unlinked
        - edited
        - added
        - duplicated
        - deleted
        - zoomed into
    6. (Optional) If you want to filter your children further, you can use additional "expressions".
    7. Once finished click "ok"

    !![](..assets/images/relation_editor_widget_list.png, 400px)

    **Attribute Form Configuration - Referencing Layer**

    1. Direct to the *Layer Properties* > *Attribute Form*
    2. Configure your attribute form with the wanted fields.
    3. (Optional): Under *Display* you can set the appearance of how the children will be displayed




## Maximum number of visible children

It is possible to limit the number of available children for your related layer if you are not interested in all items.

- **Default Number of visible children:** 4 children
- **Unlimited:** Empty

!!! Workflow

    1. Direct to Vector Layer *Properties...* > *QField*.
    2. Under "Relationship Settings" set the "Maximum number of items visible".

    !![Maximum items visible for relation](../assets/images/setting-maximum-items-visible-in-relation.png)

    !![QField Visible items](../assets/images/maximum-items-visible-in-relation.png,300px)

## Many-To-Many relations

In the case of many-to-many relations you will need a linking table, which commonly is also termed as a "pivot table".
In the official [QGIS documentation](http://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/joins_relations.html#many-to-many-n-m-relations) you will find a detailed description on how to establish these more complex relations.

## Ordered Relation

If required you can reorder linked child features based on a field by selecting the **Ordered Relation Editor** from the widget type options.
To enable this functionality, however, you require a second plugin [Ordered Relation Editor](https://github.com/opengisch/qgis-ordered-relation-editor) <!-- markdown-link-check-disable-line -->

!!! Workflow

    1. Install the Plugin [Ordered Relation Editor](https://github.com/opengisch/qgis-ordered-relation-editor) plugin from the official repository or through the "Plugin Manager" in QGIS.

    2. Open the Vector Layer *Properties...* > *Attributes Form* and set the layout editor to **Drag and Drop Designer**.

    3. Click on the relationship of your available widgets.

    4. Direct to *Properties* > *Attribute Form* and find your relation under the relationship section.

    5. On the right under "Widget Display" scroll down to the "Widget Type option and  select **Ordered Relation Editor**.

    6. Configure the widget using the following settings:

         - **Ordering Field**: Specify the field in the child layer that will be used to determine the order of the features.

         - **Description**: Define an expression to be displayed for each child feature in the list.

         - **Image Path (Optional)**: Provide a path to an image or icon to visually enhance the list. This is an expression that resolves dynamically.

    !![Widget configuration in QGIS](../assets/images/ordered_relation_widget_configuration.png)

    !![QField](../assets/images/ordered_relation_widget.webp,400px)

## Search in value relation and relation reference widget

It is possible to search values in a *value relation* or *relation reference* widget using the magnifying glass next to the field.

!![](../assets/images/autocomplete_search_value.webp,300px)

!!! note
    Define the *display expression* for the concerned layers, this will be used for searching for features.
    This is configured under Vector Layer *Properties...* > *Display*
