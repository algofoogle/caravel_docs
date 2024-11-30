# Documentation source for Caravel Frame and SoC

This is the Sphinx source code for new Caravel "readthedocs"-style documentation intended to replace (or at least supersede) https://caravel-mgmt-soc-litex.readthedocs.io and https://caravel-harness.readthedocs.io

## Decisions made

*   Continue using Sphinx as the documentation compiler, for compatibility with existing docs.
*   Retain the [`docs/`](./docs/) subdirectory so this can be planted into an existing repo (say, [caravel]) later.
*   Switch to the [Wagtail theme](https://sphinx-wagtail-theme.readthedocs.io/) because it looks nice, supports full-width layouts and mobile views, and renders complex tables more sensibly.


## Setting up

```bash
python3 -m venv --prompt caravel_docs .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
```


## Building and viewing the documentation

> [!NOTE]
> I built this using Sphinx 7.3.7 which is the default that pip installed.

First:

```bash
source .venv/bin/activate
cd docs
```

Then for each build:

```bash
make html  # Updates docs/build/html/
```

And to view it (maybe persisting in a separate terminal):

```bash
python3 -m http.server --directory build/html
```

...and open http://localhost:8000/ in a web browser.


## Viewing live updates during development

Instead of doing a manual build (e.g. `make html` then running the Python HTTP server), you can set up a live build-and-serve process that watches as you update source files:

```bash
sphinx-autobuild source build --host 0.0.0.0
```


## Editing

I use VSCode. I have these extensions installed (but not sure whether I actually *benefit* from all or not):
*   [reStructuredText][rst] (`lextudio.restructuredtext`)
*   [reStructuredText Syntax highlighting][rstsh] (`trond-snekvik.simple-rst`)
*   [Esbonio][esbonio] (`swyddfa.esbonio`) -- I'm not sold on this one yet. It always complains about the server not working. Not sure what it's actually for, but I think it's bundled with the "reStructuredText" extension above anyway, and it's maybe for analyzing your content/doctree to provide easier cross-linking and intellisense...?


## Customization

[`docs/source/conf.py`](./docs/source/conf.py) contains Sphinx configuration for how this documentation should be built, and its appearance.


## readthedocs

[readthedocs.io](https://readthedocs.io) is a service which automates the building and hosting of documentation, typically using Sphinx. It can watch pushes to this repo and automatically handle building/deployment. It relies on [`.readthedocs.yaml`](./.readthedocs.yaml)


[caravel]: https://github.com/efabless/caravel
[rst]: https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext
[rstsh]: https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst
[esbonio]: https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio
