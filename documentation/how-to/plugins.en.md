---
title: Plugins
tx_slug: documentation_how-to_plugins
---

# QField Plugins

QField has a QML/Javascript plugin framework through which additional functionalities and features can be scripted.

## Types of plugins

Plugins can be served in two ways:

- as a project-specific plugin that will be active for the duration of a given project session;
- as an application plugin that will be activated when QField launches.

!!! note
    A permission dialog is shown prior to activating a plugin, providing you with the possibility of granting or denying individual plugins.

### Project plugins

Project plugins are deployed as a sidecar file to a given project file and must share the same file name with a .qml extension.
For example, if your project file is “tree_inventory_qfield.qgs”, the plugin’s main QML file must be “tree_inventory_qfield.qml”.

For cloud projects, you simply add the relevant QML file into your local cloud project folder and upload the newly added file on QGIS using qfieldsync.
This method insures a smooth plugin deployment and update to devices on the field.

For non-cloud projects, refer to the QField [storage handling documentation page](../get-started/storage.md)
to learn how to import projects onto devices.

### Application plugins

Application plugins are installed through a plugins popup accessed from QField’s Settings panel.
Click on the "Install plugin from URL" button and paste in a URL pointing to a zipped plugin file, or download one of the "Available Plugins" already developed by the [community](../reference/plugins.md).

!![](../assets/images/application-plugins.png,400px)

Once installed, the plugin will appear in the plugins list found in the popup, with a switch to toggle the activation of the plugin.
