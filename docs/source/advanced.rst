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

Advanced Guides
===============

Executing code from RAM
-----------------------

Custom ISRs
-----------

Power-on behavior
-----------------

Management Core wrapper
-----------------------

The Caravel "Management Core Wrapper" is designed in a way to allow the implementation of different management cores. Early versions of the Google-sponsored "Open MPW" Caravel SoCs used a PicoRV32 core, while the current version officially offered by Efabless is "Caravel V6.0" (in use since Open MPW-6) and is generated using Litex with a VexRiscv CPU core.

The common parts of the management core wrapper include:

*  Housekeeping and HKSPI.
*  GPIO configuration blocks (power-on defaults and runtime-reprogrammable).
*  User Project Wrapper interface pins, namely: Logic Analyzer; IRQs; Wishbone (inc. ``wb_rst_i``, and ``wb_clk_i`` and ``user_clock2`` clock sources); and power rings (for a :abbr:`PDN (Power Delivery Network)` of up to 4 power domains).
*  Management protection.
*  Clocking module (DLL/DCO).
*  POR (Power-On Reset) module.


Building Caravel using Litex
----------------------------
