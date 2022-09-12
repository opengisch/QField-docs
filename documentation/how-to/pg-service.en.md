---
title: PostgreSQL service
---

# PostgreSQL service

A `pg_service.conf` file allows to use an named alias for a PostgreSQL server connection. Instead of storing hostname, port, database name and more into the QGIS Project file, these can be stored separately. It is even possible to store username and password in a `pg_service.conf` file, to avoid having this stored in clear text in the QGIS Project.

Read more about PostgreSQL services in the [QGIS documentation](https://docs.qgis.org/3.22/en/docs/user_manual/managing_data_source/opening_data.html#postgresql-service-connection-file).

# QField - Direct Connection

If you directly connect from QGIS to your database you can make use of a `pg_service.conf` file by placing it in the QField data folder. You can place your file either on the Internal Device Storage or on the SD Card Storage. You can check the path for the QField data folder in the bottom of the `About QField` screen in the app.

Usually the path on Android devices looks something like this: `/Android/data/ch.opengis.qfield/files/QField`.

!!! note
    Unlike on *NIX systems where the file is named `.pg_service.conf`, the file on Android is named `pg_service.conf` without a leading dot sign (`.`).

# QFieldCloud

QFieldCloud support `pg_service.conf` configurations too. You need to configure your PostgreSQL layers with "Offline editing" cloud action and store your service settings on QFieldCloud Project's Secrets page.

Read more [how to configure PostgreSQL service](../reference/qfieldcloud/secrets.md) in the QFieldCloud documentation.
