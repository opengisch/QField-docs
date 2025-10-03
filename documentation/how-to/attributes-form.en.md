---
title: Simple attribute form configuration
tx_slug: documentation_how-to_attributes-form
---

# Attribute form

Before you go into the field, you will have to configure your forms - the fields that the user will see in the fields.
You can create the forms in your QGIS project.
It works the same way as it does for a regular QGIS project, but with a few differences.

## Attribute Form Configuration

To configure a form you have to open the vector layer's *Properties* > *Attribute form* in QGIS.

Depending on what behaviour you want for your different attributes, you can choose different "widget types".
Below is an overview what widget types are available and supported.

| Widget type        | Support          | Notes                                                                                                                                                                                                  |
|--------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text Edit          | :material-check: | - HTML is not supported <br> - Numeric input is enforced based on the field type.                                                                                                                          |
| Check Box          | :material-check: |                                                                                                                                                                                                        |
| Value Map    (dropdown or radio button)      | :material-check: |                                                                                                                                                                                                        |
| Hidden             | :material-check: |                                                                                                                                                                                                        |
| Attachment         | :material-check: | This field is combined with camera integration. <br> It is also able to open other files like pdf and doc (if you have an appropriate viewer) [Attachment (photo settings)](#configurable-attachment-path) |
| Date Time          | :material-check: |                                                                                                                                                                                                        |
| Range              | :material-check: |                                                                                                                                                                                                        |
| Relation Reference | :material-check: |                                                                                                                                                                                                        |
| Value Relation     | :material-check: |                                                                                                                                                                                                        |
| UUID Generator     | :material-check: |                                                                                                                                                                                                        |
| QML / HTML Widget  | :material-check: |                                                                                                                                                                                                        |
| Others             | :material-close: | [Funding](../get-started/contribute.md#feature-sponsoring)                                                                                                                                      |

## General Attribute Settings

In order to customize the attribute form, it is necessary to use the drag and drop designer in QGIS or to a use pre-written UI file.
You can also make use of powerful expressions to populate the different fields.
Additionally, to the ones available there are [QFieldCloud specific variables](../reference/expression_variables.md#qfieldcloud), which can be utilized inside the attribute form:

Below are some other general useful settings, which you can find in the Vector Layer *Properties...* > *Attribute form* (see image below).

- **Drag and drop designer**: You can structure your forms using various containers, such as tabs and groups, and enhance interactivity by incorporating conditional visibility of fields and assigning default values.
For more information refer to: [Drag and Drop Designer QGIS Documentation](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html#vector-attributes-menu)

- **Hide attribute form upon**: You can hide the attribute form by changing from the "Show form on Add Feature" to the setting "Suppress attribute form".
When adding a new feature in QField, no attribute form needs to be populated.
**Note**: In such a case, you have to configure the attribute form in such a way that all constraints/rules are met even if you do not add any attributes.

- **Editable**: You can decide whether a field is editable or not by activating it in the widget display of the corresponding field.
- **Remember last values**: If you don't want to add the same value again and again you can enable this option under the widget display in QGIS.
QField, however, offers a more fine-grained control over the last used values.
If you enable this option in QGIS, the rule will always apply.
With QField you can change and disable this option at any point during data collection.


!![General Attribute Form](../assets/images/drag-and-drop-designer-attribute-forms.png,800px)

## Value Map Widget Configuration

When using value maps as a widget type you can control the automatic switch from a "Radio buttons" interface to a list
!![QFieldSync Layer Properties](../assets/images/qfieldsync-toggle-value-map-editor-widget.png,800px).

!!! Workflow

    1. Direct to the Vector Layer *Properties* > *QField*

    2. Under the "Feature Form Settings" enable and define quantity of items that will trigger the transition to a toggle button interface.

    !![QField Value Map Editor as List](../assets/images/qfield-value-map-editor-list.png,300px)

    !![QField Value Map Editor as Buttons](../assets/images/qfield-value-map-editor-buttons.png,300px)


## Attachment Widget
:material-monitor: Desktop preparation

The widget type *Attachment* is used with fields that store the path to files.

It can be used to:

- Show and take photos or add pictures from the gallery
- Listen and record sound clips
- Show and record videos
- Show links to external files like PDFs or documents
- Add sketches directly in QField

!![Form attachment picture](../assets/images/attachement-setting-picture.png)

!![Form attachment audio](../assets/images/attachement-setting-audio.png)

!![Form attachment video](../assets/images/attachement-setting-video.png)

!!! note
    The path needs to be set to "relative".
    The pictures, audios, videos, pdf's and documents are stored then in a sub-directory of the project, where the link stored in the text field is pointing to.

You can add a new item when clicking the camera, video, microphone or document option.
Depending on what you have selected as default, one of them will be shown inside the form.

!![Media](../assets/images/attachments-qfield-media.png,300px)

On Synchronisation the sub-directory with the pictures, videos audios, pdf's and documents has to be copied as well.

By default when adding attachments QField automatically displays the file.
The option *hyperlink* on the attachment widget will disable that functionality and show just the path to the file hyperlink.

!![](../assets/images/hyperlink_option.png)

!!! Workflow
    **Set a specific attachment path**

    :material-monitor: Desktop preparation

    In QFieldSync you can configure the path of attachments.
    By default, pictures are saved into the "DCIM" folder, audio recordings are saved into the "audio" folder and videos are saved into "video" with a timestamp as name.

    1. Direct to the *Properties...* > *QField* > *Attachments Settings*
    2. Use specific expressions to set the required names of the attachments.

    !![Paths](../assets/images/paths-saving-media.png)

## Value Relation Widget

:material-monitor: Desktop preparation

The widget *Value Relation* offers values from a related table in a combobox.
Here you have several options to choose from:

- **Layer**: Set the table or layer that stores the values to be selected from.
- **Key column**: Set the column which contains the values that are to be saved.
- **value column**: Set the actual column which contains the values that are to be shown during collection.

- **Order by Value**: Set the order of how the displayed values should be shown.
This can either be by the "key", "value" or a specific column.
- **Group column**: You can group your values based on another column.
(eg. you want to collect information on tree species, you could group the values by the genus).
- **Allow NULL value**: The field can stay blank.
- **Use Completer**: You can use this option to auto-complete your fields.
When selecting the magnifying glass you can search under the available values and select accordingly.
- **Allow multiple selections**: If enabled, you can select multiple values in one feature.

!![](../assets/images/value_relation_widget.webp,300px)

!!! Workflow

    **Group Value Configuration**

    1. Choose the column that will be used to organize the items.
    The values from this column will act as group title.

    2. (Optional) Enable **Display group name** if you want to add the title of your group as a distinct header.
    This creates a clear separation between the different groups, making the list easier to navigate.

    !![First configuration](../assets/images/grouping_value_relations_widget_qgis_setting_001.png)

    !![Second configuration](../assets/images/grouping_value_relations_widget_qgis_setting_002.png)

    !![Third configuration](../assets/images/grouping_value_relations_widget_qgis_setting_003.png)

    !![Different configurations on QField](../assets/images/grouping_value_relations_widget_qfield_show_gruped.png)

!!! Workflow

    **Use Auto Complete**

    1. Direct to Vector Layer *Properties...* > *Attributes Form*.

    2. Your widget type needs to be "Value Relation".

    3. Enable the "Use completer" option.


    !![Enable auto-complete within QGIS](../assets/images/autocomplet_form.png)

    Here is a video showing how it works on QField

    !![](../assets/images/autocomplete_typing.webp,300px)


## Conditional Visibility
:material-monitor: Desktop preparation

You can hide whole groups based on expressions.
This is useful when certain attributes are only required under certain conditions.
!!! Workflow

    **Example: Accessing the status of tree species**

    *Some of them might have a disease and you have a list of possible diseases.*

    A typical step-by-step workflow could look like this:

    1. Create a group.

    2. Define a visibility expression for the group.
    *Eg. Only if the tree is marked as "sick", the field "disease" will appear.*

    3. Add the field that is to be shown only after the expression criteria is set into the group.
    *Eg. We will add our "type of disease" field into the group.*

    !![Configuration of a group box that will only be shown if the checkbox "disease" is checked.](../assets/images/conditional_visibility_configuration.png)

    In QField it will look like in the video below.

    !![](../assets/images/conditional_visibility.webp,300px)

## Define Constraints
:material-monitor: Desktop preparation

Attribute fields can have constraints attached.
Constraints are rules in the form of expressions.
Before a feature can be saved all constraints need to be met.
A description can be added that is shown if a constraint is not satisfied.

!![Configuration of a constraint within a range](../assets/images/constraint_configuration.png)

!!! Examples
    *You cannot enter an elevation value higher than the highest mountain in this country.*

    ``` sql
    "elevation" < 5000
    ```

    *It is required to fill in an identifier.*

    ``` sql
    "identifier" IS NOT NULL
    ```

## Define Default Values
:material-monitor: Desktop preparation

Fields can have default values configured.
Default values are inserted into the attribute form when digitizing a new feature.
They are visible and can be modified as long as the field is editable.

!![Configuration of a formatted date as default value](../assets/images/default_value_configuration.png)

!!! Attention

    The option "Apply default value on update" should be used with care and not for fields that act as primary keys.


## Working with expressions

When creating expressions for projects intended to be used with QField, it is recommended to use layer names rather than layer IDs.
This recommendation stems from the fact that during the project conversion process via QFieldSync, the resulting layers may receive different IDs, which can lead to incorrect expression evaluations.
By using layer names, you ensure that expressions are evaluated consistently and accurately across different project states.

!![Using layer names in expressions](../assets/images/using_layer_name_in_expressions.png)

## Additional variables

For more information regarding storing information related to your position in object attributes, refer to the dedicated [GNSS documentation](./gnss.md).

For QFieldCloud users, two variables can be used in expressions including attribute form's default values:

- `@cloud_username` which returns the  name of the currently logged in QFieldCloud user.
- `@cloud_useremail` which returns the email address of the currently logged in QFieldCloud user.

!!! Examples

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

    If you want to assign a region code based on the location where a new feature is inserted, you can do so by using an aggregate expression:

    ``` sql
    aggregate( layer:='regions', aggregate:='max', expression:="code", filter:=intersects( $geometry, geometry( @parent ) ) )
    ```

    To transform the coordinates received from \@position_coordinate to the coordinate system of your project:

    ``` sql
    x(transform(@position_coordinate, 'EPSG:4326', @project_crs ))
    y(transform(@position_coordinate, 'EPSG:4326', @project_crs ))
    ```

    ::: {#snapping_results}
    If you want to use the snapping results after drawing a line, you can use the [\@snapping_results]{.title-ref} variable.
    The following code extracts the value of the attribute [id]{.title-ref} of the snapping match of the first point of a line.
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
    )
    ```

## Define QML Widgets

Custom QML widgets can be useful to integrate advanced actions into forms.

!!! Example

    *We define add a button that open a third-party map and navigation app.
    This is useful to open e.g. turn-by-turn navigation on the device-native app for the user.*

    ```qml
    import QtQuick 2.0
    import QtQuick.Controls 2.0

    Button {
        width: 200
        height: width/5
        text: "Open in Maps"
        onClicked: {
            Qt.openUrlExternally(expression.evaluate("'geo:0,0?q=' || $y || ',' || $x"));
        }
    }
    ```

    The `geo` URI above is adapted to work with Android. For Apple Maps the URI can be changed to `'geo:' || $y || ',' || $x`.

    ![](../assets/images/qml_widget_button.png)
