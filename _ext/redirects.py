"""
    sphinxcontrib.redirects
    ~~~~~~~~~~~~~~~~~~~~~~~
    https://github.com/mbernasocchi/redirects

    Generate redirects for moved pages when using the HTML builder.

    See the README file for details.

    :copyright: Copyright 2017 by Stephen Finucane <stephen@that.guru>
    :license: BSD, see LICENSE for details.
"""

import os

from sphinx.builders import html as builders
from sphinx.builders import linkcheck as linkcheckbuilders
from sphinx.util import logging

TEMPLATE = """<html>
  <head><meta http-equiv="refresh" content="0; url={to_path}"/></head>
  <body>
  This page has moved. Redirecting...
  <script>
  window.location.href = '{to_path}' + (window.location.search || '') + (window.location.hash || '');
  </script>
  </body>
</html>
"""


def generate_redirects(app):
    logger = logging.getLogger(__name__)

    path = os.path.join(app.srcdir, app.config.redirects_file)
    if not os.path.exists(path):
        logging.warning("Could not find redirects file at '%s'" % path)
        return

    in_suffix = app.config.source_suffix
    if isinstance(in_suffix, list):
        in_suffix = in_suffix[0]
    elif isinstance(in_suffix, dict):
        logger.warning("app.config.source_suffix is a dictionary type. "
                 "Defaulting source_suffix to '.rst'")
        in_suffix = ".rst"

    if type(app.builder) == linkcheckbuilders.CheckExternalLinksBuilder:
        logger.warning("Detected 'linkcheck' builder in use so skipping generating redirects")
        return

    if not (type(app.builder) == builders.StandaloneHTMLBuilder or type(app.builder) == builders.DirectoryHTMLBuilder):
        logger.warning("The 'sphinxcontib-redirects' plugin is only supported "
                 "by the 'html' and 'dirhtml' builder, but you are using '%s'. Skipping..." % type(app.builder))

    dirhtml = False
    if type(app.builder) == builders.DirectoryHTMLBuilder:
        dirhtml = True

    with open(path) as redirects:
        for line in redirects.readlines():
            from_path, to_path = line.rstrip().split(' ')

            logger.debug("Redirecting '%s' to '%s'" % (from_path, to_path))

            if dirhtml:
                from_path = from_path.replace(in_suffix, '/index.html')
            else:
                from_path = from_path.replace(in_suffix, '.html')

            if dirhtml:
                to_path = to_path.replace(in_suffix, '/')
            else:
                to_path = to_path.replace(in_suffix, '.html')

            to_path_prefix = '..%s' % os.path.sep * (
                len(from_path.split(os.path.sep)) - 1)
            to_path = to_path_prefix + to_path

            logger.debug("Resolved redirect '%s' to '%s'" % (from_path, to_path))

            redirected_filename = os.path.join(app.builder.outdir, from_path)
            redirected_directory = os.path.dirname(redirected_filename)
            if not os.path.exists(redirected_directory):
                os.makedirs(redirected_directory)

            with open(redirected_filename, 'w') as f:
                f.write(TEMPLATE.format(to_path=to_path))


def setup(app):
    app.add_config_value('redirects_file', 'redirects', 'env')
    app.connect('builder-inited', generate_redirects)
