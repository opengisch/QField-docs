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

Before heading out to the field though, preliminary steps such as layer styling, tailored forms, input validation, or any other project configurations should first be done on the desktop via QGIS.

## Compatibility with QGIS


Since QField is a mobile optimized version of the QGIS desktop app, your project will appear and feel identical both in QGIS and QField.
The rendering engine in QField is the same as the one used in desktop QGIS, ensuring that projects will appear virtually identical in both environments.

Configuration options prepared in QGIS beforehand don't need to be recreated, which is why QField uses the same edit widgets as QGIS desktop does.
As a result, projects configured on the desktop should work seamlessly on the mobile app.

These principles have so far informed our development and design of QField, and will continue to do so in the future.
In the last few years, QField has proved to be the fieldworker's best friend and continues to evolve with new features handling an even broader range of needs.

!!! Workflow

    To illustrate how these principles translate into action, a typical data collection cycle involves the following steps:

    1. **Package**: Create a QField package using the QFieldSync plugin in QGIS. This generates a working copy in a separate folder.
    2. **Transfer**: Copy the QField package to the target mobile device (via cable or file transfer).
    3. **Collect**: Go out to the field and collect data using QField.
    4. **Transfer**: Copy the modified project folder back to your desktop computer.
    5. **Synchronize**: Synchronize the modified data with your original database or files.


!!! note
    If you are using **QFieldCloud**, the manual transfer steps (2 and 4) are handled automatically over the internet.

## Mode based

QField is built around different *modes*, similar to the *map tools* in the QGIS desktop version.
The mode currently selected defines the nature of the task being performed:

* **Browsing:** Users move around the map, inspect layers, and view feature attributes.
* **Digitizing:** Users enter an edit mode to record new features or modify existing data in the field.
