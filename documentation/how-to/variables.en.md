---
title: Variables
tx_slug: documentation_how-to_variables
---

# Variables

QField allows users to add and edit expression variables.
These can be used for a wide range of applications, including data-defined symbology, setting default field values, controlling print layout and application behavior, and much more.
See [the relevant QGIS documentation](https://docs.qgis.org/latest/en/docs/user_manual/introduction/general_tools.html#storing-values-in-variables) for more information.

QField supports two main types of custom variables:

- **Project Variables:** Project-bound variables defined within the project file.
- **Global Variables:** Application-wide global variables with a set of read-only variables matching those found in QGIS.

!!! note
    Like any other variable, these can be used in expressions with prefixed with `@`.
    The variables will only be available on QField and not in QGIS at configuration time.
    To make configuration easier, it's recommended to configure the same variables in the QGIS instance where you are configuring your project.

## Project Variables

Project variables are defined and managed directly within your QGIS project.
They allow you to add custom variables that are only relevant in the context of a specific project.
QField users can edit those variables, with modified values remembered across sessions.

## Global Variables

QField comes pre-configured with some global variables which are visible in Settings->Variables.
New global variables can be added or modified and will be available in QField across sessions.
Global variables can be used to add a unique identifier across a fleet of QField devices if `@cloud_username` is not available.
Since they are not bound to specific projects and are defined locally, they make for a great way to customize experience for multiple users sharing the same projects.

## Variable Management in QField

Variables are managed directly on your device and are accessible in all available QField projects.
When you access the variables list in QField ( Settings > Variables ), you will find a consolidated and organized view of all available variables.

### Variable configuration

:material-tablet: Fieldwork

To configure a device-specific variable, follow these steps:

1. Open **Settings** in QField.
2. Navigate to the **Variables** tab.

Here you will see a list of all variables currently applicable to your project.
To add a new variable:

1. Click on *Add a new variable* at the bottom of the variable list.
2. Enter the name and value for your new variable.

!![Configuration of editable variables in addition to the
pre-defined system variables.](../assets/images/configure_global_variables.png, 400px)
