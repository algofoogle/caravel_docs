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

Firmware, Flash SPI, and Programming Guide
==========================================

Use of the Caravel CPU and other SoC peripherals is optional. Complex user designs can be made that ignore the CPU and SoC completely, but they offer several other advantages also. You might want to use the CPU and |soc| for any of:

*  :term:`Bring-up` and debugging, especially in a prototype where you need to be able to define and inspect internal signals, or otherwise alter aspects of how your design interfaces with the rest of the system and the outside world.
*  As a general-purpose microcontroller, whether in combination with your design, or otherwise separately.
*  As a supervisor to ensure proper operation of your design, especially to enable user project access to :io:`4:0` (i.e. |reserved_gpios|) if specifically required.
*  Diagnostics and maintenance in the field.

If you want the CPU to remain idle/unused, you should strap the |resetb| pin low (i.e. ensure the CPU is always held in reset).

Otherwise, use of the CPU (or SoC typically) requires that the CPU is able to execute firmware code. This section covers:

*  Hardware required to host firmware code that the CPU will execute.
*  Writing C code that is compatible with the RISC-V CPU in general.
*  References to specific C API calls that access hardware and functions of the SoC.
*  Installing and using a compiler that targets the Caravel RISC-V CPU.
*  Simulating execution of your C code on the CPU, and its interaction with the rest of the chip and with your user design.

For details on how to actually deploy firmware code to a Caravel-based development board (with your fabricated chip) and test it, see: :doc:`bringup`.

.. _firmware-spi:

Firmware Flash SPI interface
----------------------------


Writing and compiling basic firmware for the Caravel RISC-V CPU
---------------------------------------------------------------

Writing and simulating testbenches with Verilog or Cocotb
---------------------------------------------------------

Other important programming information
---------------------------------------

.. todo::
   Note the need for ``volatile`` everywhere.
