.. Caravel Frame and SoC documentation master file, by sphinx-quickstart.
   This file should at least contain the root `toctree` directive.

.. raw:: html

   <!---
   # SPDX-FileCopyrightText: 2020 Efabless Corporation
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
   -->

Caravel Frame and SoC documentation
===================================


What is Caravel?
----------------

.. raw:: html

   <p>
   With the free and open-source <strong>Caravel</strong>, you have a ready-to-use chip harness for creating your own ASIC design and getting it fabricated for prototype or production purposes. It includes a blank silicon <strong>design area of 10mm<sup>2</sup></strong> and optional on-chip microcontroller/test framework. You can use it whether you are creating a proprietary/private chip, one for commercial purposes, or an open-source design.
   </p>

"**Caravel**" is both the name of:

*  an **Efabless chipIgnite chip template** (including padring); and
*  its included **ready-made silicon SoC** (system-on-chip, i.e. CPU and other useful devices).
   
These parts are open source, but you may also freely use them for any closed/commercial/private project.

Designing and fabricating an ASIC with `Efabless chipIgnite <https://efabless.com/chipignite>`_ requires that you use an existing supported template (or "frame"), and Caravel is recommended as the most popular, feature-rich, and production-ready template. The chipIgnite submission process automatically integrates your user project design area into the frame, so you don't have to worry about it.

.. hint::
   While this documentation describes **Caravel**, it also covers **Caravan** (our frame with some dedicated bare analog pads, suitable for prototyping) and **Caravel Mini**. All 3 are very similar, with some specific distinctions marked where appropriate.

   For more information about the different frames and options, see: `Which chipIgnite template should I use? <https://info.efabless.com/knowledge-base/whats-the-difference-between-caravel-caravan-and-openframe>`_


.. figure:: _static/i/caravel-floorplan.svg
      :name: caravel_floorplan
      :alt: Caravel Floorplan
      :align: center

      Caravel die floorplan

Table of Contents
=================

.. toctree::
   :maxdepth: 2

   Features <caravel-features>

