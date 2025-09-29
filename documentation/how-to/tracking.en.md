---
title: Tracking
tx_slug: documentation_how-to_tracking
---

# Tracking

:material-tablet: Fieldwork

QField allows you to track your position through the creation of points, lines or polygons while browsing the map, working on other features and layers, or in the background while having the device in your pocket.
To enable tracking, you need to ensure that your positioning is activated.

## Set-Up Tracking Session

1. Open the main dashboard legend and long-press on the layer which you want to use for tracking.
2. Select **Setup tracking** and a new window will appear showing the configuration settings.

    !![](../assets/images/tracking-layer-properties.png,350px)

    You can choose between two options for the recording interval of vertices during the tracking session:

    - The `Time requirement` records your position at a regular rate (e.g., every 30 seconds), which is ideal for consistent logs and saving battery.
    - The `Distance requirement` is more efficient, recording a point only after you move a minimum distance.
      This keeps your track clean by ignoring movement when you are stationary.
    To capture fine detail on steep or winding terrain, use a shorter distance, for straight routes, a longer distance is better.

    !![](../assets/images/tracking-settings.png,350px)
    - The erroneous distance safeguard option can be turned on to insure sporadic bad GNSS readings are not tracked.
    The functionality relies on providing a maximum tolerated distance from the last recorded position beyond which readings will be skipped.
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

1. Open the side dashboard and press on the layer's tracking badge you want to stop.

1. Open the side dashboard and press long on the tracking layers layer
2. Select the *Stop tracking* button.

!![](../assets/images/tracking-stop.png)

## Automatic Tracking Sessions

This functionality enables one or more position tracking sessions to automatically start upon project load.
The feature form of the layer will immediately open asking you for the attributes.
If the tracked vector layer has the "Hide Form on Add Feature" mode selected, the feature form will be skipped.

!![Hide Form on Added Feature](../assets/images/hide-form-on-add-feature.png)

### Configuration of an Automatic Tracking Session

1. Open the properties of the vector layer you want to track your position against and go to the QField tab.

2. Activate "Tracking Session" and specify the tracking requirements.

!![Activating automatic "Tracking Sessions" in QFieldSync](../assets/images/automatic-tracking-session.png)

!![Tracking activated automatically in QField](../assets/images/qfield-tracking-session.png,350px)

!!! note
    ### Benefits
    - **Efficiency**: Automation saves time and effort in the field.
    - **Flexibility**: Users can customize sessions and opt for automatic initiation with default values.
