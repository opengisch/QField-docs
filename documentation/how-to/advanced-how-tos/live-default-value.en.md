---
title: Live default value
tx_slug: documentation_how-to_live-default-value
---

# Live Default Values

QField supports live updating of default attribute values when editing features.
Modifying one attribute value automatically updates dependent attribute fields configured with dynamic default expressions.
For example, selecting a scientific species name can automatically populate a common species name or retrieve a corresponding image.

## Configuring Live Default Values
:material-monitor: Desktop preparation

Configure live default values in QGIS layer properties by combining default value expressions with the **"Apply default value on update"** setting.

!!! Workflow
    1. In QGIS, navigate to _Vector Layer Properties... > Attribute Form_.
    2. Select the target field that should update automatically (such as `photos`).
    3. Enter your dynamic expression in the **"Default value"** field.
    4. Enable **"Apply default value on update"**.
        !![Live default value image configuration](../../assets/images/live_default1.png,700px)
    5. Select the triggering attribute field (such as `plant_species`) configured with a **Value Relation** or **Value Map** widget.
    6. Configure the widget properties and default expressions as needed.
        !![Live default value relation configuration](../../assets/images/live_default2.png,700px)
    7. Click **"OK"** and save your project.

## Usage Example
:material-tablet: Fieldwork

When editing feature attributes in QField, changing a value in a parent field immediately re-evaluates expressions and updates dependent default fields in real time.

![type:video](../../assets/videos/live_default_value.webm)
