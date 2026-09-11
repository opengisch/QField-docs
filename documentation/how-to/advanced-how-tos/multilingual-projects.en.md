---
title: Multilingual project support
tx_slug: documentation_how_to_multiligual_project_support
---

# Multilingual Project Support

QField supports project localization, allowing a single QGIS project file to display in multiple languages based on device settings.

Layer names, field aliases, value maps, and metadata display in the device's local language without duplicating QGIS project files.

## How It Works

Project localization relies on compiled Qt Translation files (`.qm`) stored alongside QGIS project files (`.qgs` or `.qgz`).
When QField loads a project, it detects the device or application language setting.
If a matching translation file exists, QField translates the project interface automatically.

!!! Example

    A project file named `Beekeeping.qgs` configured with English as the source language:

     - **English Device:** Displays layer titles as "Bee Species".
     - **German Device:** QField detects the German system locale, loads `Beekeeping_de.qm`, and displays layer titles as "Bienenarten".



## Setting Up Multilingual Projects

You can prepare multilingual projects in QGIS using standard Qt translation workflows.
For additional background, read the [OPENGIS.ch QGIS Multilingual Announcement](https://www.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/).

!!! Workflow
    **Step 1: Generate Translation Source Files (TS) in QGIS**

    1. Open your project in QGIS on desktop.
    2. Navigate to _Project > Properties... > General_.
    3. Under **Generate Translation Source File (TS)**, select your project's primary source language (e.g., English).
    4. Click **Generate TS File**. QGIS creates a `.ts` XML file in your project directory containing all translatable strings (layer names, group names, field aliases, value relations, and metadata).


    **Step 2: Translate Strings using Qt Linguist**

    1. Open the generated `.ts` file using **Qt Linguist** or translation platforms like Transifex.
    2. Translate source text strings into target languages (e.g., source string "Beekeeper" translated to "Imker").


    **Step 3: Compile Translation Files (QM)**

    1. In Qt Linguist, select **File > Release** to compile `.ts` XML files into binary `.qm` translation files.
    2. Name the `.qm` file to match your project filename appended with the ISO language code:
        - Project file: `citybees.qgz`
        - German translation file: `citybees_de.qm`
        - French translation file: `citybees_fr.qm`


    **Step 4: Deploy to QField or QFieldCloud**

    1. Store `.qm` translation files in the same directory as the main project file (`.qgs` or `.qgz`).
    2. Transfer the project directory to your mobile device or synchronize via QFieldCloud.

!!! Note
    - **Sidecar Project Files:** Opening translated projects in QGIS Desktop may generate temporary project files (such as `citybees_de.qgs`). QField hides these sidecar project files in the project selector to prevent opening incomplete projects. Always open the primary project file.
    - **Translatable Elements:**
        - Layer and group names
        - Field aliases (Field *Names* remain unchanged to maintain database integrity)
        - Value Relation and Value Map widget displays
        - Project and layer metadata

## Key Features

- **Automatic Language Detection:** Respects QField application language settings or device OS system locales without manual switching.
- **Clean File Selection:** Hides generated sidecar translation project files (such as `Beekeeping_de.qgs`) from the file selector screen.
Users select the main project file (`Beekeeping.qgs`), and QField handles translations automatically.
- **QFieldCloud Support:** Full compatibility with QFieldCloud projects and cloud synchronization workflows.
- **Metadata Localization:** Translates project and layer metadata (titles, abstracts, and descriptions) for field data identification.
