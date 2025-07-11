---
title: Variables
tx_slug: documentation_how-to_variables
---

# Variables

With the support of variables you can dynamically add additional values at different levels, such as project, layer or model specific level.
See [the relevant QGIS Documentation](https://docs.qgis.org/3.40/en/docs/user_manual/introduction/general_tools.html#storing-values-in-variables) for more information.
They can be used for a wide range of applications, including styling, setting default field values, controlling application behavior and more.

QField supports two main types of variables:

- **Project Variables:** Project variables are defined and managed in your QGIS project.
- **Global Variables:** The global variables adopt the global variables of QGIS. Additional device-specific variables can be configured directly within QField.

## Project Variables

Project variables are defined and managed directly within your QGIS project.
They allow you to add custom variables that are only relevant in the context of a specific project.
This is especially useful working among multiple users.

## Global Variables

A key feature in QField is the ability for users to customize variables on their devices without changing or adapting the original variables set in a project file.

For example, a project could have a variable named `lang` that controls the language of labels and descriptions.
A user can change the value of this `lang` variable on their device to their preferred language.
These changes are saved locally and will be restored the next time they open the project, all without affecting the experience of other users sharing the same project.

## Variable Management in QField

Variables are managed directly on your device and are accessible in all available QField projects.
When you access the variables list in QField ( Settings > Variables ), you will find a consolidated and organized view of all available variables.

### Variable configuration

:material-tablet: Fieldwork

To configure a device-specific variable, follow these steps:

1. Open **Settings** in QField (Legend > ... > Settings).
2. Navigate to the **Variables** tab.

Here you will see a list of all variables currently applicable to your project.
To add a new variable:

1. Click on *Add a new variable* at the bottom of the variable list.
2. Enter the name and value for your new variable.

The list is sorted to ensure that the most relevant variables are easily accessible:

1. **Project Variables:** All variables from the current QGIS project are displayed at the top.
These are the variables you are most likely to interact with for project-specific configurations.
2. **Editable Device-Specific Variables:** Your custom, device-specific variables appear next.
3. **Global Variables:** Pre-defined, read-only system variables are listed at the bottom.

!![Configuration of editable variables in addition to the
pre-defined system variables.](../assets/images/configure_global_variables.png, 400px)
