---
title: Tracking
tx_slug: documentation_how-to_tracking
---

# Tracking

## General Settings
:material-tablet: Fieldwork

QField allows you to track your position through the creation of points, lines or polygons while browsing the map, working on other features and layers, or in the background while having the device in your pocket.

See [Here](../../fieldwork/navigation-and-positioning/tracking.md) how it looks in QField.

## Automatic Tracking Session

You can configure the QGIS project in such a way that one or more position tracking sessions automatically start when opening a project in QField.
The feature form of the layer will immediately open asking for the attributes.
You can also hide the attribute form so that the tracking session automatically starts.

!!! Workflow

    1. In QGIS for your tracking layer direct to  *Layer Properties* > *QField*
    2. Activate "Tracking Session" and specify the tracking requirements.

        !![Activating automatic "Tracking Sessions" in QFieldSync](../../assets/images/automatic-tracking-session.png)

        !![Tracking activated automatically in QField](../../assets/images/qfield-tracking-session.png,350px)

    3. (Optional) hide your attribute form when automatically starting a session by directing to *Layer Properties* > *Attribute form* and selecting the "Hide Form on Add feature" option.

        !![Hide Form on Added Feature](../../assets/images/hide-form-on-add-feature.png)

- **Efficiency**: Automation saves time and effort in the field.
- **Flexibility**: Users can customize sessions and start sessions without entering any attribute information by customising the feature with default values.
