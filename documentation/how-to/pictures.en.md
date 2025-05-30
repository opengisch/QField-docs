---
title: Pictures
tx_slug: documentation_how-to_pictures
---

# Use attachment

In QField, a field with *Attachment* widget can be used to:

-   show and take photos
-   show and record videos
-   listen and record sound clips
-   show links to external files like PDFs or documents

!![Attachments](../assets/images/attachments.png "")

To configure the Widget, please refer to the [Attributes Form Documentation](./attributes-form.md#configure-attachmentpictures-widget)

## Add a series of pictures to a feature
:material-monitor: Desktop preparation

One or more pictures can be added to the feature.
Here is an example of how to proceed.

### Tables
It is necessary to set up two tables.
One table where the features are stored and one with a list of pictures.

#### Apiary
| Field      | Type       |
|------------|------------|
| `id`       | Text (UUID)|
| `geometry` | Geometry   |
| `...`      |            |

#### Apiary_pictures
| Field       | Type       |
|-------------|------------|
| `id`        | Text (UUID)|
| `apiary_id` | Text (UUID)|
| `path`      | Text       |
| `...`       |            |

### Relations
Create a relation with:

-   `apiary` Referenced layer
-   `id` Referenced field
-   `apiary_picture` Referencing layer
-   `apiary_id` Referencing field
-   `strength` Composition

!![Relations](../assets/images/add-1-n-pictures-relations.png "")

### Widgets

#### Apiary
Set the default value of the field id to `uuid()` or use the *UUID Generator* widget.
There is no need to show it in the form.

!![widgets](../assets/images/add-1-n-pictures-widgets_hive.png "")

Set the relation widget to *many to one relation* and add the relation to the form

!![widgets](../assets/images/add-1-n-pictures-widgets_hive2.png "")

#### Apiary picture
Set the widget type of the field path to *Attachment* and add it to the form

!![widgets](../assets/images/add-1-n-pictures-widgets_picture.png "")

## Drawing and sketching

QField has an in-app drawing and sketching functionality enabling you to directly sketch over and annotate images captured while in the field as well as drawing on top of a blank canvas or over a template.

![type:video](../assets/videos/drawing-sketch-feature2.webm)

### Drawing templates

On top of annotating captured images, QField supports drawing from image templates.
The following two methods are available to add templates:

- The first method is to create a `drawing_templates` folder located alongside a project file and populate it with images.
Whenever that project is loaded, QField will register all images within that folder as drawing templates.
- Alternatively, you can add images into the `drawing_templates` folder found inside your QField app folder.
If you are not familiar with that app folder, its location is shown at the bottom of the About QField overlay.

Templates shipped alongside projects as well as the QField app folder will be shown when users choose 'Draw a sketch' within attachments widget's 3-dot menu.

!![picture path](../assets/images/drawing_templates.png "")

## Geotagging
:material-tablet: Fieldwork

QField's internal camera will automatically geotag your pictures.

Information about location and direction of the pictures will therefore be baked into the image file.

!!! note
    While with older Android versions it was possible to use other apps like the amazing OpenCamera app for taking pictures and preserving EXIF information from there, this is no longer with recent Android versions.
    Is recommended to disable  *Use native Camera* in the *settings* to preserve [EXIF](../reference/exif.md) information.

## Fetching Geotags (EXIF) from the image file into the attribute table
:material-monitor: Desktop preparation

Sometimes you might be interested in automatically storing Geotags such as the latitude, longitude, orientation, etc.
This information is also known as EXIF tags.

To store the EXIF information, follow these steps:

1.  Add an attribute per EXIF tag in the table that contains the pictures.
2.  In the pictures form, configure the default value of each attribute to the corresponding
   *EXIF* expression [See QGIS EXIF function](https://docs.qgis.org/3.34/en/docs/user_manual/expressions/functions_list.html#exif),
    and make sure *Apply on update* is activated.
4.  The EXIF tags that QField can capture are listed in the QGIS documentation (link above).
    However, this list might slightly vary depending on the mobile characteristics.
5.  Capturing EXIF tags requires accessing the full physical path of the picture.
Be sure to reflect this in the QGIS expression.
   For example, the expression `exif(@project_folder + '/' + "path", 'Exif.Image.Orientation')` retrieves the orientation of the picture stored in *path*.
   For more tags visit the [QField EXIF reference documentation](../reference/exif.md) and the [exiv library documentation](https://exiv2.org/tags.html).
6.  Completed! QField now captures and stores the EXIF tags in the pictures table while taking pictures.

## Maximum picture size
:material-monitor: Desktop preparation

The advanced settings allow rescaling the photos to a maximum width/height in *QFieldSync plugin > Project configuration*

![image](https://user-images.githubusercontent.com/4992805/189456560-3e251c44-c85c-40bd-a3cc-039c49090e03.png)

## Configurable attachment path
:material-monitor: Desktop preparation

QFieldSync provides the possibility to configure the path and the file names of picture attachments.

1.  Go to *Layer Properties > QFieldSync plugin *
2.  Choose the layer, the field and configure the expression

Use expressions to specify the path of the attachments.
By default, pictures are saved into the "DCIM" folder, audio are saved into the "audio" folder and videos are saved into "video" with a timestamp as name.

!![picture path](../assets/images/picture_path.png "")

Additional directories can be synchronized with pictures or other attachments.
Extra paths can be configured in _Attachment directories_ in the QFieldSync settings under *project properties*.
All paths are relative to the project directory.

!![attachments directories](../assets/images/attachments_directories.png "")
