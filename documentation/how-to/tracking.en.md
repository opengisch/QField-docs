---
title: Tracking
tx_slug: documentation_how-to_tracking
---

# Tracking

QField allows you to create points, lines, and polygons from tracking your position.

## Activate and Resume Tracking

:material-tablet: Fieldwork

To begin tracking, first, ensure that positioning is active.
Then, open the side dashboard and long-press on the layer where you want to save your tracks.

!![](../assets/images/tracking-layer-properties.png,350px)

### Resuming a Previous Session

If a tracking session was previously started but not explicitly stopped (for example, if the app was closed), QField provides the option to continue where you left off. A prompt will appear asking whether to **resume the last session** or **start a new one**.

- **Resuming** a session for a line or polygon layer will continue adding vertices to the feature from the previous session.
This allows you to seamlessly continue a single track across app restarts.

- **Starting a new session** will discard the incomplete feature from the previous session and begin a new one.

### Starting a New Session

If no previous session exists, or if you choose to start a new one, select the **Setup tracking** button to configure the session.

Two constraints are available to limit the number of vertices recorded during tracking:

- A minimum time interval

- A minimum distance

!![](../assets/images/tracking-settings.png,350px)

Once you have finished configuring the session, tap the **Start tracking** button to begin recording.
A feature form will appear, allowing you to define the attributes for the feature(s) being created.

For line and polygon layers, a single feature will be created per tracking session, with its geometry formed from the recorded positions.
For point layers, a new feature will be created for each recorded position, and the attribute values entered in the form will be remembered for subsequent points.

To prevent erroneous entries, you can set a maximum distance tolerance.
If the distance between the last and next tracked point/vertex exceeds this tolerance, the new position will be discarded.

!!! note
    QField will skip the feature form if the layer is configured to hide all attributes or if the form has been set to hide on feature addition in the attribute form settings.
    This can streamline the process of starting tracking sessions.

!!! note
    QField offers the capability to resume tracking sessions seamlessly, even if the application has been restarted or the device has been rebooted. This ensures continuity by allowing previously started tracking sessions to be reactivated without loss progress.

!![](../assets/images/maximum-distance-tolerance.png,350px)

## Tracking underway

Once a tracking session has been setup, a badge will appear in the side dashboard
legend next to the layer(s) against which tracking is being recorded.

!![](../assets/images/tracking-badge.png)

The features created by the tracking session are saved on every vertex recorded.
A rubberband line overlayed onto the map is attached to each tracking session,
allowing you to glance at what has been recorded.

If the layer linked to a tracking session supports the M dimension, QField will store
the time passed since the first vertex recorded in each vertex's M value.

!!! note
    You can simultanously record multiple trackings sessions across several layers.

!!! note
    While the tracking session is active the layer is still editable, but the tracked feature can't be edited or deleted until the tracking session is stopped over the legend again.

## Terminate tracking

To terminate tracking, simply open the side dashboard. From there, long-press
on a legend layer linked to an active tracking session and select the
*Stop tracking* button.

!![](../assets/images/tracking-stop.png)

## Predefined Project Tracking Sessions

This functionality enables one or more position tracking sessions to automatically start upon project load. Users will be presented with a feature form popup as the tracking session begins to fill in attributes. If the vector layer used to track has the "Hide Form on Add Feature" mode selected, the feature form will be skipped.

!![Hide Form on Added Feature](../assets/images/hide-form-on-add-feature.png)

### Configure a Project Tracking Session

:material-monitor: Desktop preparation

The configuration of a project tracking session happens in the vector layer properties dialog's QField panel. There, you can activate "Tracking Session" and specify the tracking requirements. Note that the QField panel is only available when the QFieldSync plugin is installed in your QGIS profile.

!![Activating automatic "Tracking Sessions" in QFieldSync](../assets/images/automatic-tracking-session.png)

!![Tracking activated automatically in QField](../assets/images/qfield-tracking-session.png,350px)

!!! note
    ### Benefits
    - **Efficiency**: Automation saves time and effort in the field.
    - **Flexibility**: Users can customize sessions and opt for automatic initiation with default values.
