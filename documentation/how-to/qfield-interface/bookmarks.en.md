---
title: Bookmarks
tx_slug: documentation_how-to_bookmarks
---

# Bookmarks

QField allows you to save, organize, and navigate to spatial bookmarks across sessions and projects.
By default, bookmarks display as marker overlays on the map canvas, appear in search bar queries, and list inside a dedicated Bookmarks panel.

## Project Bookmarks vs. User Bookmarks

QField categorizes spatial bookmarks into two types:

- **User Bookmarks:** Created directly inside QField on mobile devices.
User bookmarks persist across local projects and can be edited, grouped by color, or exported to GeoPackage files.
- **Project Bookmarks:** Embedded inside QGIS project files (`.qgs` or `.qgz`) on desktop computers.
Project bookmarks display under the **"Project bookmarks"** section header in the list view and remain read-only in QField.

### Creating Project Bookmarks in QGIS
:material-desktop: Desktop preparation

!!! Workflow
    1. Open your project in QGIS and navigate to your target spatial extent.
    2. Press **Ctrl + B** or navigate to _View > New Spatial Bookmark..._.
    3. Enter a bookmark name, group, and map extent in the [QGIS Spatial Bookmarks Manager](https://docs.qgis.org/latest/en/docs/user_manual/introduction/browser.html#spatial-bookmarks). <!-- markdown-link-check-disable-line -->
    4. Save your project and synchronize it to QField.

!![Spatial Bookmark QGIS](../../assets/images/bookmarks-qgis.png,600px)

## Viewing and Accessing Bookmarks
:material-tablet: Fieldwork

Interact with spatial bookmarks in QField using two methods:

### Map Overlays

Bookmarks display directly on the map canvas as colored marker pins:

- **Single tap:** Displays the bookmark name label.
- **Double tap:** Centers and zooms the map canvas to the bookmark extent.

!![](../../assets/images/bookmarks.png)

### Bookmark List Panel

QField includes a dedicated side drawer to manage and browse bookmarks.

!!! Workflow
    1. Open the **Side Dashboard** from the map canvas.
    2. Tap the three-dotted menu *(⋮)* and select **"Bookmarks"**.
    3. Browse bookmarks categorized by color groups (*Green*, *Orange*, *Red*, *Blue*) or under the **"Project bookmarks"** header.
    4. Tap any bookmark entry in the list to pan and zoom directly to its location on the map canvas.

!![](../../assets/images/list_panel_bookmarks.png)

## Adding a New Bookmark
:material-tablet: Fieldwork

Bookmark locations capture target coordinates and active map scales to preserve zoom levels.

### Option 1: Long-Press on the Map

!!! Workflow
    1. Long-press the map canvas at the target location.
    2. Tap **"Add Bookmark"** in the context menu.
        !![](../../assets/images/bookmarks-add-from-touch.png, 300px)
    3. Enter a bookmark name and select a color group (*Green*, *Orange*, *Red*, *Blue*).
        !![](../../assets/images/bookmarks-properties.png, 800px)

### Option 2: Location Pie Menu

!!! Workflow
    1. Tap your current location marker on the map canvas.
    2. Tap the bookmark icon in the bottom-right corner of the pie menu.
    3. Enter a bookmark name and select a color group.

!![](../../assets/images/pie-menu-bookmark.png, 300px)

## Managing and Exporting Bookmarks
:material-tablet: Fieldwork

User-created bookmarks can be edited, copied, deleted individually or in batches, and exported to standalone GeoPackage datasets.

### Individual Bookmark Actions

Open the Bookmark List panel and tap the three-dotted menu *(⋮)* next to a user bookmark to perform the following actions:

- **"Edit Bookmark":** Modifies the bookmark name or color group.
- **"Copy Bookmark Details":** Copies the bookmark name and geographic coordinates to the device clipboard.
- **"Navigate to bookmark":** Sets the bookmark as the active navigation destination.
- **"Delete Bookmark":** Deletes the bookmark.

!![](../../assets/images/bookmarks_individual_actions.png, 300px)

### Multi-Selection and Batch Deletion

!!! Workflow
    1. Open the **Bookmarks** list panel from the Side Dashboard.
    2. Long-press a user bookmark or tap the top three-dotted menu *(⋮)* and select **"Toggle Bookmark Selection"**.
    3. Check the selection boxes next to target bookmarks.
    4. Tap the three-dotted menu *(⋮)* and select **"Delete Selected Bookmark(s)"**.

!![](../../assets/images/delte_multiple_bookmarks.png, 300px)

### Exporting Bookmarks to GeoPackage

Export user bookmarks to a standalone GeoPackage (`.gpkg`) file to archive or share with colleagues.

!!! Workflow
    1. Open the **Bookmarks** list panel from the Side Dashboard.
    2. Select target bookmarks or export all bookmarks:

        - **Export all user bookmarks:** Tap the top three-dotted menu *(⋮)* and select **"Export All User Bookmarks"**.
        - **Export selected user bookmarks:** Select target bookmarks, tap the top three-dotted menu *(⋮)*, and select **"Export Selected Bookmark(s)"**.
    3. QField compiles bookmark geometries, names, and color attributes into a `.gpkg` file and opens the native device sharing dialog (**"Send to..."**) to transfer the file via email or cloud storage.

!![](../../assets/images/export_multiples_bookmarks_to_gpkg.png, 300px)

## Navigating to a Bookmark
:material-tablet: Fieldwork

Set any spatial bookmark as an active navigation destination.

### Option 1: Via the Bookmark List Panel

!!! Workflow
    1. Open the **Bookmarks** list panel from the Side Dashboard.
    2. Tap the three-dotted menu *(⋮)* next to the target bookmark.
    3. Select **"Navigate to bookmark"** (navigation flag icon).
    4. QField sets the bookmark coordinates as the active navigation target.

!![](../../assets/images/navigate_to_bookmark.png, 300px)

### Option 2: Via Search Bar

!!! Workflow
    1. Tap the search bar on the map canvas.
    2. Enter the bookmark name or type `b ` to filter for bookmarks.
    3. Tap the purple navigation flag icon next to the bookmark in the search list to start navigation, or tap the text label to pan to the location.

!![](../../assets/images/bookmarks-search.png, 300px)

## Enabling or Disabling Bookmarks
:material-tablet: Fieldwork

Hide spatial bookmark overlay pins on the map canvas:

!!! Workflow
    1. Open the **Side Dashboard**.
    2. Tap the gear icon to open **Settings**.
    3. Under **General**, toggle **"Show bookmarks"**.

!![](../../assets/images/bookmarks-toggle.png, 800px)
