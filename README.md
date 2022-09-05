# QField Documentation
This is the documentation for the QField Ecosystem composed by QField, QFieldCloud and QFieldSync.
The documentation is deployed [here](https://docs.qfield.org).

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa],
feel free to use it accordingly and to contribute back your updates via a
[pull request](https://github.com/opengisch/QField-docs/pulls).


[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

## Structure

(Inspired by https://documentation.divio.com/)

The documentation is structured in four separated topics:

  * Get Started
  * How-to guides
  * Technical references
  * Background information

### Get Started

Contains lessons that take the reader by the hand through a series of
steps to complete a project of some kind. They are what your project
needs in order to show a beginner that they can achieve something with
it.

They are wholly learning-oriented, and specifically, they are oriented
towards learning _how_ rather than learning _that_.

### How-to guides

How-to guides take the reader through the steps required to solve a
real-world problem.

They are recipes, directions to achieve a specific end - for example:
how to create a web form; how to plot a three-dimensional data-set;
how to enable LDAP authentication.

### Technical references

Reference guides are technical descriptions of the machinery and how
to operate it.

Reference guides have one job only: to describe. They are
code-determined, because ultimately that’s what they describe: key
classes, functions, APIs, and so they should list things like
functions, fields, attributes and methods, and set out how to use
them.

### Background information

Explanation to clarify and illuminate a particular topic. They broaden
the documentation’s coverage of a topic.

## Process

The documentation is written in English and managed in this git
repository. The latest version of the documentation is automatically
built by a Github action and published on the links above.

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
where all the real documentation text is located.

#### Testing your changes

```sh
pipenv run pip install transifex-client
pipenv install -r requirements.txt
pipenv run mkdocs serve
```

The local doc will be available at http://localhost:8000

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
[open an issue](https://github.com/opengisch/QField-docs/issues/new) and tell us which
language you would like to translate it to.
