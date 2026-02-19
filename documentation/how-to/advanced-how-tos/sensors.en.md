---
title: Sensors
tx_slug: documentation_how-to_sensors
---

# Sensors

QField offers a range of sensor functionalities that allow you to passively collect sensor data in the background,
display the collected data, and save it into newly-digitized feature attributes.

## Activating sensors

In QField, registered sensors are listed within the currently opened project file in a sub-menu that can be accessed via the "Side Dashboard" .

!!! Workflow

    1. Open the "Side Dashboard"
    2. Tap on the 3-dotted-menu and choose "sensor"

        !![](../../assets/images/main_menu_sensors.png)

    3. To toggle the passive collection of sensor data, simply click on a sensor name in the sub-menu.
     When active,a sensor icon will appear next to the sensor name, while when inactive, a dot icon will be shown.
     All active sensors that are collecting data will be listed in a sensors information table located at the bottom of QField's map canvas.

        !![](../../assets/images/sensors_information_panel.png)

## Sensor-Driven Tracking

QField enables you to initiate tracking sessions against a point layer, saving collected sensor data linked to
your current position.

!!! Workflow

    1. Open the layer properties of the point layer, where the sensor data will be stored.
    2. Direct to the attribute form layout.
    3. Set the [default value](../project-setup/attributes-form.en.md#define-default-values) to *"sensor_data('abc') where 'abc' corresponds to the name of the sensor.
    4. Once this configuration is done, you can start tracking your position against the point layer.
    When starting the tracking session, a sensor constraint can be activated to ensure that added points occur every time a sensor has captured new data.

     !![](../../assets/images/sensors_tracker_constraint.png)

!![](../../assets/images/sensors.webp,700px)
