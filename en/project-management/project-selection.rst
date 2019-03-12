Project selection
=================

QField opens QGIS projects in the ".qgs" format. Currently it is not possible to open ".qgz" files.

OField uses a customized file selector to open the projects. On choosing "Open project" from the QField menu, the file selector will be opened showing the roots:

- The primary media/shared storage directory returned by Environment.getExternalStorageDirectory()
- The application-specific directories on all shared/external storage devices where the application can place persistent files it owns if they are not already included in the primary storage directory.

Inside these directories, only subdirectories and files with the ".qgs" extension are shown.

QField requires the project file to be physically on the device, so it is not possible to use providers that work with remote files (e.g. Google Drive). On the other hand you can use apps like `syncthing <https://syncthing.net/>_` or `nextcloud <https://nextcloud.com/>`_ (or dropbox and probably many others) that allow you tho physically sync the file to your device.

External SD card
----------------
The file selector only shows the application-specific directory on an external SD card, as it is the only directory for which the app has write access. The directory is the following:

.. code-block:: none

    /Android/data/ch.opengis.qfield/files

Warning!
--------
By storing data in this folder, you risk losing data.
The application-specific directory (`/Android/data/ch.opengis.qfield/`) will be deleted by the system if you uninstall QField from your Android device. This is important if you keep the data in the External sd card.

How to turn external SD card into internal storage on Android 6 and 7.
--------
We recommend to turn external SD cards to internal storage.

NOTE: Please be sure you start with a blank SD card. It needs to be blank because when the card is converted to "Internal" storage, it will be formatted (wiped) and encoded (making the cards data only readable by that device).

1. Go to device “Settings”, then select “Storage”.
2. Select your "SD Card", then tap the “three-dot menu“ (top-right), now select “Settings” from in there.
3. Now select “Format as internal”, and then “Erase & Format”.
4. Your SD Card will now be formatted as internal storage.
5. Reboot your phone.

NOTE: If you don't reboot the phone, many things may not work correctly, so make sure you do.
