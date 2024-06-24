---
title: Principles
tx_slug: documentation_get-started_concepts
---

# Principles

QField is designed with a few key principles in mind.


## Keeping it simple

The requirements in the field are not the same as on a desktop.
Firstly, when using a phone or a tablet, the canvas to work on is much more limited than a computer monitor.
Secondly, devices for data collection as well as the individual tasks that need to be performed are vastly different.

QField aims to help users do fieldwork without the nuisance of a cluttered user interface.
In other words, only the relevant parts of a task are accessible on the interface, while less important things remain out of sight.

Before heading out to the field though, preliminary steps such as layer styling, tailored forms, or any other project configurations should first be done on the QGIS desktop version.

## Compatibility with QGIS

Since QField relies on exxisting QGIS Libraries, it is not an extensive rebuild of QGIS. 
The rendering engine in QField is the same as the one used in desktop QGIS, ensuring that projects will appear virtually identical in both environments.

Configurations options prepared in QGIS beforehand don't need to be recreated, which is why QField uses the same edit widgets as QGIS desktop does. 
As a result, projects configured on the desktop should work seamlessly on the mobile app.

These principles have so far informed our development and design of QField, and will continue to do so in the future. 
Even though QField has been around for some time now, it is still a work in progress.

## Mode based

QField is built around different *modes*, similar to the *map tools* in the QGIS desktop version.
The mode defines the nature of the task.
In QField, users are either *browsing* through data or *digitizing* new stuff.
