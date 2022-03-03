---
title: Track lines and polygons
---

# Track lines and polygons

You have the possibility to do tracking on lines and polygons.

![type:video](https://player.vimeo.com/video/499958163)

It's available when GNSS is enabled. A tracking session can be started
in the legend by long-pressing on the layer. The time interval and the
minimum distance can be entered individually to define when a vertex
needs to be set.

There can be several trackings session active on several layers. But
only one tracking session per layer can be active at the time.

!![tracking_layers1](../assets/images/track_lines_tracking_layers1.jpeg)

!![tracking_layers2](../assets/images/track_lines_tracking_layers2.jpeg)

The tracked feature is saved on every vertex. While the tracking session
is active the layer is still editable, but the tracked feature can't be
edited or deleted until the tracking session is stopped over the legend
again.

!![stop_tracking_delete](../assets/images/track_lines_stop_tracking_delete.jpeg)

If the layer geometry supports m value, the time is stored in the m
value, that passed since the first vertex of this tracking session has
been recorded.
