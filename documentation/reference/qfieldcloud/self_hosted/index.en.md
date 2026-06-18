---
title: QFieldCloud Self-Hosting
tx_slug: documentation_reference_qfieldcloud_self_hosted
---

# QFieldCloud Self-Hosting

!!! note
    Most of this documentation site describes QFieldCloud as offered at [app.qfield.cloud](https://app.qfield.cloud). That hosted service runs on the same open-source backend, but adds a polished web frontend as well as account, subscription, and payment management for the hosted offering. Revenues from the hosted service helps fund ongoing development of QField and QFieldCloud.

The full QFieldCloud backend is open source and production-ready. You can self-host it and get everything needed to work with QField and QFieldSync. QFieldCloud also exposes a complete REST API, so you can build your own frontend or integrate it into existing systems. Contributions are welcome via the [contributor guide](https://github.com/opengisch/QFieldCloud#collaboration).

Self-hosting gives you full control over data residency, user management, and configuration.

## Installation

Installation instructions, requirements, and configuration reference are maintained in the QFieldCloud source repository:

[https://github.com/opengisch/QFieldCloud](https://github.com/opengisch/QFieldCloud)

Follow the README and the documentation in that repository to set up and configure your self-hosted instance.

## Administration via the Django admin panel

The documentation in this section covers administration through the built-in Django admin panel. Once your instance is running, see:

- [Django administration interface](django_interface.md) — manage users, organisations, teams, projects, and secrets.
