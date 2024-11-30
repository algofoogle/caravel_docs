#!/usr/bin/bash

# This will delete the 'build/' static output,
# then run a web server on https://localhost:8000/ that does
# live rebuilding as you edit the source files. Great for dev/debug!

make clean
sphinx-autobuild source build --host 0.0.0.0

