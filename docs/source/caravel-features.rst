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

Features of Caravel
===================

Caravel includes the following key features:

General
-------

*   **Housekeeping SPI (HKSPI)** interface.
*   **38 GPIOs**:

    *   Can be configured (and reconfigured via CPU firmware or HKSPI) to function as outputs, bidirectional, or inputs (including optional pull-up or pull-down).
    *   33 support power-on default configuration specified by the designer.
    *   29 support direct pad connections for analog signals [#f1]_.
    *   **For Caravan**: 11 are "bare analog" pads without GPIO circuitry and without ESD protection.
*   **DLL (similar to a PLL) for clocking control**, delivering 2 independently-configurable clock sources, and the option to output clocks directly on GPIO pins.
*   **SPI pass-through** interface able to be driven via HKSPI to take control (for reading/writing) of a firmware SPI ROM connected to the Management SoC.
*   **4 power domains**; two intended as nominal 1.8V digital supplies, two intended as analog supplies in the range 1.8V to 5.5V.


Management SoC
--------------

The Management SoC's RISC-V CPU (RV32I) is able to interface with your design in the user project wrapper, and externally to the chip.

The SoC includes the following peripherals and capabilities that can be optionally enabled/disabled on subsets of the GPIO pins, to make the SoC useful both as a general-purpose microcontroller and a specialized test/debug interface for your design:

*   **GPIO control**: Ability to reconfigure the 38 GPIOs (**27 for Caravan**), including taking over GPIOs as "management mode".
*   **Logic Analyzer**: 128 internal IO pins that can optionally be connected with your design in the user project wrapper.
*   **Wishbone master**: 32-bit Classic-Wishbone-based memory map expansion of the CPU.
*   **UART** with fixed baud rate.
*   **SRAM**: 1.5kBytes of local RAM scratch space.
*   **SPI master** for direct control by user firmware.
*   **6 user IRQs**, 3 internally-driven by the user project.
*   **Dedicated firmware ROM SPI master** for XIP loading of firmware code from an external SPI memory into a local 16-word (64-byte) instruction cache.
*   **Counter-timers**.
*   **Single management GPIO pin**.

.. rubric:: Footnotes

.. [#f1] Caravel direct analog pad connections include ESD protection which typically limits full swing signals to about 50MHz.
