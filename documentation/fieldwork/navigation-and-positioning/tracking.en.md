---
title: Tracking
tx_slug: documentation_how-to_tracking
---

# Tracking

## Activate Tracking

You can track yourself and collect points, lines or polygons while browsing the map, working on other features and layers, or in the background while having the device in your pocket.
For lines and polygons, one object will be created per tracking session.
For points, a new object will be created for each recorded position.
The attributes you enter in the beginning of the trackking sessions will be added to every object recorded.

!!! Note

    To enable tracking, you need to ensure that your positioning is activated.

You can choose between two options for the recording interval of vertices during the tracking session:

- **Time Requirements:** This option records your position at a regular rate (e.g., every 30 seconds), which is ideal for consistent logs and saving battery.
- **Distance requirement:** This option records a new vertex or feature only after you move a minimum distance.
This keeps your track clean by ignoring movement when you are stationary.
!![](../../assets/images/tracking-settings.png,350px)

!!! Workflow

    **Option 1: Through the Side Dashboard Panel**

    1. Open the Side Dashboard Panel and long-press on the layer which you want to use for tracking.
    2. Tap **Setup tracking** and a new window will appear showing the configuration settings.

        !![](../../assets/images/tracking-layer-properties.png)

    3. Tap the **Start tracking** button to begin the tracking.
    4. Enter the attributes for the feature(s) about to be created and tap the :material-check:.
    Once a tracking session is set up, a badge :material-head: appears in the **Side Dashboard** next to the tracked layers.
    !![](../../assets/images/tracking-badge.png)
    During a tracking session, a rubberband line appears on the map to visualize the recorded path.
    5. Once finished open the **Side Dashboard** and long-press on the layer's tracking badge you want to stop.
    6. Tap **Stop tracking** to finish the session.


    !![](../../assets/images/tracking-stop.png)

    **Option 2: Through the Location Pie Menu**

    1. Tap on your position on the map
    2. A **pie menu** will open around your position.

        !![](../../assets/images/pie-menu-tracking.png,250px)

    3. Choose the **Tracking** icon (small walking figure).
    4. Enter the attributes for the feature(s) about to be created and tap the :material-check:.

## General and Additional Settings

There are additional settings which you can activate.

- **Sensor data requirement:** In case that you are working with a sensor, you can toggle this option and record a point/vertex anytime when a new sensor reading is being recorded
- **Erroneous distance safeguard:** If exact positioning is important to you, you can enable this option and set a maximum distance between two vertices so that bad GNSS readings are not tracked.
!![](../../assets/images/maximum-distance-tolerance.png,350px)
- **Measure(M) value attached to vertices:** If your layer supports the M dimension, QField can store the time passed since the first vertex recorded in each vertex's M value.

!!! tip
    You can simultaneously record multiple trackings sessions across several layers.

## Resume to a Previous Session

If you did not explicitly terminate your tracking session (for example, you closed the app), QField allows you to continue where you left off.
A prompt will appear asking whether to **resume the last session** or **start a new one**.

- **Resuming:** A session for a line or polygon layer will continue adding vertices to the feature from the previous session.
This allows you to simply continue across app restarts.

- **Starting a new session:** This option will discard the incomplete feature from the previous session and begin a new one.

## Automatic Tracking Session

If your project was configured in such a way, tracking will automatically start when you open the project.
You should see this in the **Side Dashboard**.
