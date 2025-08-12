---
title: Tracking
tx_slug: documentation_how-to_tracking
---

# Tracking


:material-tablet: Fieldwork

QField allows you to create points, lines or polygons and track yourself in the background while working on another feature layer or while having the device in your pocket. To enable tracking, you need to ensure that your positioning is activated.

## Set-Up Tracking Session

1. Open the legend and press long on the layer which you want to use for tracking
2. Select **Setup tracking** and a new window will appear showing the configuration settings


!![](../assets/images/tracking-layer-properties.png,350px)

You can choose between two options how the number of vertices will be recorded during the tracking session:

- A minimum time interval
- A minimum distance


    !![](../assets/images/tracking-settings.png,350px)

In the case that you wish to ensure that the next vertex is set not too far away from the most recent one (for example if you are in steep terrain and elevation is relevant), you can set a maximum tolerance distance.

!![](../assets/images/maximum-distance-tolerance.png,350px)


3. Tap the **Start tracking** button to begin the tracking.
4. Set the attributes for the feature(s) about to be created.



!!! note
    For line and polygon layers, a single feature will be created per tracking session, with its geometry formed from the recorded positions.
    For point layers, a new feature will be created for each recorded position, and the attribute values entered in the form will be remembered for subsequent points.


!!! tip
    QField will skip the feature form if the layer is configured to hide all attributes or if the form has been set to hide on feature addition in the attribute form settings.
    This can streamline the process of starting tracking sessions.

## Resuming to a Previous Session

If did not explicitly terminate your tracking session (for example, you closed the app), QField allows you to continue where you left off.
A prompt will appear asking whether to **resume the last session** or **start a new one**.

- **Resuming** a session for a line or polygon layer will continue adding vertices to the feature from the previous session.
This allows you to simply continue across app restarts.

- **Starting a new session** will discard the incomplete feature from the previous session and begin a new one.

## Tracking underway

Once a tracking session has been set up, a badge will appear in the side dashboard legend next to the layer(s) against which tracking is being recorded.

!![](../assets/images/tracking-badge.png)

The features created by the tracking session are saved on every vertex recorded.
A rubberband line overlayed onto the map is attached to each tracking session, allowing you to glance at what has been recorded.

If the layer linked to a tracking session supports the M dimension, QField will store
the time passed since the first vertex recorded in each vertex's M value.

!!! tip
    You can simultanously record multiple trackings sessions across several layers.


## Terminate tracking

1. Open the side dashboard and press long on the tracking layers layer
2. Select the *Stop tracking* button.

!![](../assets/images/tracking-stop.png)

## Automatic Tracking Sessions

This functionality enables one or more position tracking sessions to automatically start upon project load.
The feature form of the layer will immediately open asking you for the attributes.
If the tracked vector layer has the "Hide Form on Add Feature" mode selected, the feature form will be skipped.

!![Hide Form on Added Feature](../assets/images/hide-form-on-add-feature.png)

### Configuration of an automatic Tracking Session

:material-monitor: Desktop preparation

1. Open the properties of the your tracking layer and direct to the QField tab .
2. Activate "Tracking Session" and specify the tracking requirements.

!![Activating automatic "Tracking Sessions" in QFieldSync](../assets/images/automatic-tracking-session.png)

!![Tracking activated automatically in QField](../assets/images/qfield-tracking-session.png,350px)

!!! note
    ### Benefits
    - **Efficiency**: Automation saves time and effort in the field.
    - **Flexibility**: Users can customize sessions and opt for automatic initiation with default values.
