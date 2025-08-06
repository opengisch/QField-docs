---
title: Positioning (GNSS)
tx_slug: documentation_how-to_gnss
---

# Positioning (GNSS)

QField can make use of the internal GNSS (Global Navigation Satellite
System, like GPS, GLONASS, Galileo or Beidou). QField can also connect
to external antennas through NMEA streams over Bluetooth, TCP, or UDP
connection.

GNSS devices are also capable of measuring the altitude next to the current 2D
position on the earth surface.

## Visualization

When positioning is activated, your position will be shown in blue on the map.
Your location is visible either as a blue dot if you are still or as an arrow indicating your movement direction
if you are moving.

The blue beam indicates the current orientation of your device if the device has
a builtin magnetic compass.

A circle around your current position indicates the precision as reported by the
positioning device.

## Configuration

The following settings are available in QField settings' positioning tab.

### Measure (M) value

When digitizing a geometry onto a vector layer that contains an M dimension,
QField will add a measurement value to individual vertices whenever the
coordinate cursor is locked to the current position.

By default, the value will represent the captured position's timestamp (milliseconds
since epoch). You can change this value using the combo box in the settings'
positioning tab.

The available values to chose from are timestamp, ground speed, bearing, horizontal
accuracy and vertical accuracy as well as PDOP, HDOP and VDOP.

### Accuracy requirement

A minimum desired accuracy for measurements can be defined. The quality
will be reported in three classes, bad (red), ok (yellow) and excellent
(green). These colors will show up as a dot on top of the GNSS button.

The thresholds can be defined in the settings' positioning tab.

If the *Enable accuracy requirement* setting is activated, you will not
be able to collect new measurements with the coordinate cursor locked to
the current position with an accuracy value which is bad (red).

### Antenna height compensation

The height of the antenna pole in use can be defined in the settings.
Any measured altitude will be corrected by this value.

### Altitude correction / vertical grid shift

Altitude values can be corrected with vertical grid shift files to
calculate orthometric height.

Vertical grid shift files have to be made available to QField by putting
them into the QField app folder `[App Directory]/QField/proj`.

Once the grid shift file is placed there, it is available in QField in
the *Positioning settings* under *Vertical grid shift in use*.

If you are using altitude correction and an external positioning device
is used, consider turning *Use orthometric altitude from device* off.

The formats currently supported are:

  - GeoTIFF (.tif, .tiff)
  - NOAA Vertical Datum (.gtx)
  - NTv2 Datum Grid Shift (.gsb)
  - Natural Resources Canada's Geoid (.byn)

For example:

### **Netherlands: ETRS89 to NAP**

For transformations involving the Dutch **NAP (Normaal Amsterdams Peil)** vertical datum, you'll need the official grid file from NSGI.

