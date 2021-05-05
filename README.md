# QField-Documentation
This is the documentation for the [QField project](https://qfield.org)

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa], feel free to use it accordingly and to contribute back your updates via a [pull request](https://github.com/opengisch/QField-docs/pulls).


[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]
[![Build
Status](https://travis-ci.org/opengisch/QField-docs.svg)](https://travis-ci.org/opengisch/QField-docs)

## Resources

The final product can be found at https://qfield.org/docs/. 

The documantation is separated between a documentation for QGIS users (likely a GIS manager) [preparing the project](https://qfield.org/docs/prepare) for field use and a [field worker documentation](https://qfield.org/docs/fieldwork). While the former can go into technical details, we want to keep the field worker documentation very straightforward, easy to use and foremost visual.

## Process

The documentation is written in English and managed in this git repository.
The latest version of the documentation is automatically built (on [Travis
CI](https://travis-ci.org/opengisch/QField-docs)) and published on the links
above.

Translation is done via transifex. The latest translations are pulled and built
on a daily basis (using GitHub actions).

## Contributing

QField is a community driven open source project. As such we are very happy to
get your help and feedback.

Therefore we appreciate if you can help us by

 * Documenting features (in English)
 * Improving the documentation (in English)
 * Translate it to your language

### Documentation process

*Note: You will need a [github account](https://github.com/) for this.*

Navigate to https://github.com/opengisch/QField-docs/ and click the `Fork` link on the top
right. You now have your own copy of the documentation on which you can work
and cannot do any damage, feel free to experiment.
If you want more information about forking you can find it
[here](https://help.github.com/articles/fork-a-repo/).

You most likely want to make changes to the files in the folder `en`. That's
where all the real documentation text is located. The documentation is writtenh
in reStructuredText, a simple syntax to structure the text. You can find
information about it in the [reStructuredText
Primer](http://sphinx-doc.org/rest.html) or by looking at what is already in
the documentation and make your changes according to it.

#### Testing your changes
To quickly test locally the changes you made you can run `make devhtml`from the top-level directory. This will quickly generate the english only version of your new documentation. The HTML will be generated in `build/html/en`. From there you can open `index.html` and explore your local copy of the documentation.

#### Contribute changes

Once you have made changes which you would like to contribute back to the main
documentation, please make a [pull
request](https://help.github.com/articles/using-pull-requests/).

### Translation process

*Note: You will need to have a [transifex account](https://transifex.com/) for this.*

Navigate to our [transifex
project](https://www.transifex.com/organization/opengisch/dashboard/qfield-documentation)
and click on the language you would like to translate. You will see a link
`Join Team`. Click it and wait for approval (you will receive an email).

Once you receive the email you can head back to the transifex project page,
click on your language again and then will have the possibility to choose a
documentation chapter to translate. There is a `Translate` button after
choosing a chapter.

If your language is not yet available, we will happily add it for you. Just
[open an issue](https://github.com/opengisch/QField-docs/g/issues/new) and tell us which
language you would like to translate it to.
