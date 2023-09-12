---
title: External routing
tx_slug: documentation_how-to_routing
---

# External routing

It can come in handy to calculate an itinerary to one of your features in the field.
By an easy configuration of your attribute form in QGIS, you can quickly access the navigation tools from Google Maps via a hyperlink when working on the field.

## Configure attribute form widget in QGIS
:material-monitor: Desktop preparation

Here is an example for navigation to features of a point layer.

Create a new field in your data table (type text). In the attribute form settings, select "attachment" as widget type. Tick "Display a hyperlink for document path (read-only)".
Then enter the following expression as default value:

```
concat(
  'https://www.google.com/maps/dir/?api=1&destination=',
  y(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
  '%2C',
  x(transform($geometry, layer_property(@layer, 'crs'), 'EPSG:4326')),
  '&travelmode=driving'
)
```

And tick "Apply default value on update" in case you make changes to your geometry.

If you simply want to show your feature location in Google Maps, you can use the following expression:
*concat( 'https://maps.google.com?q=  ',y(transform($geometry, layer_property(@layer, 'crs'),'EPSG:4326')), '%2C', x(transform($geometry, layer_property(@layer, 'crs'),'EPSG:4326')), '&zoom=19&t=h')*

## Usage
:material-tablet: Fieldwork

Click on the feature on the map where you want navigation to or that you want to open in Google Maps. In the attribute form, click on the link towards Google Maps.

