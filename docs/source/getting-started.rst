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

Getting Started with Caravel
============================

Essentials
----------

Should this come before or after 'Minimal example'?

Can describe the essentials of Caravel itself? Is this already covered sufficiently in "Features of Caravel"?

Can include high-level steps, e.g. create your digital logic, connect it to physical harness, harden it to a silicon layout, ensure timing is met for realiable operation and expected clock speed(s), create firmware (if applicable), simulate (RTL & GL), submit for precheck, submit for final tapeout integration, submit for fabrication.

Different approach is to list the things a user would want to accomplish, e.g. you have a need for inputs and outputs that comply with what Caravel's physical harness offers, and optionally want to leverage SoC features, allow CPU to control/supervise aspects of your design, or just be used for bring-up and debug/diagnostics.


Minimal example
---------------

Note that all of this (except user_defines) is already implemented for a real example in CUP. Suggest the user try the example (in full) first. Almost out of scope: Should be covered better by CUP doco.

Implementation: Design/functionality:

*  Explain Verilog is the most common and readily-accessible way to think about this and get started.
*  Describe a digital macro with inputs and outputs and optionally a clock source. Note that other hardening methods exist besides 1 macro.
*  Connect it to UPW pins. Avoid lower 5 for simple designs. Point out that other pins may coexist with other SoC features, but all are optional. Note power connections inside the 'guard' also.
*  Specify user_defines for connected pins.

Hardening:

*  Describe the macro's physical attributes in config.json.
*  Harden the macro -- ensure timing is met (advanced users can adjust as required -- OpenLane is out of scope, but what about SDC port naming??)
*  Minimal instantiation of the macro in UPW config.json.
*  Harden UPW -- check timing again.
*  Check for any other warnings.

Firmware, simulation/verification: ...

Submission: ...


Block diagram
-------------

.. _user_project_wrapper:

user_project_wrapper
--------------------

.. todo::
   Is there a difference worth describing between user_project_wrapper and "user project area"? Technically they are different, but maybe it's always best to refer to "UPW" in all documentation and avoid "user project area".

caravel_user_project template
-----------------------------

.. _powerup:

Power-up/boot process
---------------------

.. todo::

   Create a diagram or sequence that describes both the steps and timing from Caravel chip power-up, both with and without Caravel CPU involvement, and including :term:`crt0` behaviour.
