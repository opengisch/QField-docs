---
title: Authentication
tx_slug: documentation_how-to_authentication
---

# Authentication

QField supports connecting to services requiring access authentication. This page will go through authentication examples as well as demonstrating how to export authentication configuration from QGIS into QField

## OAuth2-protected web services

To successfully load OAuth2-protected layer(s) in QField, the QGIS project must be setup to use OAuth2.

### Prepare the OAuth2 authentication in QGIS
:material-monitor: Desktop preparation

To setup a WFS with OAuth2 in QGIS follow these steps in the QGIS project configuration.

In the WFS layer configuration:

!![widgets](../assets/images/oauth2_setup_wfs.png)

Add a new authentication configuration and adjust parameters to match your OAuth2 server setup:

!![widgets](../assets/images/oauth2_setup_auth.png)

Once the layer's authentication configuration is setup, you can add layer(s) into your project and test that the authentication mechanism works as expected. Follow instructions below to export the configuration into QField.

## Export authentication configurations from QGIS
:material-monitor: Desktop preparation

!!! note
    Prior to exporting authentication configurations, it is always good to verify that you are able to properly connect to relevant service(s) using QGIS.

To export one or more authentication configurations, open the QGIS options dialog and select the authentication panel. There, you can select multiple authentication configurations by selecting the appropriate rows in the configurations table widget. Then, use the lower-right utilities button to select the *export selected authentication configurations to file* action.

!![widgets](../assets/images/oauth2_export_config.png)

When prompted for a password, *leave it blank*. You will be warned that might be leaking sensitive information, which is a good reminder to treat the resulting XML with caution.

## Import authentication configurations into QField
:material-monitor: Desktop preparation

Once you have exported the authentication configuration(s) to an XML file, you must copy that file onto the device(s) running QField. The file has to be copied to into an `auth` folder found within the QField's app directory:

- On Android, you can find the directory by connecting your device using a USB cable; the directory will be located at `<drive>:/Android/data/ch.opengis.qfield/files/QField/auth/`;
- On desktop platforms, you can reach this directory by clicking on the directory path located towards the bottom of the About QField popup.

Once the authentication configurations file is copied, project files containing web services requiring authentications will be able to reach the relevant configuration details and provide access.

For authentication methods requiring user input such as OAuth2, QField will provide a browser or dialog to prompting for the required details such as user, password, or 2-step authentication code.
