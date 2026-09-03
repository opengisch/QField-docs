---
title: External routing
tx_slug: documentation_how-to_routing
---

# External Routing

Calculate itineraries or open external navigation applications (such as Google Maps or Apple Maps) directly from feature attribute forms in QField.
Configure attribute fields with dynamic hyperlink expressions in QGIS to open routing and mapping services in external mobile applications.

## Configuring External Routing in QGIS
:material-monitor: Desktop preparation

### Direct Navigation Directions

Configure an attribute field to open driving directions to feature coordinates in Google Maps.

!!! Workflow
    1. Open your project in QGIS and add a text attribute field (such as `routing_url`) to your vector layer.
    2. Navigate to _Vector Layer Properties... > Attribute Form_.
    3. Select your routing attribute field and set **"Widget Type"** to **"Attachment"**.
    4. Enable **"Display a hyperlink for document path (read-only)"**.
    5. Set **"Default Value"** to the following navigation directions expression:

        ```sql
        concat(
          'https://www.google.com/maps/dir/?api=1&destination=',
          y(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
          '%2C',
          x(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
          '&travelmode=driving'
        )
        ```

    6. (Optional) Enable **"Apply default value on update"** to recalculate routing links automatically when feature geometries change.

### Feature Location Preview

Configure an attribute field to open and highlight feature coordinates on external maps without initiating active turn-by-turn navigation.

!!! Workflow
    1. Follow steps 1–4 from the navigation directions workflow above.
    2. Set **"Default Value"** to the following location preview expression:

        ```sql
        concat(
          '[https://maps.google.com?q=](https://maps.google.com?q=)',
          y(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
          '%2C',
          x(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
          '&zoom=19&t=h'
        )
        ```

    3. (Optional) Enable **"Apply default value on update"**.

## Accessing External Navigation in QField
:material-tablet: Fieldwork

!!! Workflow
    1. Open your project in QField and tap a feature on the map canvas to open its attribute form.
    2. Locate the routing attribute field inside the feature form.
    3. Tap the hyperlink text to launch your device's native browser or external navigation app.
