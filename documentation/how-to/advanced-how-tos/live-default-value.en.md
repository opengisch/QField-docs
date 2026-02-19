---
title: Live default value
tx_slug: documentation_how-to_live-default-value
---

# Live default value

QField is supporting the "live" updating of default attribute value when editing features.
This means, when changing one value in an attribute another automatically adjusts.
Examples for this could be species names that are both recorded with the original species name and the common name.

!!! Workflow

    ## Configuration

    :material-monitor: Desktop preparation

    In this example, the image will automatically update when a different plant_species is chosen.

    1. Direct to the layer properties, where you want to set the updating value field.
    2. Go to the 'photos' field and add the following expression into the default value.
    3. Toggle the *apply default upon update*.

     !![live default value image](../../assets/images/live_default1.png,700px)

     4. Go to the plant_species field where your *value relation* is set as a widget type.
     5. Add the following expression as shown below into the default value.

     !![live default value relation](../../assets/images/live_default2.png,700px)

     6. Press Ok and save.

!!! Example

    In the video below there is an example of "live" default value updates when editing features on QField.

     !![Live_Default_Value](../../assets/videos/live_default_value.webp)
