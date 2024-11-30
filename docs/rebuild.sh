#!/usr/bin/bash

# This will delete the static contents of build/ and
# then rebuild the static HTML output, as though it is ready for web hosting.

make clean
make html

