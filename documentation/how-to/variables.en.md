---
title: Global variables
tx_slug: documentation_how-to_variables
---

# Project and Global Variables

Variables are a powerful feature in both QGIS and QField. They allow you to dynamically set values based on the current project, layer, system, or user-defined settings.
This can be used for a wide range of applications, including styling, setting default field values, controlling application behavior, and much more.

QField supports two main types of variables:

- **Project Variables:** These are defined within the QGIS project file itself (`.qgs/.qgz`). They are a central part of your project's configuration.
- **Global Variables:** These are specific to a user's device and are configured directly within the QField app.

## Project Variables

Project variables are defined and managed in your QGIS project. They are ideal for settings that are integral to the project's logic and shared with all users.

### User-Customized Project Variables

A key feature in QField is the ability for users to customize project variables on their device without altering the main project file.
This is particularly useful for projects shared, allowing each user to adapt the project to their specific needs.

For example, a project could have a variable named `lang` that controls the language of labels and descriptions.
A user can change the value of this `lang` variable on their device to their preferred language.
These changes are saved locally and will be restored the next time they open the project, all without affecting the experience of other users sharing the same project.

## Global Variables

Global variables are managed directly on your device and can be used across all projects opened in QField.

### Configuring Global Variables

:material-tablet: Fieldwork

To configure a device-specific global variable, follow these steps:

1. Open **Settings** in QField.
2. Navigate to the **Variables** tab.

Here you will see a list of predefined system variables. To add a new variable:

1. Click on *Add a new variable* at the bottom of the variable list.
2. Enter the name and value for your new variable.

## Variable Management in QField

When you access the variables list in QField (_Settings > Variables_), you will find a consolidated and organized view of all available variables.

The list is sorted to ensure that the most relevant variables are easily accessible:

1. **Project Variables:** All variables from the current QGIS project are displayed at the top.
These are the variables you are most likely to interact with for project-specific configurations.
2. **Editable Global Variables:** Your custom, device-specific variables appear next.
3. **Read-Only Variables:** Pre-defined, read-only system variables are listed at the bottom.

!![Configuration of two new global variables in addition to the
pre-defined system
variables.](../assets/images/configure_global_variables.png)
