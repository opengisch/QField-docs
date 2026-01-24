---
title: FAQ
tx_slug: documentation_get-started_faq
---

# Frequently Asked Questions

## Billing and Plans

??? help "What is the difference between "metered" and "licensed" users on my invoice?"

    ## What is the difference between the metered and licensed users on my invoice?
    By default when subscribing to an organization plan, at least two users need will be paid on a monthly basis.
    Even if the user is not active, at least two users will always be billed.
    The **metered user**, on the other hand, are billed upon activity.
    This means that as soon as a "job" is executed, the user will be counted as an active user.
    The metered users are always billed retrospectively (eg. in February, you will be billed for the metered user from January).

??? help "Why am I still being invoiced? I cancelled my subscription already."

    ## Why am I still being invoiced? I cancelled my subscription already.
    In QFieldCloud there are two billing pages.
    One for your personal account and one for your organization(s).
    Make sure that you cancel all subscriptions, if you do not wish to use it anymore.
    Otherwise, you will be invoiced monthly.

??? help "Is it possible to pay by invoice on a monthly basis?"

    No, unfortunately, we only offer invoice for an annual subscription with a one-off administration fee.

## Configuration questions in QField

??? help "How do I fix issues with missing or broken layers after syncing?"

    Ensure all layers are stored in the same local project folder before uploading.
    Convert all layers to GeoPackage format and use relative paths.

??? help "What should I do if my project fails to package or synchronize?"

    - Check for invalid geometries using the “Fix Geometries” tool in QGIS.
    - Avoid absolute paths in your project.
    - Make sure you’re using the latest versions of QGIS, QField, and QFieldSync.

??? help "How do I handle attachments and images?"

    Use the DCIM folder for images.
    To save space or more quick synchronizations, set a maximum picture size (e.g., 800px).
    Attachments should be referenced by relative paths.

??? help "How do I record heights or my location coordinates in QField?"
    Activate “Coordinate cursor locked to position” and use expressions like z(@position_coordinate) or z(@gnss_coordinate) (if you are using an external GNSS device) for height in this [section](../reference/expression_variables.md) a list with more variables available.
    If you are using your internal device use "position_"
    If you are using an external GNSS device use "gnss_"

## General

??? help "How many versions of a file are stored on QFieldCloud?"

    How many versions of a file are stored on QFieldCloud?
    The number of stored file versions depends on the account type. 3 versions are stored for COMMUNITY account, and 10 for other account types.

??? help "How can I delete old file versions?"

    How can I delete old file versions?
    You can delete old versions of a file, except for the latest version, from QFieldSync or the QFieldCloud web interface. When you remove a version, all previous versions are also removed.

??? help "Which browsers are supported by QFieldCloud?"

    Which browsers are supported by QFieldCloud?
    We try to ensure compatibility with recent (up to one year old) versions of Firefox, Chromium-based browsers (e.g. Chrome and Edge) and Safari.

??? help "Is there a maximum duration that an action can take on QFieldCloud?"

    Is there a maximum duration that an action can take on QFieldCloud?
    QFieldCloud jobs should finish in 10 minutes, otherwise they are terminated. If you have special needs you can [contact us](mailto:info@opengis.ch) to find an ad hoc solution.

??? help "I have a question about QField or QFieldCloud. Who can I ask?"

    I have a question about QField or QFieldCloud. Who can I ask?
    We have a [discussion platform](https://github.com/opengisch/QField/discussions) to connect with other members of our community. If you need professional support please [contact us](mailto:info@opengis.ch).

You can find more plans and service related questions in the [QFieldCloud FAQ](https://qfield.cloud/faq) page.
