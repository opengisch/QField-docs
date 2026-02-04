---
title: EXIF Data
tx_slug: documentation_reference_exif
---

# EXIF Data in QField

When using the internal QField camera, images will be geotagged with various EXIF metadata fields. Below is a reference table listing the available EXIF tags, their descriptions, examples, and comments about their usage in QField.

| EXIF Tag                            | Description                                                           | Example                   | Comments                                       |
|-------------------------------------|-----------------------------------------------------------------------|---------------------------|------------------------------------------------|
| Exif.GPSInfo.GPSLatitude            | The latitude of the location where the image was taken.                | 47.3769                    | Stored as a positive value with a reference to N/S (see below). |
| Exif.GPSInfo.GPSLatitudeRef         | Latitude reference (N = North, S = South).                            | N                          | Determines whether the latitude is north or south of the equator. |
| Exif.GPSInfo.GPSLongitude           | The longitude of the location where the image was taken.               | 8.5417                     | Stored as a positive value with a reference to E/W (see below). |
| Exif.GPSInfo.GPSLongitudeRef        | Longitude reference (E = East, W = West).                             | E                          | Determines whether the longitude is east or west of the prime meridian. |
| Exif.GPSInfo.GPSAltitude            | The altitude above sea level (in meters) where the image was taken.    | 490                        | Positive values indicate above sea level; negative values indicate below. |
| Exif.GPSInfo.GPSAltitudeRef         | Altitude reference (0 = Below Sea Level, 1 = Above Sea Level).         | 1                          | Indicates whether altitude is above or below sea level. |
| Exif.GPSInfo.GPSImgDirection        | The direction in degrees in which the camera was facing when the image was taken. | 270                        | Represents the compass direction (0 = North, 90 = East, 180 = South, 270 = West) relative to magnetic north. |
| Exif.GPSInfo.GPSImgDirectionRef     | Direction reference (M = Magnetic North).                             | M                          | Specifies whether the direction is relative to magnetic north. |
| Exif.GPSInfo.GPSSpeed               | The speed of the device when the image was taken, in kilometers per hour (km/h). | 30.5                       | Captured if the device is moving at the time of image capture. |
| Exif.GPSInfo.GPSSpeedRef            | Speed unit (K = kilometers per hour).                                 | K                          | Currently, speed is recorded in kilometers per hour in QField. |
| Exif.GPSInfo.GPSDateStamp           | The date the image was captured in UTC.                               | 2024:10:06                 | Date stored in the format YYYY:MM:DD. |
| Exif.GPSInfo.GPSTimeStamp           | The time the image was captured in UTC.                               | 14:23:56                   | Time stored in the format HH:MM:SS. |
| Exif.GPSInfo.GPSSatellites          | The number of satellites used for GPS information.                    | 12                         | Number of GPS satellites that contributed to location accuracy. |
| Exif.Image.Make                     | The make of the device that captured the image.                       | QField                     | Always set to "QField" to indicate the software used. |
| Xmp.tiff.Make                       | XMP tag for the device make, also set to QField.                      | QField                     | Similar to Exif.Image.Make, used for compatibility in XMP metadata. |

## Notes

- QField captures and stores EXIF metadata automatically when using the internal (i.e. not the native) camera.
- The coordinates (latitude and longitude) are always stored as absolute values, with the hemisphere indicated by the corresponding reference tags (e.g., `GPSLatitudeRef` for N/S).
- Altitude is recorded as a positive or negative value depending on whether the elevation is above or below sea level, with `GPSAltitudeRef` used to indicate the direction.
- Date and time stamps are stored in UTC format for consistency across locations.
- See the corresponding [how to fetch geotag exif information into the attribute table section](https://docs.qgis.org/latest/en/docs/user_manual/expressions/functions_list.html#exif) for instructions how to make use of this. <!-- markdown-link-check-disable-line -->
