import sphinx_fontawesome
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Damian Krawczyk'
copyright = '2021, Damian Krawczyk'
author = 'Damian Krawczyk'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_fontawesome",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = "Damian Krawczyk"

html_show_sphinx = False

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#586069",
        "color-brand-content": "#586069",
    },
    "navigation_with_keys": True,
}
html_logo = "_static/img/pic.png"
html_css_files = [
    "css/custom.css",
    "css/font-awesome.css",
]

# https://www.sphinx-doc.org/en/master/usage/advanced/intl.html#quick-guide
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# https://docs.readthedocs.io/en/stable/guides/manage-translations.html
gettext_uuid = True

rst_prolog =  sphinx_fontawesome.prolog + """
.. General:
.. |me| replace:: :abbr:`me (Damian Krawczyk)`

.. |GUI| replace:: :abbr:`GUI (Graphical User Interface)`
.. |csv| replace:: :abbr:`csv (comma-separated value)`
.. |xlsx| replace:: :abbr:`xlsx (Microsoft Excel Open XML Spreadsheet)`
.. |VA| replace:: :abbr:`VA (Vulnerability Assessment)`

.. |GPI| replace:: :abbr:`GPI (GOV PL Info)`
.. |GIS| replace:: :abbr:`GIS (Główny Inspektorat Sanitarny)`
.. |MSI| replace:: :abbr:`MSI (Main Sanitary Inspectorate)`
.. |GIF| replace:: :abbr:`GIF (Główny Inspektorat Farmaceutyczny)`
.. |MPI| replace:: :abbr:`MPI (Main Pharmaceutical Inspectorate)`
.. |GUS| replace:: :abbr:`GUS (Główny Urząd Statystyczny)`
.. |CSO| replace:: :abbr:`CSO (Central Statistical Office)`


.. |CET| replace:: :abbr:`CET (Central European Time)`
.. |CEST| replace:: :abbr:`CEST (Central European Summer Time)`
"""