1. **Download the file**: Get `nlgeo2018.gtx` directly from the [NSGI website](https://www.nsgi.nl/rdnaptrans).<!-- markdown-link-check-disable-line -->

2. Place the downloaded `.gtx` file into the directory `[App Directory]/QField/proj`.

### **Switzerland: CH1903+/LV95**

To get precise altitude data for **Cadastral Surveying in Switzerland (LV95)**, you must use a geoid correction grid from Swisstopo. The official file comes in an `.agr` format and must be converted to `.gtx` before it can be used.

#### **Step 1: Download the Geoid Grid**

First, download the "Geoid OGD" dataset from Swisstopo.

- **Download Link**: [Geoid OGD from Swisstopo](https://cms.geo.admin.ch/ogd/geodesy/Geoid_OGD.zip)<!-- markdown-link-check-disable-line -->

Once you unzip the archive, you will find the required file: `chgeo2004_htrans_LV95.agr`.

#### **Step 2: Convert the `.agr` file**

You can easily convert the file format using the [gdal_translate](https://gdal.org/en/stable/programs/gdal_translate.html) algorithm from the GDAL library, which is included with QGIS.
The target format is typically `.gtx` (NTv2 Grid Shift File), but you can also convert to other raster formats like GeoTIFF (.tiff).

##### **Method 1: QGIS Graphical User Interface (GUI)**

1. In QGIS, open the Processing Toolbox panel.

2. Navigate to **GDAL** > **Raster conversion** and double-click the **Translate (Convert format)** tool.

3. Configure it with your needed requirements:

    - **Input layer**: Select your `chgeo2004_htrans_LV95.agr` file.

    - **Output file**: Click "Save to File..." and name your output file with a `.gtx` extension (or other format needed), for example, `chgeo2004_htrans_LV95.gtx`.

4. Click **Run**. The other default settings are typically sufficient for this conversion.

!![](../assets/images/qgis_core_translate_convert_format.png)

##### **Method 2: Command Line (`qgis_process`)**

For automation or users who prefer the command line, `qgis_process` is a great option.
Open your terminal and run the following command, adjusting the paths to your files.

```bash
qgis_process run gdal:translate --INPUT="/path/to/your/chgeo2004_htrans_LV95.agr" --OUTPUT="/path/to/your/chgeo2004_htrans_LV95.gtx"
```

##### **Method 3: PyQGIS Script**

You can also perform the conversion programmatically within the QGIS Python Console or a standalone script.

```Python
import processing

input_grid = '/path/to/your/chgeo2004_htrans_LV95.agr'
output_grid = '/path/to/your/chgeo2004_htrans_LV95.gtx'

processing.run("gdal:translate", {
    'INPUT': input_grid,
    'OUTPUT': output_grid
})

print(f"Successfully converted grid to: {output_grid}")
```

#### **Configure the Application**

After converting the `.agr` file:

1. Move your new `chgeo2004_htrans_LV95.gtx` file to the directory `[App Directory]/QField/proj`.

2. In your application's settings, select the file as the vertical grid shift correction file.

!![](../assets/images/vertical_grid_selection_in_qfield_settings.png,450px)

## Usage
:material-tablet: Fieldwork

A short press on the *GNSS button* will turn on the GNSS and center to the
current location once *positioning information* is available.

Activate *edit mode* and press on the target button, the cross in the
center means it is using GNSS positioning.

!![](../assets/images/gnss_use.webp,250px)

A long press on the *GNSS button* will show the *positioning menu*.

Inside the *positioning menu* you can turn on the *Show position information*
which will show the current coordinates which are reprojected into the
project CRS along with precision information.

!![](../assets/images/positioning-menu.png)

!!! note
    If you see WGS 84 lat/lon information instead of information in your
    project CRS, you probably have no signal yet.

## Using an external GNSS Receiver
:material-tablet: Fieldwork

QField supports connecting to external GNSS positioning devices via NMEA streams through Bluetooth, TCP,
or UDP connections.

In *Settings > Positioning*, you can find a set of buttons to add, edit, or delete external
devices as well as a dropdown list to switch between internal and saved external GNSS devices.

!![](../assets/images/saved-gnss-devices.png)

The breakdown of connections support by platform is as follow:

|             | :material-android: Android | :material-apple: iOS | :material-microsoft-windows: Windows | :material-linux: Linux | :material-apple: MacOS |
|-------------|----------------------------|----------------------|--------------------------------------|------------------------|------------------------|
| Bluetooth   | :material-check:           |                      | *                                    | :material-check:       | :material-check:       |
| TCP         | :material-check:           | :material-check:     | :material-check:                     | :material-check:       | :material-check:       |
| UDP         | :material-check:           | :material-check:     | :material-check:                     | :material-check:       | :material-check:       |
| Serial port | :material-check:           |                      | :material-check:                     | :material-check:       | :material-check:       |

*(\*) Bluetooth support on Windows occurs through the virtual serial port automatically
created by the operating system when it connects to the GNSS device.*

The NMEA sentences currently supported are GGA, RMC, GSA, GSV, GST, VTG, HDG and HDT.

!!! note
    Make sure no other app like mock location providers are using the same connection.

### External receiver log

In *Settings > Positioning* if you have selected an external receiver as the positioning device, you will find a switch `Log NMEA sentences from device to file`. If this is activated, all NMEA sentences coming from external positioning devices will be logged to a file.

The logs will be placed in *Android/data/ch.opengis.qfield/files/QField/logs*.

!![](../assets/images/external_receiver_log.png,250px)

!!! note
    Be aware that if the log is always turned on, it will fill up all the storage.


## Mock location
:material-tablet: Fieldwork

It is possible to provide a mock location via a separate android app to
QField. There are several options for this, one of them is [Android NTRIP Client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient).

To use this you have to [enable mock locations on your Android device](https://www.youtube.com/watch?v=v1eRHmMiRJQ).

## Averaged positioning functionality
:material-tablet: Fieldwork

!!! note
    The coordinate cursor must be locked to the current location via the [Lock to position button](./digitize.md#adding-point-features)

There is a function that allows you to digitize using averaged positions.

The survey will start by pressing and holding the add vertex button, which will start collecting positions.

While collecting, an indicator will appear on top of the coordinate cursor showing a text reflecting the current number of collected positions.
If an averaged position minimum count requirement is active, a progress bar will also be present indicating the progress towards meeting that requirement.

!![](../assets/images/positioning-averaged.webp,280px)

The setting to activate an average position minimum count threshold can be found in QField settings's *positioning* panel.
When active, holding the add vertex button is not required, a short tap on the button will begin the collection of positions and automatically add the averaged position when the minimum count requirement is met.

!![](../assets/images/positioning_averaged_set.png,280px)

When using [`@gnss_*` or `@position_` variables](./gnss.md#positioning-variables) on averaged positions, the variable will also represent the average over all collected samples.


## Project configuration
:material-monitor: Desktop preparation

### Positioning variables

You can get access to positioning information through additional
expression variables accessible in the attribute form. These will
only be available when positioning is enabled.

These variables are commonly used as part of [default values expressions](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html#default-values)<!-- markdown-link-check-disable-line -->
for fields to keep track of the quality of individual measured points.

A common use case is recording the horizontal accuracy, which can be done by using the variable `@position_horizontal_accuracy`.
Another often used strategy is using the altitude of the current measurement which can be achieved with `z(@position_coordinate)`.
For a complete listing of all available variables, refer to the [expression variables reference documentation](../reference/expression_variables.md).

Information for GNSS Z value with Vertical grid shift in use:
- *Antenna height compensation=False*

| Vertical Grid Shift in use | point Z Value z(geometry) | GNSS Device z(@position_coordinate) | QField Display | QField Label                |
|----------------------------|---------------------------|--------------------------------------|----------------|-----------------------------|
| None                       | Z ellipsoidal device value| Z ellipsoidal device value           | Z ellipsoidal device value | Altitude: xxx.xxxx m       |
| Orthometric from device    | Z orthometric device value| Z orthometric device value           | Z orthometric device value | Altitude: xxx.xxxx m (ortho.) |
| USER_Shift_Grid.GTX <br> [vertical grid shift](#altitude-correction-vertical-grid-shift)        | Z shiftgrid value         | Z ellipsoidal device value           | Z shiftgrid value          | Altitude: xxx.xxxx m (grid) |

### Vertex logger

It is possible to setup a log layer of the collected vertices. This
allows to keep track of meta data for each vertex like GNSS quality
attributes and more. To set this up, a point layer can be added to the
project and attributes configured to store this information.

![](../assets/images/vertex_log1.png){width="600px"}

Then you should assign the role *digitizing logger* to a point layer.

Go to *QFieldSync > Project Properties*

![](../assets/images/vertex_log2.png){width="600px"}

To be most effective, the layer attributes should have default values that
relies on the positioning variables enumerated above.
