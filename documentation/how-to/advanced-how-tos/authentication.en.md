---
title: Authentication
tx_slug: documentation_how-to_authentication
---

# Authentication

QField supports connecting to web services requiring user or token authentication.
This page details configuring OAuth2 services in QGIS and exporting authentication configurations to QField mobile devices.

## OAuth2-Protected Web Services in QGIS
:material-monitor: Desktop preparation

Configure OAuth2-protected web layers (such as WFS or WMS) in QGIS before loading them in QField.

!!! Workflow
    1. In QGIS, navigate to _Layer > Add Layer > Add WFS / OGC API Feature Layer..._.
    2. Click **"New"** or select an existing service connection and click **"Edit"**.
    3. Under the **"Authentication"** section, click the green plus (**"+"**) button to add a new authentication configuration.
    4. Set **"Type"** to **"OAuth2"** and adjust parameters to match your OAuth2 provider server setup.
    5. Save the configuration and verify that layers load correctly on the QGIS canvas.

!![WFS Service Settings](../../assets/images/oauth2_setup_wfs.png)

!![Authentication](../../assets/images/oauth2_setup_auth.png)

## Export Authentication Configurations from QGIS
:material-monitor: Desktop preparation

Export authentication configurations from QGIS to transfer service credentials securely to mobile devices.
Verify that service connections function properly in QGIS before exporting credentials.

!!! Workflow
    1. In QGIS, navigate to _Settings > Options... > Authentication_.
    2. Select target configuration entries in the configurations table.
    3. Click **"Utilities"** and select **"Export selected authentication configurations to file..."**.
    4. When prompted for an encryption password, leave the password field **blank**.

!![QGIS Authentication Settings](../../assets/images/oauth2_export_config.png)

!!! Warning
    Leaving authentication export passwords blank stores credentials in plain text inside the output XML file.
    Keep exported XML files secure and delete them after completing device deployment.

## Import Authentication Configurations into QField
:material-tablet: Fieldwork

Transfer exported authentication configuration XML files directly into the QField application directory on your mobile device.

!!! Workflow
    1. Export the authentication configuration XML file from QGIS.
    2. Copy the exported XML file into the `QField/Auth` directory inside your device [App Directory](../../how-to/project-setup/storage.md#5-qfield-app-directory).
    3. Launch QField and open your project.

!!! Tip
    For interactive authentication methods (such as OAuth2), QField opens an in-app browser dialog prompting for user credentials, passwords, or two-factor authentication (2FA) verification codes when connecting to services.
