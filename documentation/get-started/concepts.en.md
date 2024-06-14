---
title: Concepts
tx_slug: documentation_get-started_concepts
---

# Concepts

QField was designed with a few key concepts in mind.

## Keep it simple

The requirements in the field are hardly the same as on a desktop. Firstly, when using a phone or a tablet, the
canvas to work on is much more limited than a computer monitor. 
Secondly, devices for data collection as well as the individual tasks that need to be performed are vastly different.

QField aims to help users do fieldwork without the nuisance of a cluttered user interface. 
In other words, only the relevant parts of a task are accessible on the interface, while less important things remain out of sight.

Before heading out to the field though, preliminary steps such as layer styling, tailored forms, or in general any other project configurations 
should first be done on the QGIS desktop version.

## Be compatible with QGIS

Since QField relies on the QGIS Libraries, it is not an extensive rebuild of QGIS. The rendering engine in QField is the same as the one used in desktop QGIS, ensuring that projects will appear virtually identical in both environments.

Configurations options prepared in QGIS beforehand don't need to be recreated, which is why QField uses the same
edit widgets as QGIS desktop does. As a result, projects configured on the desktop should work seamlessly on the mobile app.

Remember, this is just the *concept*. This is what we have in mind when
we develop QField. It does not mean that it is already completely there
yet.

## Mode based

QField is built around *modes*. Modes are similar to a *map tool* in
QGIS desktop. A mode defines the task which a user is currently doing.
Either a user is *browsing* through the data or she is *digitizing*
something new.
