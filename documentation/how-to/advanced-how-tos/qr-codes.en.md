---
title: QR Codes
tx_slug: documentation_qr_codes
---

# QR Codes in QField

QField can leverage QR codes in multiple ways. This page lists a couple of ways authors can leverage this to easily share their projects and plugins.

## Projects

QR codes can be generated for users to scan them on their devices and automatically open QField to initiate a project download.

### Cloud projects hosted on QFieldCloud

The easiest way to share a project with your co-workers or the public is through QFieldCloud.

QR codes for QFieldCloud projects allow authors to automatically launch QField and immediately open a given cloud project details page where users can access information such as the title and the description as well as author information. From there, the user can immediately download and open the project.

The URI to generate a QR code to bring QField directly to a cloud project is as follow:

`qfield://cloud?project=username/project_name`

Simply replace username with a QFieldCloud user account and project_name with an actual project name tied to the user account.

If a project is not public, the logged in QFieldCloud user account of the device scanning the QR code will determine whether a given project details and ability to download it will be offered. In addition to access and permission management functionalities offered by QFieldCloud, authors can also benefit from its synchronization abilities to keep their project up-to-date.

### Compressed projects uploaded on the web

The importing of compressed projects uploaded on the web into QField can be simplified through QR codes. When scanning such a code, QField will launch and open a project import permission dialog.

The URI to generate such a QR code is as follow:

`qfield://local?import=https://www.public.com/project.zip`

Simply replace the https:// part of the URI with a publicly available web hyperlink. Once imported, the project will be located in the local projects and datasets' "Imported Projects" folder.

## Application plugin QR codes

QField's plugin manager popup allows users to install application plugins from a URL. The installation dialog has a nifty QR code button that allow for users to quickly scan a URL pointing to a compressed application plugin and install it without the need to type in anything.

The QR code itself is a simple web URL pointing to a compressed application plugin file as the QR code.
