---
title: Technical specs
tx_slug: documentation_reference_qfieldcloud_specs
---

## Firewall configuration

If a project contains online layers (PostGIS, WMS, WFS, etc), QFieldCloud will try to establish a connection to this services. Sometimes these services are behind a firewall and the system administrators need to allowlist the QFieldCloud IP.

| service          | IP              |
|------------------|-----------------|
| app.qfield.cloud | 159.100.252.133 |
| app.qfield.cloud | 194.182.188.113 |


## PostgreSQL configuration

If your project contains PostgreSQL (PostGIS) layers, you need to configure your PostgreSQL server so it allows connection from `app.qfield.cloud` IP address.

Otherwise, you will get an error like this:

```
FATAL: no pg_hba.conf entry for host "185.203.114.168", user "qfc", database "mydb_test", SSL off
WARNING:QGIS_MSGLOG:1 unavailable layer(s) found:
```

To do so, you need to edit the `pg_hba.conf` file where your PostgreSQL server is hosted. For more information, refer to recommendations on [StackOverflow questions](https://stackoverflow.com/search?q=FATAL+no+pg_hba.conf+entry+for+host).<!-- markdown-link-check-disable-line -->
