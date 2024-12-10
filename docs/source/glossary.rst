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
