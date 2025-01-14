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

General Purpose Input/Output (GPIO)
===================================

.. todo::
   Talk about the wrapper, and its general use of IO cells (link to gpiov2), housekeeping configuration, |upw_ports|, etc...

In the Caravel context, "General Purpose Input/Output" (or GPIO) most often refers to the 38 |gpio|, but might also refer to the single extra |mgmt_gpio|.

.. todo::
   Explain how it's useful that pins can be reconfigured and taken over, but also that this is relatively slow to do (whether via firmware or HKSPI).

.. seealso::
   :doc:`pinout`
      List of all the Caravel chip external pins (including GPIO pins), named by function.

.. _user_gpio:

User GPIO pins
--------------

Caravel provides 38 external GPIO pins, typically called ``mprj_io[37]`` down to ``mprj_io[0]``, sometimes referred to as ``GPIO[37:0]`` or simply ``IO[37:0]``. These are available for use by the user design and logic, and/or by the Caravel Management SoC (including CPU, but also other dedicated periphrals that can be enabled on certain pins). While all are digital-capable, some can also carry analog signals (for advanced designs that :doc:`implement their own analog <analog>` circuits/devices).

*  All 38 GPIOs have digital control circuitry that allows them to be configured after power-on for different modes via registers accessible via firmware or |hkspi|.
*  .. _reserved_gpios:
   
   The lowest-numbered 5 of the 38 always power up in a fixed Caravel management mode: ``IO[4:1]`` are enabled for exclusive use as the |hkspi| interface; ``IO[0]`` is enabled as a :doc:`debug <debug>` pin. Therefore, these are not immediately usable by the user design area, until they are reconfigured at run-time (if desired), in which case the respective HKSPI/debug functions are disabled (until explicitly re-enabled by firmware, or until the next power-on, only).
*  The remaining 33 of 38 must have their default power-on modes masked-programmed, i.e. a simple ":ref:`user_defines <user_defines>`" configuration file defines how they will be hard-set during fabrication. This ensures they have a known desired mode immediately after power-up, though they can still be reconfigured at run-time.
*  NOTE: The GPIO configuration modes are retained across SoC resets, but not across power cycling.
*  Out of the above 33 pins, 29 (``IO[35:7]``) can also be configured to support :doc:`direct analog connections <analog>`, thus disabling their digital control circuitry for  designers who specifically want to include their own (or ready-made) analog circuits in the user project area.

Each of the 38 GPIOs provides multiple ports into the user project area to enable direct connections to the user's design/logic, and meet all supported use cases:

*  All 38 provide ``io_in[*]`` (input digital signal paths), ``io_out[*]`` (output digital signal paths), and ``io_oeb[*]`` ("Output Enable :term:`Bar`" for setting the signal directions). Note that, at any given moment, whichever of these paths are actually usable or meaningful depends on what mode the pin is configured for. For example, ``io_oeb`` has no effect on changing the pin direction if the pin is already configured as an output.
*  The 29 that are analog-capable also provide ``analog_io[*]`` ports.

.. note::
   ``io_in`` always has an active input buffer that feeds the digital logic state of the pin back into the user project area depending on the voltage present on the pad :tbc:`(does it definitely? Are there cases where this is not true?)`

.. todo::
   Come up with a concise way to represent all the combinations, inc. for pull-up/down, and buffer states in various modes (e.g. analog).

.. todo::
   Explain that io_oeb has certain conventions depending on intended mode and pull-up/down behaviour.

.. todo::
   Note Caravan and Caravel Mini differences also.




.. _mgmt_gpio:

Management GPIO pin
-------------------

.. _gpio_reconfiguration:

User GPIO configuration by firmware or HKSPI
--------------------------------------------

.. _user_defines:

User GPIO power-on configuration by user_defines
------------------------------------------------

.. _gpio_modes:

Standard GPIO configuration mode constants
------------------------------------------

