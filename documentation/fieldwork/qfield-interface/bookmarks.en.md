---
title: Bookmarks
tx_slug: documentation_how-to_bookmarks
---

# Bookmarks

QField allows you to save, organize, and navigate to spatial bookmarks across sessions and projects.
By default, bookmarks are displayed as marker overlays on the map, searchable via the search menu, and accessible from a dedicated list panel.

## Bookmark Types

QField can handle two distinct types of spatial bookmarks:

* **User Bookmarks:** You can create bookmarks directly inside QField.
You can access, edit, export and group them by colors across all your local projects.
* **Project Bookmarks:** These come with your QGIS project file (`.qgs`/`.qgz`) on the desktop.
These appear under the **Project bookmarks** section header in the list view and are read-only in QField.

## Bookmark Interaction

You can either interact with bookmarks directly on the map canvas or through the **Bookmark List**.
If you want to see bookmarks on the map, you will have to enable them under the general settings.

!!! Workflow

    1. Open the **Side Dashboard**.
    2. Tap the **3-dotted menu** icon to open **Settings**.
    3. Under **General**, toggle **Enable Bookmarks**.
    !![](../../assets/images/bookmarks-toggle.png, 800px)

Once enabled you can either **Display** their name by single-tapping on the bookmark or **re-center and zoom** to the map extent of where the bookmark was saved by double-tapping on it.
!![](../../assets/images/bookmarks.png)

### Bookmark List

To see all your saved bookmarks at once you can access the Bookmark List.

!!! Workflow

    1. Open the **Side Dashboard**.
    2. Tap the **3-dotted menu** and select **Bookmarks** in the menu.
    3. The Bookmark List will open, categorized into color groups (<span style="color:green">**Green**</span>, <span style="color:orange">**Orange**</span>, <span style="color:red">**Red**</span>, <span style="color:blue">**Green**</span>).
    If there are project bookmarks, which were created in QGIS before, they will be shown in this list
    4. Tap any bookmark in the list to instantly jump to its location on the map.
    !![](../../assets/images/list_panel_bookmarks.png)

## Adding a New Bookmark
:material-tablet: Fieldwork

Bookmark locations capture both the target point coordinates and the active map scale to preserve your preferred zoom level.

!!! Workflow

    Option 1: Long-Press on the Map

    1. Long-press on the map canvas at the desired location.
    2. Tap **Add Bookmark** in the pop-up context menu.
        !![](../../assets/images/bookmarks-add-from-touch.png, 300px)
    3. Enter a custom name and select a color marker group (*Green*, *Orange*, *Red*, *Blue*).
        !![](../../assets/images/bookmarks-properties.png, 800px)

!!! Workflow

    Option 2: Location Pie Menu

    1. Tap on your current location marker on the map canvas.
    2. Tap the **Bookmark** symbol in the bottom-right of the pie menu.
    3. Define the name and select a color.
    !![](../../assets/images/pie-menu-bookmark.png, 300px)

## Managing and Exporting Bookmarks

Your can edit, copy and delete your own bookmarks either one-by-one or multiple at the same time.
You can also export them as standalone vector datasets, such as Gpkg's.

### Individual Bookmark Actions

Under the Bookmark List Panel, tap the 3-dotted menu *(⋮)* next to the user bookmark in the Bookmark List panel to access quick actions:

- **Edit Bookmark:** Modify the name or change the color group.
- **Copy Bookmark Details:** Copies the bookmark name and its geographic coordinates (formatted in map CRS) directly to your clipboard.
- **Navigate to bookmark:** Sets the location as your active navigation destination.
- **Delete Bookmark:** Permanently removes the bookmark.
!![](../../assets/images/bookmarks_individual_actions.png, 300px)

### Multi-Selection and Deletion

!!! Workflow

    1. Open the **Bookmarks List**.
    2. Long-press on any user bookmark, or tap the top **3-dotted menu (⋮)** and select **Toggle Bookmark Selection**.
    3. Check the boxes next to the bookmarks you wish to select.
    4. Tap the **3-dotted menu (⋮)** and select **Delete Selected Bookmark(s)**.
    !![](../../assets/images/delte_multiple_bookmarks.png, 300px)

### Exporting Bookmarks

You can export your user bookmarks into a standalone GeoPackage (`.gpkg`) to share with colleagues or archive externally.

!!! Workflow

    Open the **Bookmarks List**.

    **Option 1: Export all Bookmarks**

    2. Tap **the 3-dotted menu (⋮)**
    3. Select **Export All User Bookmarks**.

    **Option 2: To export selected bookmarks**

    2. Long-press on the bookmark(s) you wish to export
    3. Open the **3-dotted menu (⋮)**
    4. Select **Export Selected Bookmark(s)**.

    In both cases QField will compile the point geometries, names, and color into a `.gpkg` file and prompt you with the **Send to...** dialog to transfer the file via email, cloud drive, or messaging apps.
    !![](../../assets/images/export_multiples_bookmarks_to_gpkg.png, 300px)

## Navigating to a Bookmark

You can set any bookmark directly as a active navigation destination.

###

!!! Workflow

    **Option 1: Via the Bookmark List**

    1. Open the **Side Dashboard**
    2. Tap the **3-dotted menu (⋮)** and select **Bookmarks**.
    2. Tap the **3-dotted menu (⋮)** next to the bookmark name.
    3. Select **Navigate to bookmark** (purple navigation flag icon).
    !![](../../assets/images/navigate_to_bookmark.png, 300px)

    **Option 2: Via Search (Locator)**

    1. Tap the **Search Bar** on the map canvas.
    2. Type the bookmark name (or type `b ` to filter explicitly for bookmarks).
    3. In the search results list, tap the <span style="color:purple">:material-flag:</span> next to the bookmark name to immediately start navigating, or tap the text to center the map canvas.
    !![](../../assets/images/bookmarks-search.png, 300px)
