---
title: Expression Variables
tx_slug: documentation_reference_expression_variables
---

# Expression Variables in QField

QField supports various expression variables that can be used as field defaults, constraints or also to control the visibility of your attribute forms.
These include not only all the expression variables available in QGIS but also additional variables provided by QField to access positioning information and give explicit information about the QFieldCloud data.

## QFieldCloud

For QFieldCloud users, two expression variables can be used in forms or default values:

- `@cloud_username` - Returns the name of the currently logged-in QFieldCloud user.
- `@cloud_useremail` - Returns the email address of the currently logged-in QFieldCloud user.

## Positioning and GNSS Variables

Accurate positioning information can be relevant in a lot of contexts.
When your location is activated, the specific variables will populate the pre-configured fields.
These variables are commonly used in default values expressions to track the quality and details of individual measured points.

In case you are connecting to an external positioning device, it is possible to interchange the `@position_*` variable with the `@gnss_*` variable to directly connect its position instead.

!!! Watch out
  Make sure that your positioning is enabled, otherwise the fields will not be populated.

### List of Positioning and GNSS Variables

**Note**: in order for the positioning variable to be available is when the crosshair is snapped to the sensor.
#### Most regular ones

- `@position_source_name` - The name of the device providing the location information, as reported by the sensor.
If the position is manually set and not snapped to the cursor, the source name is "manual".
- `@position_quality_description` - A human-readable and translated description of the quality as reported by the sensor (e.g., "Fixed RTK").
- `@position_coordinate` - A point containing the WGS84 coordinate (longitude, latitude, altitude) as delivered by the sensor.
- `@position_horizontal_accuracy` - The horizontal accuracy of the coordinate (in meters), as reported by the sensor.
- `@position_timestamp` - The timestamp of the position in UTC, as reported by the sensor.

- `@position_direction` - The direction of movement in degrees from true north, as reported by the sensor.

- `@position_orientation` - The orientation of the device itself, regardless of its movement, relative to true north (from 0° to 359°).
- `@position_ground_speed` - Groundspeed (in m/s), as reported by the sensor.

- `@position_magnetic_variation` - The angle between the magnetic field's horizontal component and true north (magnetic declination). A positive value indicates a clockwise direction from true north; a negative value indicates counter-clockwise.
- `@position_vertical_accuracy` - The vertical accuracy of the coordinate (in meters), as reported by the sensor.

- `@position_3d_accuracy` - The three-dimensional accuracy of the coordinate (in meters), as reported by the sensor.

- `@position_vertical_speed` - The vertical speed (in m/s), as reported by the sensor.
- `@position_averaged_count` - The number of collected positions from which an averaged position was calculated. If not averaged, the value is `0` (zero).
- `@position_pdop` - Position dilution of precision, as reported by the sensor.
- `@position_hdop` - Horizontal dilution of precision, as reported by the sensor.
- `@position_vdop` - Vertical dilution of precision, as reported by the sensor.
- `@position_number_of_used_satellites` - The number of satellites used by the sensor.

- `@position_used_satellites` - A list of satellites in use (PRI), as reported by the sensor.

- `@position_fix_status_description` - The GPS fix status ("NoData", "NoFix", "Fix2D", or "Fix3D"), as reported by the sensor.

- `@position_fix_mode` - The fix mode ("M" = Manual, "A" = Automatic), as reported by the sensor.

- `@position_imu_correction` - Returns true of the position information was improved by an IMU device.

- `@position_imu_roll` - The roll value of an active IMU device providing positioning corrections.
- `@position_imu_pitch` - The pitch value of an active IMU device providing positioning corrections.
- `@position_imu_heading` - The heading value of an active IMU device providing positioning corrections.
- `@position_imu_steering` - The steering value of an active IMU device providing positioning corrections.

!!! info
    - I: Internal position source, E: External (NMEA) position source.
    - Variables containing `satellites` are not available on iOS.

!!! note
    The `gnss_*` variables always report the GNSS sensor values, even when the crosshair is not snapped.
    - When the crosshair is snapped to the sensor:
      - `@gnss_horizontal_accuracy` > Reports the sensor's horizontal accuracy (in meters).
      - `@position_horizontal_accuracy` > Reports the same value as the corresponding `gnss` value.
      - `@position_source_name` > Reports the sensor name.
    - When the crosshair is manually moved:
      - `@gnss_horizontal_accuracy` > Reports the sensor's horizontal accuracy (in meters).
      - `@position_horizontal_accuracy` > The value is `NULL`.
      - `@position_source_name` > The value is `manual`.
