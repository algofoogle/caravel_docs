# SPDX-FileCopyrightText: 2024 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from docutils import nodes
from docutils.parsers.rst import roles


# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Caravel Frame and SoC'
copyright = '2024, Efabless'
author = 'Efabless'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.ifconfig',
    'sphinxcontrib.wavedrom', # For rendering register diagrams.
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_new_tab_link',
    'sphinx_wagtail_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    'build',
    'Thumbs.db',
    '.DS_Store',
    '.gitignore',
    'requirements.txt',
    '.keep',
    # Files included in other rst files.
    'introduction.rst', # Included in index.rst
]

master_doc = "index"
today_fmt = "%Y-%m-%d %H:%M"
todo_include_todos = True
numfig = True

# Hack to put a DRAFT warning message on every page:
rst_prolog = """
.. danger::
    **This documentation is an early work-in-progress and should not be used yet!**

.. danger::
    **Before public release,** fix 'Edit on GitHub' via ``html_theme_options['github_url']``
"""

# A handler for the 'tbc' role, i.e. "to be confirmed" text:
def tbc_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
  """Role for marking text as 'to be confirmed'."""
  node = nodes.inline(text, text, classes=['to-be-confirmed'])
  return [node], []
roles.register_local_role('tbc', tbc_role)



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_wagtail_theme'
html_show_sphinx = False # Hide footer Sphinx/Wagtail links; formatting is broken.
html_last_updated_fmt = today_fmt
html_favicon = '_static/i/Efabless-globe-favicon-192.png'
html_static_path = ['_static']
html_extra_path = [
    '_static/i/efabless-logo-dark-bg.png', # Force Efabless logo build, so Wagtail theme can use it.
]
new_tab_link_show_external_link_icon = True

html_css_files = ['css/custom.css']

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = project, # Alternative title for header bar.
    logo = "i/efabless-logo-dark-bg.png", # I've found this needs to be in html_extra_path.
    logo_alt = "Efabless",
    logo_url = "/",
    logo_width = 125,
    logo_height = 30,
    github_url = "https://github.com/algofoogle/caravel_docs/blob/main/docs/source/",
    header_links = "Efabless.com|https://efabless.com, GitHub/efabless|https://github.com/efabless", # In top-right corner of header bar
    footer_links = ",".join([
        "Efabless.com|https://efabless.com",
        "Efabless Knowledgebase|https://info.efabless.com/knowledge-base",
        "caravel_user_project|https://github.com/efabless/caravel_user_project",
    ]),
)

html_sidebars = {"**": [
    "searchbox.html",
    "globaltoc.html",
    "menu_footer.html",    # Extra HTML in menu_footer.html displays at bottom of sidebar menu.
]}

