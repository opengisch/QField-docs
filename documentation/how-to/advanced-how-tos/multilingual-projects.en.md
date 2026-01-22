---
title: Multilingual Project Support
tx_slug: documentation_how_to_multiligual_project_support
---

# Multilingual Project Support in QField

QField supports for **Project Localization**, meaning that a single QGIS project file supports multiple languages if the according configuration has been applied.

This allows the field staff to see the layer names, field aliases, and value maps in the device's local language without needing separate project files.

### How it works

The system relies on Qt Translation files (`.qm`) stored alongside the QGIS project.
When QField opens a project, it checks the device's language settings.
If a matching translation file is found, QField automatically translates the project interface.

**Example:**

You have a project named `Beekeeping.qgs` (in English).

- **User A** has a phone with an **English** operating system.
As a title, when opening the project the user will see "Bee Species" as a title.
- **User B** has a phone with a **German** operating system.
When opening the same project file (`Beekeeping.qgs`).
QField will detect the local language, accesses the German translation file, and correspondingly displays "Bienenarten" as title instead.

### Key Features

- **Automatic Language Detection:** QField respects the language defined in QField's system settings or the device's Operating System locale.
Languages do not need to manually switched.
- **Cleaner File Browser:** QField hides the "translated" sidecar project files (e.g., `Beekeeping_de.qgs`) from the file selector.
 Users simply select the main project file, and QField handles the translation in the background.
- **Cloud Support:** This feature is fully compatible with QFieldCloud projects.
- **Metadata Support:** This is supported for translating project and layer metadata (titles, abstracts, etc.), useful for identifying datasets in the field.

### Setting up Multilingual Projects

To enable this in QField, you must prepare your project in QGIS.
The workflow is identical to the standard QGIS localization process.
(for a more detailed step-by-step instructions check the following blog [QGIS speaks a lot of languages](https://www.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/)).

!!! Workflow

    :material-monitor: QGIS Setup

    1.  Open your project in QGIS.
    2.  Go to **Project Properties > General**.
    3.  Under **Generate Transaction Source File (TS)**, select your project's source language (e.g., English).
    4.  Click **Generate TS File**. This creates a `.ts` (XML) file in your project folder containing all translatable strings (Layer names, Field Aliases, Value Relations, etc.).

    :material-monitor: 2. Translation

    1.  Open the `.ts` file using **Qt Linguist** (standard Qt utility) or a web platform like Transifex.
    2.  Translate the strings (e.g., source: "Beekeeper", translation: "Imker").

    :material-monitor: 3. Compilation

    1.  Once translated, "Release" the file in Qt Linguist to generate a `.qm` file (binary translation file).
    2.  **Crucial Naming Convention:** The `.qm` file must be named exactly matching your project filename with the language code appended.
        * Project: `citybees.qgs`
        * German Translation: `citybees_de.qm`
        * French Translation: `citybees_fr.qm`

    :material-monitor: 4. Transfer to QField

    1.  Copy the `.qgs` (or `.qgz`) file and the associated `.qm` files to the device (or upload them to QFieldCloud).

!!! notes

    * **Sidecar Files:** In QGIS Desktop, opening a translated project often generates a temporary file (e.g., `citybees_de.qgs`). QField is programmed to ignore these files in the browser to prevent users from opening the wrong file. Always open the source project.
    * **Translatable Elements:**
        * Layer Names & Group Names
        * Field Aliases (Note: Field *Names* remain unchanged to preserve data integrity; only Aliases are translated)
        * Value Relation Widgets (Content)
        * Project Metadata
