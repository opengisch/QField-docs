---
title: XLSForm Converter
tx_slug: documentation_xlsforms_plugin
---

# XLSForm Converter Plugin for QGIS

The **XLSForm Converter** plugin converts existing XLSForm spreadsheets into fully configured QGIS project files and GeoPackage databases.
It migrates survey question structures, logic, and choice lists directly into QGIS layer attribute forms.
When installed alongside QFieldSync, the plugin allows uploading converted projects directly to QFieldCloud for mobile field deployment.

## XLSForms

XLSForm is a digital form standard used by field survey platforms such as [ODK](https://getodk.org/) and [KoboToolbox](https://kobotoolbox.org/).
XLSForm uses Excel spreadsheets (`.xlsx`, `.xls`, or `.ods`) to define survey questions, logic, and choice lists across standard data types (such as integers, text, select lists, and geometries).
Read more on the official [XLSForm Reference Website](https://xlsform.org/).

## Installing the Plugin
:material-monitor: Desktop preparation

Install the XLSForm Converter plugin using the QGIS Plugin Manager.

!!! Workflow
    1. In QGIS, navigate to _Plugins > Manage and Install Plugins..._.
    2. Select the **"All"** tab and search for **"XLSForm Converter"**.
    3. Click **"Install Plugin"**.

!![XLSForm Converter Plugin](../../assets/images/xlsform-plugin-interface.png,500px)

Once installed, the **"Convert XLSForm to QGIS project"** algorithm appears in the QGIS Processing Toolbox under the **"XLSForm"** group.

!![Processing](../../assets/images/xlsform-processing.png,300px)

## Convert XLSForms to QGIS Projects
:material-monitor: Desktop preparation

Convert an XLSForm spreadsheet into a QGIS project file (`.qgz`) and GeoPackage database.
Refer to this [Google Sheets Template](https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko/edit?gid=1052905058#gid=1052905058) for standard XLSForm structures.

!!! Workflow
    1. Open the Processing Toolbox in QGIS (_Processing > Toolbox_).
    2. Double-click **"Convert XLSForm to QGIS project"** under the **"XLSForm"** group.
    3. Select your XLSForm spreadsheet file (`.xls`, `.xlsx`, or `.ods`).
    4. (Optional) Enter a custom project name and target language.

!![XLSForm Converter Process Interface](../../assets/images/xlsform-processing-windows.png,800px)

!!! Workflow
    5. Select a basemap layer (such as **OpenStreetMap** or **Humanitarian OpenStreetMap Team**).
    6. (Optional) Enable **"Create QFieldCloud project"** to automatically create a QFieldCloud project using QFieldSync.
    7. (Optional) Configure settings under **Advanced Parameters**:
        - Set custom project spatial extents.
        - Set target Coordinate Reference Systems (CRS) (defaults to `EPSG:3857 - WGS 84 / Pseudo-Mercator`).
        - Enable **"Pre-fill project with features' geometries and matching attributes"** to import existing feature datasets matching XLSForm table schemas.
    8. Specify the output folder path under **Project folder**.
    9. Click **"Run"**.

Upon completion, the plugin saves the generated `.qgz` project file and GeoPackage dataset in the specified directory.

## Additional Resources

For technical details and plugin documentation, refer to the following resources:

- [XLSForm Converter Source Code Repository](https://github.com/opengisch/XLSFormConverter)
- [OPENGIS.ch XLSForm Converter Announcement Blog Post](https://www.opengis.ch/2025/06/02/xlsform-converter-unlock-a-world-of-surveys-with-our-brand-new-qgis-plugin/)
