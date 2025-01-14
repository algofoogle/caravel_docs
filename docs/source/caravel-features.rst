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

.. todo::

   Need a block diagram to show separation between SoC/chip and its pins on either side.



Caravel Padframe General Features
---------------------------------

These features are universally available to any chip based on the Caravel frame, even without specific use of the **Management SoC**.

Caravel user_project_wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Caravel includes a **10mm² "user project wrapper" design area**. The ``user_project_wrapper`` is what a user submits as a fixed-area :term:`GDS` macro. It is then automatically integrated (by the Efabless chipIgnite submission process) into the rest of the Caravel chip harness to produce the final GDS that is submitted for fabrication. This design area, in the 130nm node, is enough for on the order of :tbc:`6 million transistors or 1 million logic gate primitives`.

The designer can choose whether the design they include in the user project wrapper will interface with the Caravel SoC, the padframe GPIOs, the built-in clock sources, the :term:`PDN` (Power Delivery Network) or any combination of these. For advanced users ordering bare dice and implementing a highly-specialized design, the user design may even use none of these features (though this is not recommended).

The user project wrapper provides **support for digital, analog, and mixed-signal projects**.

See: :ref:`user_project_wrapper`


Housekeeping SPI
^^^^^^^^^^^^^^^^

The chip's power-on state defaults to assigning 4 GPIOs as a **Housekeeping SPI (HKSPI)** interface for an external SPI controller to assert debugging control over certain base configuration, debugging, and clocking of the chip.

This also includes **SPI pass-through**, able to be driven via HKSPI to take control (for reading/writing) of a firmware SPI ROM connected to the Management SoC.

See: :doc:`housekeeping`


38 GPIOs
^^^^^^^^

Caravel provides **38 GPIO pins** that can be used interchangeably by the user's own digital logic, the Caravel CPU, or in some cases as analog connections:

*  These 38 can be configured (and reconfigured via CPU firmware or HKSPI) to function as outputs, bidirectional, or inputs (including optional pull-up or pull-down).
*  They also have built-in |esd| protection, level shifting, and buffering, thus simplifying the job of the designer.
*  33 support power-on default configuration specified in silicon by the designer, while the remaining 5 have Caravel-dedicated power-on functions (that can be overridden by CPU firmware or HKSPI).
*  29 optionally support direct pad connections for analog signals [#f1]_.
*  **For Caravan**: 11 are "bare analog" pads without GPIO circuitry and without |esd| protection.
*  Some offer additional Caravel SoC "management" functions (such as UART and additional debug functions).

See: :doc:`gpio`

.. rubric:: Footnotes

.. [#f1] Caravel direct analog pad connections include |esd| protection which typically limits full swing signals to about 50MHz.


Dedicated clock input and DLL/DCO configurable clocking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Caravel and/or the user design can optionally receive (and modify) a clock signal via a dedicated clock input pin that includes circuitry for multiplying/dividing the input clock frequency.

.. note::

   The DLL/DCO is inactive by default, passing the optional dedicated clock input directly through to the user project wrapper. If the DLL/DCO is to be used, it must be explicitly enabled via HKSPI or firmware running on the **Management SoC**. For more information, see the section on **Clocking, DLL and DCO**.

See: :doc:`clocking`

POR (Power-On Reset) module
^^^^^^^^^^^^^^^^^^^^^^^^^^^

See: :ref:`powerup`


Four power domains
^^^^^^^^^^^^^^^^^^

Caravel provides **4 power domains**: two intended as nominal 1.8V digital supplies, two intended as analog supplies in the range 1.8V to 5.5V. It also includes |vddio| for setting the desired external digital logic level (as a reference voltage in the range 1.8V-5.5V) for compatibility with a wide range of device.



Caravel Management SoC Features
-------------------------------

The Management SoC's RISC-V CPU (|rv32i|) is built into the die area, adjacent the user project wrapper, and can be interfaced with your design, as well as externally to the chip.

The SoC is generated using :term:`Litex` and includes the following peripherals and capabilities that can be optionally enabled/disabled on subsets of the GPIO pins, to make the SoC useful both as a general-purpose microcontroller and a specialized test/debug interface for your design...


VexRiscv RISC-V CPU core
^^^^^^^^^^^^^^^^^^^^^^^^

The CPU core is a :term:`VexRiscv` minimal+debug configuration. Intended for use either as a microcontroller, general-purpose CPU, control or debug interface to the user design. It can be considered as a lightweight single-core bare-metal microcontroller, programmable in C or RISC-V assembly (|rv32i|, 32-bit instructions specifically), and it comprises:

*  **Dedicated firmware ROM SPI master** for :term:`XIP` loading of firmware code from an external SPI memory into a local 16-word (64-byte) instruction cache.
*  **1.5kByte** local SRAM for stack, scratch space/variables, or small high-speed in-memory executable subroutines.
*  **Interrupt and** :tbc:`exception handling`.
*  **Dedicated power domain**.
*  **GPIO control**: Ability to reconfigure the 38 GPIOs (**27 for Caravan**), including taking over GPIOs as "management mode", either to activate SoC peripherals that have external interfaces, or for firmware to directly use some GPIOs.
*  **Single management GPIO pin**. See: :ref:`mgmt_gpio`

See: :doc:`firmware`

The CPU core also has **access to a range of other SoC peripherals** as described below.

.. note::

   If you don't intend to make use of the Management SoC at all, you can simply choose to not connect to its ports in the users project wrapper, and you can optionally tie its ``RESETb`` signal low externally to hold it in reset.



Logic Analyzer interface
^^^^^^^^^^^^^^^^^^^^^^^^

The **Logic Analyzer** comprises 128 internal IO pins that can optionally be connected with your design in the user project wrapper. :todo:`Explain separate input, output, and OEB signals.`

See: :doc:`logic-analyzer`

Wishbone master
^^^^^^^^^^^^^^^

The user project wrapper has an incoming **Wishbone master** interface from the CPU. This includes the |clk1| signal. It is implemented as a 32-bit Classic-Wishbone-based memory map expansion of the CPU :tbc:`for addresses in the range` ``0x30000000`` -- ``0x300FFFFF``.

See: :doc:`wishbone`

UART
^^^^

The SoC includes a UART that is accessible only to the CPU. It can be enabled to take over two specific GPIO pins for transmit and/or receive, and it has the following features:

*  Fixed baud rate proportional to 9,600 baud at a 10MHz core clock (i.e. 19,200 baud if the Caravel core clock is set to 20MHz).
*  Fixed 8N1 configuration.
*  16-byte FIFO for each of transmit and receive.
*  TX/RX runs independently of the CPU.
*  :tbc:`CPU can poll the FIFO state or enable an IRQ for the UART.`

See: :doc:`uart`


SPI Controller
^^^^^^^^^^^^^^

**SPI master** for direct control by user firmware.

See: :doc:`spi-controller`


6 user IRQs
^^^^^^^^^^^

*  3 internally-driven by the user project.
*  2 externally-driven (optional) by GPIO pins.
*  :tbc:`1 internally-driven by SoC peripherals.`

See: :doc:`irq`


Counter-timer
^^^^^^^^^^^^^

See: :doc:`counter-timer`
