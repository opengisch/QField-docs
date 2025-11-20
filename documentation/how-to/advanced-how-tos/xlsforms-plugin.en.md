---
title: XLSForm Converter
tx_slug: documentation_xlsforms_plugin
---

# XLSForm Converter Plugin for QGIS

Use the **XLSForm Converter** plugin to convert existing XLSForms into QGIS projects.
This tool migrates all configurations from your form into a configured project alongside a geopackage containing your survey layers. The plugin allows you to upload the result directly to QFieldCloud provided you have installed QFieldSync. Once converted, the resulting project is ready to be loaded into QField for use in the field.

## XLSForms

XLSForms is a standard used by several survey products such as [ODK](https://getodk.org/) or [KoboToolbox](https://www.kobotoolbox.org/).
XLSForms is built on a spreadsheet format using Excel as the standard.
In simple terms a survey is made up of several "Questions" that can be presented in different formats (integer, text, lists etc.).
To learn more about the standard please visit [More about XLSForms](https://xlsform.org/en/)

## How to install the plugin

You can install the XLSForm Converter in QGIS through its plugin manager.

!!! Workflow

    1. Direct to *Plugins* > *Manage and Install Plugins* > *All*
    2. Search for XLSForm Converter and click "Install Plugin".

        !![XLSForm Converter Plugin](../../assets/images/xlsform-plugin-interface.png,500px)

     Once it is installed it will appear in your processing box
        !![Processing](../../assets/images/xlsform-processing.png,300px)

## Convert XLSForm to QGIS Project

To convert an XLSForm you need to make sure you follow the standards and format of the original XLSForm.
Here is a [template](https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko/edit?gid=1052905058#gid=1052905058), you can adapt in case you are more familiar with XLSForms than QGIS.

!!! Workflow

    1. In QGIS Open the "Convert XLSForm to QGIS project" process from your Processing Toolbox.
    2. Find the XLSForm in your file directory.
    2. (Optional) In case you want to assign a specific name or a specific language to your project, fill in the dedicated fields.
        !![XLS Converter Process Interface](../../assets/images/xlsform-processing-windows.png,800px)
    3. Select your preferred basemap:
         - OpenStreetMap
         - Humanitarian OpenStreetMap Team (HOT)
    4. (Optional) You can directly turn your project into a QFieldCloud project if you check the according checkbox.
    5. (Optional) Under **Advanced Parameters** you can further customize the settings of your project:
         - Set your desired project extent
         - Define a preferred coordinate reference system.
        **Note**: By default the WGS 84: Pseudo Transmercator (EPSG:3857) will be used.
         - "Pre-fill project with features' geometries and matching attributes" allows you to take an existing feature with the **exact** table names and add it to the project by default.
    6. Choose the location of where your project is stored.
    7. Click "Run" and wait.
    In case successful, the new project will be saved in your selected project folder.

## More Information

If you want to know about what is all possible with the XLS-Forms Converter Plugins and what it has been used for, have a look at the resources below:

- [XLS Converter Plugin Source Code](https://github.com/opengisch/XLSFormConverter)
- [OPENGIS.ch Blog Post](https://www.opengis.ch/2025/06/02/xlsform-converter-unlock-a-world-of-surveys-with-our-brand-new-qgis-plugin/)
