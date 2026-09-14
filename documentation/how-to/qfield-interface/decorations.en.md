---
title: Map decorations
tx_slug: documentation_how-to_decorations
---

# Map Decorations

:material-monitor: Desktop preparation

Customize your project with decorations in QField by configuring them first in QGIS.
Read more in the [QGIS Map View Documentation](https://docs.qgis.org/latest/en/docs/user_manual/map_views/map_view.html#decorating-the-map). <!-- markdown-link-check-disable-line -->

Choose from several decoration types:

- **"Grid":** Overlays the map canvas with lines or markers at defined intervals to provide spatial reference, which is useful in remote areas.
- **"Title Label":** Displays a title on your map, such as the project name.
- **"Copyright Label":** Displays data source origins or branding information on your map canvas.
- **"Image":** Places a logo, watermark, or graphic directly on your map.
- **"Scale Bar":** Displays a scale bar on the map canvas, which can be enabled directly inside QField settings.

### Grid

!!! Workflow
    1. In QGIS, navigate to _View > Decorations > Grid..._.
    2. Enable the **"Enable Grid"** checkbox.
    3. Customize the grid appearance options:

        - **"Grid type":** Select **"Solid lines"**, **"Crosses"**, or **"Markers"**.
        - **"Interval":** Set grid line spacing along the **X** and **Y** axes based on the project Coordinate Reference System (CRS).
        - **"Line/Marker Symbol":** Customize color, thickness, and style for grid lines or markers.
        - **"Draw annotations":** Displays grid coordinates on the map canvas, controlling font, orientation, and margin distance from the map frame.

Once configured in QGIS, the grid displays automatically in QField after synchronizing or transferring the project.

### Title Label

!!! Workflow
    1. In QGIS, navigate to _View > Decorations > Title Label..._.
    2. Enable the **"Enable Title Label"** checkbox.
    3. Enter static text or construct a dynamic title using QGIS expressions.
    4. Click the **"Insert or Edit an Expression..."** button to open the expression builder.

    A common use case displays the project title configured under _Project > Properties... > General_:

    ```sql
    -- Displays the title saved in the project properties
    [% @project_title %]
    ```

    **Example of a more complex title:**

    Combine static text with expression variables and functions to generate dynamic titles:

    ```sql
    -- Creates a title like: "Survey for Project *' %project_name% - 20xx"
    'Survey for Project ' || [% @project_title %] || ' - ' || [% year(now()) %]
    ```

### Copyright Label

!!! Workflow
    1. In QGIS, select _View > Decorations > Copyright Label…_.
    2. Enable the "Enable Copyright Label" checkbox.
    3. Enter copyright text or use QGIS expressions to display dynamic content.

    Use expressions to display real-time positioning information and map scale directly on the map canvas:

    ```sql
    -- Displays the GNSS coordinates and current map scale
    Lat: [% format_number(y(@gnss_coordinate), 8) %] | Lon: [% format_number(x(@gnss_coordinate), 8) %]
    Scale: 1:[% round(@map_scale) %]
    ```

    The ability to use [positioning variables](../../reference/expression_variables.md#positioning-and-gnss-variables) (`@gnss_coordinate`) offers a streamlined way to display critical location data without cluttering the main user interface.

### Image

!!! Workflow
    1. In QGIS, open _View > Decorations > Image…_.
    2. Enable the **"Enable Image"** checkbox.
    3. Click the **"..."** button next to **"Image path"** to select your image file.

    !!! Important
        Store image files inside your project directory and use relative file paths for compatibility with QField.

        - Create a dedicated folder inside your project directory (e.g., `assets`).
        - Reference the image using a path that starts with `./`.

        Example of a relative path:

        `./assets/company_logo.png`

    ![type:video](../../assets/videos/qfield_map_decoration.webm)

### Scale Bar

:material-tablet: Fieldwork

!!! Workflow

    1. Open your project in QField.
    2. Open the **"Side Dashboard"** (**☰**).
    3. Tap the **Settings** icon.
    4. Navigate to the **"General"** section.
    5. Enable **Show scale bar** .

    !![](../../assets/images/scale_bar_toggle.png,900px)
