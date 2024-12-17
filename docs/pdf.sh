#!/usr/bin/bash
make clean
DRAFT="${DRAFT:-False}" make simplepdf && ls -alh build/simplepdf/caravel_frame_and_soc.pdf

