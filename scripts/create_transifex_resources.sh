#!/bin/bash

# This script is used to register InaSAFE translatable resources with Transifex
# http://transifex.com
#
# Note that this script updates or creates entries in .tx/config file
#
# Tim Sutton, March 2013

#
# Sphinx documentation first
#

#LOCALES=`ls i18n`
LOCALES='de fr it ro es pl hu pt'

# Exit on error
set -e

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/..

# to be sure there are no pot files left
make clean
make gettext

pushd ${DIR}
for POFILE in `find i18n/pot/${ITEM}/ -type f -name '*.pot'`
do
  # get the po file, replacing 'en' with '<lang>' and removing double '//'s in path
  GENERICFILE=`echo $POFILE | sed 's|//|/|g'`
  # Get the filename-only part of the po file so we can use that
  # name when registering the resource
  BASE=`dirname $GENERICFILE`/`basename $GENERICFILE .pot`
  # replace _ in - in filenames
  # replace empty spaces to -
  # replace / in _
  # replace . to _ (eg for release2.0 names)
  # so we have for a file like
  #   site/about/my_screenshots/index.po
  # we will get
  #   site_about_my-screenshots_index
  RESOURCE=qfield-documentation.`echo $BASE | sed 's|i18n/pot/||g' | sed 's|[_ /\.]|-|g'`
  echo "*** RESOURCE: $RESOURCE"
  # Register each pot file as a transifex resource (an individual translatable file)
  set -x
  tx set -t PO -r $RESOURCE --source -l en "$GENERICFILE"
  #set +x
  # Now register the language translations for the localised po file against
  # this resource.
  for LOCALE in $LOCALES
  do
      echo $POFILE
      LOCALEFILE=`echo $BASE | sed "s|/pot/|/$LOCALE/|g"`.po
      #echo "$LOCALEFILE"
      tx set -r $RESOURCE -l $LOCALE  "$LOCALEFILE"
  done
  # When we are done in this block we should have created a section in the
  # .tx/config file that looks like this:
  #
  #   [qgis-website.site_forusers_alldownloads]
  #   file_filter = i18n/<lang>/LC_MESSAGES/site/forusers/alldownloads.po
  #   source_file = i18n/en/LC_MESSAGES/site/forusers/alldownloads.po
  #   source_lang = en
  #   trans.nl = i18n/nl/LC_MESSAGES/site/forusers/alldownloads.po
  #   type = PO
done
popd

#Print out a listing of all registered resources
#tx status
