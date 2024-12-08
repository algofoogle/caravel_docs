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

Clocking and DLL/DCO
====================

.. todo::
   Put in DLL/DCO/clocking diagram inc. register names.

.. todo::
   Simplify the idea that there is a DCO, DLL, and configurable dividers (as well as bypass). Maybe the diagram above will do this. Otherwise it's confusing: The DCO can be 'divided', but with feedback it becomes a DLL.

You may choose to make your user project design take its clock(s) from any sources you like (including your own internal oscillator, Caravel-CPU-controlled logic, or any GPIO pin). However, Caravel offers two dedicated clock paths internally: ``wb_clk_i`` :tbc:`(also called "core_clock")` and ``user_clock2``. These have :tbc:`known timing characteristics` and can either be derived from Caravel's internal ring oscillator (:ref:`DCO <dco>`) or from Caravel's external dedicated :ref:`clock <clock>` input pin -- in both cases optionally also being modified by the DLL/divider circuits as described below.

.. _dll:

DLL (Delay-Locked Loop)
-----------------------

.. |clock| replace:: :code:`clock`

The Caravel DLL is like a :term:`PLL` as found in an FPGA. The Caravel frame has a dedicated :ref:`"clock"  <clock>` input pin.

.. _dco:

DCO (Digitally-Controlled Oscillator)
-------------------------------------

This is an internal ring oscillator with a fixed base frequency and which can be "trimmed" by up to 26 steps to control its actual output frequency. This allows it to be used as a direct internal clock source for the Caravel SoC and user project, before optionally being divided by two independent 

It is used by the DLL to generate a :tbc:`reasonably stable` multiple of the input clock source, but can
also be used simply as a direct clock source for Caravel without an input clock source.

Note that the actual internal DCO frequency is :term:`PVT`-dependent.

.. _user_clock2:

user_clock2
-----------

When the DLL is enabled, the clock source feeding ``user_clock2``'s divider is 90 degrees out of phase. That is, ``user_clock2`` lags ``wb_clk_i`` by a quarter-cycle.
