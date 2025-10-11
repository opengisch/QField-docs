---
title: External routing
tx_slug: documentation_how-to_routing
---

# External routing

It can come in handy to calculate an itinerary to one of your features in the field.
By an easy configuration of your attribute form in QGIS, you can quickly access the navigation tools from Google Maps via a hyperlink when working in the field.

!!! Workflow

    :material-monitor: Desktop preparation

    1. In QGIS Create a new field in your feature layer with the datatype text
    2. Under *Vector Properties* Find the "attribute form" setting
    3. As widget type select "attachment"
    4. Tick "Display a hyperlink for document path (read-only)".
    5. Then enter the following expression as default value:

        ```sql
          concat(
            'https://www.google.com/maps/dir/?api=1&destination=',
            y(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
            '%2C',
            x(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
            '&travelmode=driving'
          )
        ```

    6. (Optional) Tick "Apply default value on update" in case you make changes to your geometry.

    **Show Feature Location only**

    1. Follow the same steps (1-4) as above
    2. This time use the following expression:

    ```sql
      concat( 'https://maps.google.com?q=',
      y(transform($geometry, layer_property(@layer, 'crs'),'EPSG:4326')),
      '%2C',
      x(transform($geometry, layer_property(@layer, 'crs'),'EPSG:4326')),
      '&zoom=19&t=h')
    ```

    :material-tablet: Fieldwork

    1. In QField select the feature layer where you added the field.
    2. Edit the layer and find the according attribute.
    3. Click on the link towards Google Maps
