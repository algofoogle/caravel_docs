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
import os
import datetime

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# If DRAFT is True, TODOs are shown, and TBCs are highlighted:
DRAFT = os.environ.get('DRAFT', 'True').lower().strip() in ['true', '1']
# NOTE: DRAFT = True if not specified in environment.
if DRAFT:
    print('************ DRAFT mode ************')
else:
    print('------------ PRODUCTION mode ------------')

project = 'Caravel Frame and SoC'
copyright = '© 2024 Efabless Corporation'
author = 'Efabless'
release = '2024.09.13-1' # This is based on the latest tag: https://github.com/efabless/caravel/tags
version = '6.1.0' # x.y.z: x=Major(MPW version), y=Minor(Frame stepping), z=Revision(doco stepping)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_simplepdf', #NOTE: Not bad, but doesn't work so well yet. Need to find an alternative?
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
if DRAFT:
    todo_include_todos = True
else:
    todo_include_todos = False
numfig = True

# Hack to put a DRAFT warning message on every page:
rst_prolog = """
.. include:: /_templates/substitutions.rst
"""
if DRAFT:
    rst_prolog += """
.. danger::
    **This documentation is an early work-in-progress and should not be used yet!**
    This is being rendered in **DRAFT** mode.

    **Before public release,** fix 'Edit on GitHub' via ``html_theme_options['github_url']``
"""

# A handler for the 'tbc' role, i.e. "to be confirmed" text. This is content
# which we THINK is correct (and can be presented as-is publicy) but probably
# need to be checked for accuracy. In DRAFT mode this content should render
# with a draft-to-be-confirmed style which makes it stand out. In PRODUCTION
# mode this should render with the prod-to-be-confirmed style which has no
# explicit CSS.
def tbc_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for marking text as 'to be confirmed'."""
    node = nodes.inline(text, text, classes=['draft-to-be-confirmed' if DRAFT else 'prod-to-be-confirmed'])
    return [node], []
roles.register_local_role('tbc', tbc_role)

# A handler for the 'todo' role, i.e. inline markers that we need to do
# something more to the content. These are only shown if todo_include_todos is True.
def todo_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for inline 'todo' text."""
    if todo_include_todos:
        node = nodes.inline(text, text, classes=['draft-todo' if DRAFT else 'prod-todo'])
    else:
        node = nodes.inline()
    return [node], []
roles.register_local_role('todo', todo_role)


# A handler for the 'nbar' role, i.e. overbar for active-low signal names:
def nbar_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for marking text as 'to be confirmed'."""
    node = nodes.inline(text, text, classes=['nbar'])
    return [node], []
roles.register_local_role('nbar', nbar_role)


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

html_context = {
    'cover_meta_data': f'{project} documentation',
    # 'cover_logo_title': '<img src="_static/i/efabless-logo-dark-bg.png" />',
    'cover_footer':
        f'Documentation build: {datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}<br>'
        f'<a href="https://efabless.com/">{copyright}</a>',
}

simplepdf_file_name = 'caravel_frame_and_soc.pdf'
# simplepdf_debug = True
simplepdf_vars = {
    #NOTE: These get embedded directly in CSS, so literal strings must be quoted:
    # 'cover-overlay': 'rgba(160, 0, 0, 0.8)',
    'cover-bg': 'url(i/m2-green-on-red-bg.jpg) no-repeat center',
    # 'cover': '#aa0000',
    'cover': '#ffffff',
    'top-right-content': f'"{project} documentation"',
    'bottom-left-content': f'"{copyright}"',
    'bottom-right-content': 'string(heading)',
}
