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

.. todo::
    Include a general summary in here of each of the features, then link to their respective sections, as this page sort of does: https://caravel-mgmt-soc-litex.readthedocs.io/en/latest/

.. todo::
    How do we offer a "quick-start, essentials-only, what you need to know" guide or summary on things?
    Should it be the above proposed high-level list of features you need to know about and their default state, noting that their default state is a sensible starting point for maximal usability? **OR** should it be a summary panel at the start of every page: "The essentials you need to know about X: You don't need to worry about it". **OR** should both of these things be done?

As a padframe, Caravel offers easy-to-connect standard features such as GPIO pins, power delivery (optionally with multple power domains), clocking, and reset logic (both a dedicated reset pin, and a :term:`POR` circuit). These are well-characterized and qualified to reduce the overhead of the designer.

As an :term:`SoC`, Caravel provides a wide range of optional functionality on-chip that can either be largely ignored or can be used for any of :term:`bringing up <bring-up>` your design, debugging and providing a diagnostic/maintenance interface, controlling different peripherals that your design can leverage, or even as a full microcontroller (including CPU with external firmware interface, basic UART, and SPI controller).



Caravel Padframe General Features
---------------------------------

These features are universally available to any chip based on the Caravel frame, even without specific use of the **Management SoC**.

*   **10mm² "user project wrapper" design area**.
*   **Housekeeping SPI (HKSPI)** interface for an external SPI controller to assert debugging control over certain base configuration, debugging, and clocking of the chip.
*   **38 GPIOs**:

    *   Can be configured (and reconfigured via CPU firmware or HKSPI) to function as outputs, bidirectional, or inputs (including optional pull-up or pull-down).
    *   33 support power-on default configuration, specified in silicon by the designer.
    *   29 support direct pad connections for analog signals [#f1]_.
    *   **For Caravan**: 11 are "bare analog" pads without GPIO circuitry and without ESD protection.
*   **Dedicated clock input pin** (optional).
*   **DLL (similar to a PLL) for clocking control** (or available to be used as an internal "DCO" ring-oscillator clock), delivering 2 independently-configurable clock sources, and the option to output clocks directly on GPIO pins.
*   **POR (Power-On Reset) module**.
*   **SPI pass-through** interface able to be driven via HKSPI to take control (for reading/writing) of a firmware SPI ROM connected to the Management SoC.
*   **Support for digital, analog, and mixed-signal projects**.
*   **4 power domains**; two intended as nominal 1.8V digital supplies, two intended as analog supplies in the range 1.8V to 5.5V.

.. note::

    The DLL/DCO is inactive by default, passing the optional dedicated clock input directly through to the user project wrapper. If the DLL/DCO is to be used, it must be explicitly enabled via HKSPI or firmware running on the **Management SoC**. For more information, see the section on **Clocking, DLL and DCO**.



Caravel Management SoC Features
-------------------------------

The Management SoC's RISC-V CPU (RV32I) is built into the die area, adjacent the user project wrapper, and can be interfaced with your design, as well as externally to the chip.

The SoC is generated using Litex and includes the following peripherals and capabilities that can be optionally enabled/disabled on subsets of the GPIO pins, to make the SoC useful both as a general-purpose microcontroller and a specialized test/debug interface for your design:

*   **VexRiscv core**: VexRiscv minimal+debug configuration.
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
*   **Dedicated power domain**.

.. note::

    If you don't intend to make use of the Management SoC at all, you can simply choose to not connect to its ports in the users project wrapper, and you can optionally tie its ``RESETb`` signal low externally to hold it in reset.

.. todo::

    Need a block diagram to show separation between SoC/chip and its pins on either side.


.. rubric:: Footnotes

.. [#f1] Caravel direct analog pad connections include ESD protection which typically limits full swing signals to about 50MHz.
