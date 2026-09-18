---
title: All about GPS, GNSS and NTRIP
tx_slug: documentation_how-to_gnss
---

# Positioning (GNSS)

QField is capable to show your live position using several sources:

- Either by using the internal GNSS (Global Navigation Satellite System, like GPS, GLONASS, Galileo or Beidou) of your mobile device (typically 5 m accuracy) or
- Through an external antenna through NMEA streams over Bluetooth, TCP, or UDP connection. (typically 1.5 m accuracy) or
- Through an external antenna connected to an additional NTRIP service (down to cm accuracy)

!!! Tip

    Depending on your technical domain, it is advisable to make use of an external antenna, given that the known limitation of a mobile device is around 5 meters.
    Furthermore, an external antenna is also able to measure the altitude next to the current 2D position on the earth surface.

## Visualization

When positioning is enabled, your position will be shown in blue on the map.
Your location is represented by a <span style="color:blue"> :material-circle:</span> when you are not moving and by an <span style="color:blue"> :material-arrow-up:</span> indicating your movement direction if you are moving.
The blue beam indicates the current orientation of your device if the device has a builtin magnetic compass.
A shaded circle around your current position indicates the precision as reported by the GPS in use.
!![Position enabled](../../assets/images/position_icon.png,250px)

## Positioning Settings

!!! Workflow

    **To access the Positioning Settings**

    1. Open the **Side Dashboard** and click on the **3-dotted menu**
    2. Tap on **Settings** and switch to the *Positioning* tab

The following settings are available in QField settings' positioning tab.

