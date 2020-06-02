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

project = 'Build The Earth'
copyright = '2020, Build The Earth Contributors'
author = 'Build The Earth Contributors'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Internationalisation Options --------------------------------------------
language = 'en'
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Material theme options (see theme.conf for more information)-------------
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Build The Earth Guide',

    # This option is disabled, modify the logo (touch_icon) via _templates/header.html
    #'logo': 'img/BTEarth.gif',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Specify a base_url used to generate sitemap.xml. If not specified, then
    # no sitemap will be built.
    #'base_url': 'https://project.github.io/project',

    # Set the repo location to get a badge with stats
    #'repo_url': 'https://github.com/project/project/',
    #'repo_name': 'Project',

    'html_minify': True,
    'css_minify': True,

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,

    # Set your GA account ID to enable tracking
    #'google_analytics_account': 'UA-XXXXX',
}