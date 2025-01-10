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

Glossary
========

.. glossary::
   :sorted:

   bring-up
      The process of getting a chip to operate for the first time after receiving it as a fabricated device.
      During this time, many measurements and experiments may be required, as well as debugging.
      This includes to verify that the core features of the frame/SoC are functioning as expected,
      and that your design is able to respond in a set of your own expectations.

   Caravel SoC
      :tbc:`Define me`

   Management SoC
      :tbc:`Define me`

   Management Area
      :tbc:`Define me`

   Management Core Wrapper
      :tbc:`Define me`

   Management Core
      :tbc:`Define me`

   PLL
      Phase-Locked Loop. A device commonly used in FPGAs and in Caravel to derive a new clock frequency/phase from a supplied clock source. Typically allows for a clock source to be multiplied in frequency by an integer value, and then divided by a second integer value to produce a new clock frequency. Sometimes may offer multiple multipliers/dividers in order to produce multiple clocks. Compare: :term:`DLL`
      
   DLL
      Delay-Locked Loop. Very similar to a :term:`PLL`. In Caravel, :ref:`there is a DLL <dll>` which is an all-digital SoC peripheral that can be used to generate new clock frequencies from an internal or external clock source.

   SPI
      `Serial Peripheral Interface <https://en.wikipedia.org/wiki/Serial_Peripheral_Interface>`_. A common 4-wire interface for simple serial communication with a peripheral device, driven by a controller. Often used between chips, and capable of multi-megabit-per-second transfers.

   crt0
      Initial "C Runtime" bootstrapping routines. Code built into the assembly process of a C program that is executed before the ``main()`` function is called. Responsible for loading the initial system/memory state, including initializing any global/static variables and optionally loading read-only data.

   PVT
      Short for "Process, Voltage, Temperature" and typically used in the context "PVT-dependent", meaning that the exact behaviour/characteristics of something is affected (or otherwise likely to deviate from typical stated figures) by virtue of: variations that naturally occur in the fabrication process; variations in precise voltages in the circuit; and variations in ambient temperature.
   
   Caravel Eval Board
      The bring-up/development/evaluation board for chipIgnite/Caravel chips. Typically one board is supplied with every chipIgnite order that includes QFN-packaged Caravel chips. For more information, see https://github.com/efabless/caravel_board and note that you can `purchase a demo board from the Efabless Store <https://store.efabless.com/products/chipignite-demo-board>`_ -- the demo board includes 1 Caravel demo chip.

   Project ID
      Every unique silicon layout (e.g. customer project) fabricated with Efabless chipIgnite has a unique 32-bit "Project ID" assigned by Efabless and included in the silicon layout. The Project ID is accessible by the Caravel SoC (and via :doc:`HKSPI <housekeeping>`) as a read-only 32-bit value, but is also present as "GDS art" text in the padring, rendered as 8 hex digits. Most Project IDs are of the pattern ``YYMMhhhh`` where ``hhhh`` is a random value assigned by Efabless at the initialization of the project, and ``YYMM`` is the shuttle number (e.g. ``2409``) and itself is formed of the last two digits of the shuttle year and the month number. An example Project ID (as a hex string) is ``240476A0`` which is `Tiny Tapeout 6 <https://tinytapeout.com/runs/tt06/>`_, on the April 2024 shuttle.

      Note that when using the SoC or HKSPI to read the 32-bit value of the Project ID, some shuttles had the project ID bits in reverse order, e.g. ``240476A0`` (which in binary is ``0010_0100_0000_0100_0111_0110_1010_0000``) would be read as ``056E2024`` (which is the binary string in reverse: ``0000_0101_0110_1110_0010_0000_0010_0100``).

   QFN
      `Quad Flat No-leads IC package <https://en.wikipedia.org/wiki/Flat_no-leads_package>`_. A plastic-encapsulated chip package with pin pads around all 4 sides.

   WLCSP
      `Wafer-Level redistribution Chip-Scale Package <https://en.wikipedia.org/wiki/Chip-scale_package>`_. A minimal chip package usually with a "redistribution" layer that attaches bare bond pads of a silicon die to ball grid array (BGA) solder balls via tiny wires.

   SoC
      System on a Chip. A combination of chip modules that provide a system of functionality, often including a CPU and other useful peripheral devices implemented in silicon.

   POR
      Power-On Reset. A circuit that ensures a stable reset sequence during chip power-on, thus ensuring a stable system state if a dedicated external reset is not otherwise implemented.

   User Project Wrapper
      The design area reserved for a user project. It has a fixed location and dimensions within the overall Caravel chip die area, and fixed pin placements around all 4 edges that a user design must connect to in order to interface with the Caravel SoC and/or GPIOs.

      Typically the User Project Wrapper also has a :term:`PDN` that is generated by the :term:`hardening` flow.

   UPW
      Short for :term:`User Project Wrapper`.

   PDN
      Power Delivery Network.

   Hardening
      The process of generating a final silicon layout (and hence :term:`GDS` file) from potentially multiple parts, including synthesis of higher-level descriptions of digital logic.

   GDS
      :tbc:`Define me`

   Litex
      :tbc:`Define me`

   VexRiscv
      :tbc:`Define me`

   XIP
      Execute In Place: Code is directly loaded and executed from an external memory as needed, without the need for user-driven caching control, buffering, translation, logic, etc.

   Active-low
      A signal whose named intent/mode is considered to be asserted when the signal is low (i.e. logic 0, or GND), and deasserted when the signal is high (i.e. logic 1, or positive). Sometimes also referred to as "inverted logic" or "negative logic". Example: A device with an input signal name like ``reset_n`` (note the ``_n`` suffix) is considered to actively be in the "reset" state when the signal is low, and otherwise running normally (and not in reset) when the signal is high. A similar convention is ``resetb`` where the ``b`` suffix means ":term:`Bar`".

   Bar
      Used as a suffix (e.g. "Output Enable Bar"), this typically means the signal is ":term:`active-low`". In the name of a signal, this is often indicated by a ``b`` or ``_b`` suffix (e.g. ``oeb`` might mean "Output Enable Bar"), where the name would normally be rendered in a schematic with a horizontal line (or "bar") over the signal name.