- **[Enable NTRIP Corrections](#enable-ntrip-corrections):** QField can act as a RTK Client if you have the essential credentials to connect to your service.
- **Show position information:** If you want to see your location coordinates on the map canvas, you can enable this option.
- **Behavior when locked to position:** This setting allows you to set the preferred way of orienting the map canvas, when positioning is enabled:
    - <u>Follow position only:</u> The map canvas will stay as it is.
    - <u>Follow position and compass orientation:</u> The map canvas will rotate in such a way that your compass always points towards the top of your screen.
    - <u>Follow position and your movement direction:</u> The map will always rotate in the way of your movement direction.
- **Measure M Values:** If your layer contains an **M** Dimension, you can collect information on:
    - <u>Timestamp</u>
    - <u>Ground Speed</u>
    - <u>Bearing</u>
    - <u>Horizontal and Vertical Accuracy</u>
    - <u>PDOP,HDOP and VDOP</u>
- **Activate accuracy indicator:** When you activate this option, you can only take measurements when your set accuracy requirement has met.
The accuracy is indicated by a <span style="color:red"> :material-circle:</span>, <span style="color:orange"> :material-circle:</span> or <span style="color:green"> :material-circle:</span> on top of your crosshair.
!![](../../assets/images/gnss_accuracy_threshold_status.png, 200px)
- **Enable averaged positioning requirement:** You can average your position when enabling this option.
This means, that you define how many times you have to add a point before it is saved.
![type:video](../../assets/videos/positioning-averaged.mp4)
- **Antenna Correction:** If you are working with an antenna, you can add the height and QField will automatically subtract that value.
- [**Vertical Grid Shift:**](#altitude-correction--vertical-grid-shift): You can correct for the altitude if you have been given a vertical grid shift file so that QField can calculate the orthometric height.
!!! Note

    If the ***Enable accuracy requirement*** setting is activated, you will not be able to collect new measurements with the coordinate cursor locked to the current position with an accuracy value which is bad (red).

## Using an external GNSS Receiver

QField supports connecting to external GNSS positioning devices via NMEA streams through Bluetooth, TCP,
or UDP connections.

Under the **Positioning Settings**, you are able to manage and switch between your internal and saved external GNSS devices.

!![](../../assets/images/saved-gnss-devices.png)

The breakdown of connections support by platform is as follow:

|             | :material-android: Android | :material-apple: iOS | :material-microsoft-windows: Windows | :material-linux: Linux | :material-apple: MacOS |
|-------------|----------------------------|----------------------|--------------------------------------|------------------------|------------------------|
| Bluetooth   | :material-check:           | :material-check:     |                                      | :material-check:       | :material-check:       |
| TCP         | :material-check:           | :material-check:     | :material-check:                     | :material-check:       | :material-check:       |
| UDP         | :material-check:           | :material-check:     | :material-check:                     | :material-check:       | :material-check:       |
| Serial port | :material-check:           |                      | :material-check:                     | :material-check:       | :material-check:       |

*(\*) Bluetooth support on Windows occurs through the virtual serial port automatically
created by the operating system when it connects to the GNSS device.*

The NMEA sentences currently supported are GGA, RMC, GSA, GSV, GST, VTG, HDG and HDT.

!!! note
    Make sure no other app like mock location providers are using the same connection.

### External receiver log

If you have selected an external receiver as the positioning device, you will find a switch `Log NMEA sentences from device to file`.
If this is activated, all NMEA sentences coming from external positioning devices will be logged to a file.

The logs will be placed in **[[App Directory](../../how-to/project-setup/storage.md#5-qfield-app-directory)]/QField/logs**.

!![](../../assets/images/external_receiver_log.png,250px)

!!! note
    Be aware that if the log is always turned on, it will fill up all the storage.

## Enable NTRIP Corrections

If you have access to an  RTK Service, QField can act as a RTK Client if you add the essential information under the settings.

!!! Workflow

    **Connect to external GPS Device**

    1. Enable bluetooth and connect to your external GPS Device
    2. In QField connect to that antenna by adding it to your selection of positioning devices.
    3. Once connected, toggle the switch.
    !![](../../assets/images/GNSS_NTRIP_configuration.png, 300px)
    4. Click on the settings button next to the switch and add your NTRIP Service information.
    !![NTRIP Settings](../../assets/images/GNSS_NTRIP_configuration_settings.png, 300px)
    5. Once added click on the arrow and ensure that the NTRIP correction is working as expected (indicated by incoming and outgoing arrows).
    !![RTK connected](../../assets/images/GNSS_NTRIP_configuration_inuse.png, 300px)

    **NOTE**: If you enable your position information in the settings you can see the established connection.

## Antenna height compensation

The height of the antenna pole in use can be defined in the settings.
Any measured altitude will be corrected by this value.

## Altitude correction / vertical grid shift

Altitude values can be corrected with vertical grid shift files to calculate orthometric height.

You have to copy the **vertical grid shift files** to your QField app folder **[[App Directory]](../../how-to/project-setup/storage.md#5-qfield-app-directory)/QField/proj**. Once it is placed there, it will be available in QField in the **Positioning settings** under the dropdown menu **Vertical grid shift in use**.

The formats currently supported are:

- GeoTIFF (.tif, .tiff)
- NOAA Vertical Datum (.gtx)
- NTv2 Datum Grid Shift (.gsb)
- Natural Resources Canada's Geoid (.byn)

!!! Workflow

    1. Copy the `vertical shift grid` file to the directory **[[App Directory]](../../how-to/project-setup/storage.md#5-qfield-app-directory)/QField/proj** on your mobile device.

    2. Open the **Site Dashboard**
    3. Tap on the **3-dotted menu *(⋮)** and direct to *Settings* > *Positioning*
        !![](../../assets/images/vertical_grid_selection_in_qfield_settings.png,450px)
    4. Enable your GNSS device.
    It will directly center to your current location once the **positioning information** is available.

    5. Change to **Digitize Mode** and press on the **Crosshair** - the cross in the center means it is using GNSS positioning.
        ![type:video](../../assets/videos/gnss_use.mp4)

    6. Long-press on the **Crosshair** to open the **Position Settings Menu**.
        Inside the menu you can turn on the **Show position information** which will show the current coordinates that are reprojected into the CRS of your project along with the precision information.
        !![](../../assets/images/positioning-menu.png,700px)


    !!! note
        If you see WGS 84 lat/lon information instead of information in your project CRS, you probably have no signal yet.

## Positioning variables

You can get the positioning information both of your internal and external device by specifically configuring your attribute form.

Have a look [here](../../how-to/navigation-and-positioning/gnss.md#positioning-variables) if you want to know how this is configured in QGIS.

## Mock location
:material-tablet: Fieldwork

It is possible to provide a mock location via a separate android app to
QField. There are several options for this, one of them is [Android NTRIP Client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient).

To use this you have to [enable mock locations on your Android device](https://www.youtube.com/watch?v=v1eRHmMiRJQ).