.. todo::
   Do this as a table that presents the constant, its value, its intended use, and how it otherwise alters the requirements and behaviour of the pin, e.g. it should explain that pull-up/down depends on certain other signals to work correctly.

   Should this table also include an expansion of the bitfields (per Mitch's table), and point out that different drive strengths and open-drain are possible (I think)?


.. _user_mode:

USER modes
^^^^^^^^^^

The presence of ``..._USER_...`` in the name of a GPIO mode constant indicates that this mode will activate the pin's respective |upw_ports|, meaning the user project can be directly connected to the GPIO's digital paths. In other words, the user project has exclusive access to the pin when one of these modes are used.

.. list-table:: Standard GPIO "USER" mode constants
   :header-rows: 1

   *  -  Named constant
      -  Value
      -  Description

   *  -  .. _GPIO_MODE_USER_STD_INPUT_NOPULL:

         ``GPIO_MODE_USER_STD_INPUT_NOPULL``
      -  0x0402
      -  |TBC|
   *  -  .. _GPIO_MODE_USER_STD_INPUT_PULLDOWN:

         ``GPIO_MODE_USER_STD_INPUT_PULLDOWN``
      -  0x0c00
      -  |TBC|
   *  -  .. _GPIO_MODE_USER_STD_INPUT_PULLUP:

         ``GPIO_MODE_USER_STD_INPUT_PULLUP``
      -  0x0800
      -  |TBC|
   *  -  .. _GPIO_MODE_USER_STD_OUTPUT:

         ``GPIO_MODE_USER_STD_OUTPUT``
      -  0x1808
      -  |TBC|
   *  -  .. _GPIO_MODE_USER_STD_BIDIRECTIONAL:

         ``GPIO_MODE_USER_STD_BIDIRECTIONAL``
      -  0x1800
      -  |TBC|
   *  -  .. _GPIO_MODE_USER_STD_OUT_MONITORED:

         ``GPIO_MODE_USER_STD_OUT_MONITORED``
      -  0x1802
      -  |TBC|
   *  -  .. _GPIO_MODE_USER_STD_ANALOG:

         ``GPIO_MODE_USER_STD_ANALOG``
      -  0x000a
      -  |TBC|


.. _mgmt_mode:

MGMT modes
^^^^^^^^^^

The presence of ``..._MGMT_...`` in the name of a GPIO mode constant indicates that this mode will give the |soc| exclusive access to the pin, thus deactivating the pin's respective |upw_ports|. In other words, the |soc| will be able to read/write/control the pin, while the user project will not.

There are two exceptions, however:

*  :tbc:`There is a |upw| input buffer always attached to the pin pad, so long as the GPIO is not configured for one of the ANALOG modes. This means the user project is always able to sense the digital state of the pin, including if it is being used in any USER or MGMT input/output mode. This also means that the |soc| could directly drive GPIOs in a way that loop back into the user project.`
*  Connections to the :doc:`analog paths <analog>` of |upw_ports| are always physically direct and cannot be disconnected. If your user project makes such connections, be careful about configuring the GPIO for any non-``ANALOG`` mode (whence the GPIO's digital circuitry will be active simultaneously).

.. list-table:: Standard GPIO "MGMT" mode constants
   :header-rows: 1

   *  -  Named constant
      -  Value
      -  Description
   *  -  .. _GPIO_MODE_MGMT_STD_INPUT_NOPULL:
      
         ``GPIO_MODE_MGMT_STD_INPUT_NOPULL``
      -  0x0403
      -  |TBC|
   *  -  .. _GPIO_MODE_MGMT_STD_INPUT_PULLDOWN:
      
         ``GPIO_MODE_MGMT_STD_INPUT_PULLDOWN``
      -  0x0c01
      -  |TBC|
   *  -  .. _GPIO_MODE_MGMT_STD_INPUT_PULLUP:
      
         ``GPIO_MODE_MGMT_STD_INPUT_PULLUP``
      -  0x0801
      -  |TBC|
   *  -  .. _GPIO_MODE_MGMT_STD_OUTPUT:
      
         ``GPIO_MODE_MGMT_STD_OUTPUT``
      -  0x1809
      -  |TBC|
   *  -  .. _GPIO_MODE_MGMT_STD_BIDIRECTIONAL:
      
         ``GPIO_MODE_MGMT_STD_BIDIRECTIONAL``
      -  0x1801
      -  |TBC|
   *  -  .. _GPIO_MODE_MGMT_STD_ANALOG:
      
         ``GPIO_MODE_MGMT_STD_ANALOG``
      -  0x000b
      -  |TBC|


Custom modes
------------

You can set your own configuration bitfield. :tbc:`DEFINE HOW.`


io_oeb conventions
------------------

.. todo::
   Discuss precheck somewhere


GPIO pin ports map
------------------

.. todo::
   Do it as a table resembling `the one showing Caravan pins <https://github.com/efabless/caravel_user_project_analog/blob/7f1055518a0ae50541981cb8a5cded9b2cdf9e65/verilog/rtl/user_analog_proj_example.v#L24-L61>`_
