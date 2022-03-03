---
title: Attribute Form Configuration
---

# Attribute Form Configuration

QField creates forms similar to, but not equal to QGIS.

## Suppress Attribute Form

The setting "suppress attribute form" is directly applied to the
QField form.

## Field widget

The field widgets from QGIS are supported on a best effort basis.


| Widget type        | Support          | Notes                                                                                                                                                                                                  |
|--------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text Edit          | :material-check: | - HTML is not supported <br> - Numerical input is enforced based on the type.                                                                                                                          |
| Check Box          | :material-check: |                                                                                                                                                                                                        |
| Value Map          | :material-check: |                                                                                                                                                                                                        |
| Hidden             | :material-check: |                                                                                                                                                                                                        |
| Attachment         | :material-check: | This field is combined with camera integration. It is also able to open other files like pdf and doc (if the user has an appropriate viewer) [Attachment (photo settings)](#attachment-photo-settings) |
| Date Time          | :material-check: |                                                                                                                                                                                                        |
| Relation Reference | :material-check: |                                                                                                                                                                                                        |
| Relation Widget    | :material-check: |                                                                                                                                                                                                        |
| Value Relation     | :material-check: |                                                                                                                                                                                                        |
| Others             | :material-close: | [Funding](../../get-started/support/#development-and-custom-apps)                                                                                                                                                                   |

## Relation Widget

For more information refer to the relations chapter of the official
[QGIS Documentation](https://docs.qgis.org/3.4/en/docs/user_manual/working_with_vector/attribute_table.html#creating-one-or-many-to-many-relations).

!![](../assets/images/relation_editor_widget_list.png)


The relation widget shows all the referencing child features in a list.
It is possible to add, delete and open them.

The visual identification of the list entries are done via the `Display
Expression` of the child layer.

### Key handling

Since the parents primary keys are used as foreign keys on the
referencing child features, these primary keys must be save to use even
after the synchronization back to the original data. Therefore we
recommend to use stable values such as UUIDs for primary keys.

It is possible to already add children from a parent that is about to be
added. This possibility will be blocked if there is no valid primary key
on the parent or the constraints are violated. In case the adding of the
parent feature is canceled after some children have been added already,
the children are deleted as well.

### Many-To-Many relations

On many-to-many relationships, according to the cardinality setting in
the QGIS Vector Layer Properties, on adding, deleting or opening an
entry in the list effects directly the child layer (on direct
cardinality) or the linking table (on many-to-one cardinality).

The second case is usually used when there are additional relation
information (e.g. percentage) in the linking table.

!![](../assets/images/relation_widget_cardinality.png)

In case of the many-to-one cardinality on many-to-many relations the
Display Expression needs to be set on the linking table.

### Attachment (photo settings)

The widget type "Attachment" is used with fields that store the path
to files.

It can be used to:

-   show and take photos
-   show links to external files like pdfs or documents

!![](../assets/images/attachement-setting.png)

The path should be set to relative. The pictures, pdf and docs are
stored then in a sub-directory of the project, where the link stored in
the textfield is pointing to.

In QField the picture is displayed. By clicking the camera symbol the
camera is started to update the picture with a new photo.

!![](../assets/images/qfield_picture.png)

On synchronization the sub-directory with the pictures, pdf and docs has
to be copied as well.

The option "hyperlink" on the attachment widget will disable the
camera functionality and enable a hyperlink to open a document (pdf,
doc, \...).

![](../assets/images/hyperlink_option.png)

## Value Relation

The widget "Value Relation" offers values from a related table in a
combobox. You can select layer, key column and value column. Several
options are available to change the standard behaviors: allow null
value, order by value and allow multiple selections. The widget will
display a drop-down or multiple-select list of the referenced features.

!![](../assets/images/value_relation_widget.gif)

## Drag and drop designer forms

Groups and Tabs from Drag and Drop designer forms are supported.

## Conditional visibility

Groups can be hidden based on an expression. This is useful when certain
attributes are only required under certain conditions. As an example
imagine mapping trees. Some of them might have a disease and you have a
list of possible deseases. To not clutter the form with many fields,
make a group and configure a visibility expression for a group
"diseases". Add a field "desease" with a checkbox. Only when the
checkbox is checked, the list of diseases will be available to the user.

!![Configuration of a group box that will only be shown if the checkbox "measures_taken" is checked.](../assets/images/conditional_visibility_configuration.png)

Let's see what we got on the field:

![type:video](https://player.vimeo.com/video/499565113)


## Constraints

Attribute fields can have constraints attached. Constraints are
expressions that needs to evaluate to `True` (or `1`) in order to be
able to save the form. Constraints are configured on a per-field basis
and a description can be added that will be shown to the user if a
constraint is not satisfied.

!![Configuration of a constraint within a range](../assets/images/constraint_configuration.png)

### Common use cases

You cannot enter an elevation value higher than the highest mountain in
this country.

``` sql
"elevation" < 5000
```

It is required to fill in an identifier.

``` sql
"identifier" IS NOT NULL
```

## Default values

Fields can have default values configured. Default values are inserted
into the attribute form when digitizing a new feature. They are visible
to the user and can be modified as long as the field is editable. They
can be based on the geometry or expression variables.

!![Configuration of a formatted date as default value](../assets/images/default_value_configuration.png)

### Additional variables

For more information regarding storing information related to your
position in object attributes, refer to the deticated
`GNSS documentation<gnss_variables>`{.interpreted-text role="ref"}.

### Common use cases

Insert positioning information as variable:

``` sql
@position_horizontal_accuracy
```

Insert the current date and time:

``` sql
now()
```

Insert the length of the digitized line:

``` sql
length($geometry)
```

Configure global variables on the device and insert them.

``` sql
@operator_name
```

If you want to assign a region code based on the location where a new
feature is inserted, you can do so by using an aggregate expression:

``` sql
aggregate( layer:='regions', aggregate:='max', expression:="code", filter:=intersects( $geometry, geometry( @parent ) ) )
```

To transform the coordinates received from \@position_coordinate to the
coordinate system of your project:

``` sql
x(transform(@position_coordinate, 'EPSG:4326', @project_crs ))
y(transform(@position_coordinate, 'EPSG:4326', @project_crs ))
```

::: {#snapping_results}
If you want to use the snapping results after drawing a line, you can
use the [\@snapping_results]{.title-ref} variable. The following code
extracts the value of the attribute [id]{.title-ref} of the snapping
match of the first point of a line.
:::

``` sql
with_variable(
  'first_snapped_point',
  array_first( @snapping_results ),
  attribute(
    get_feature_by_id(
      @first_snapped_point['layer'],
      @first_snapped_point['feature_id']
    ),
    'id'
  )
```

)

## Editable

The editable flag of fields is respected.

## Remember last values

QField offers a much more fine-grained control over the last used values
and ignores the QGIS setting.

## Auto-complete value

The "Use completer" checkbox must be checked to be able to use the
auto-complete in the value relation.

!![image](../assets/images/autocomplet_form.png)

Here a video showing how it works on QField
`Search in value list<search_value_list>`{.interpreted-text role="ref"}.
