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

Debug Port
==========

.. todo::
   Confirm that the debug port is actually available, actually works, and matches the documentation given below.

   This section needs more detail and hopefully an example.

The Caravel CPU supports debugging via the |debug| pin. :tbc:`It can be accessed through a dedicated UART port configured as a Wishbone master.` The baud rate for the port is fixed; nominally i tis 9600 baud given a 10MHz SoC core clock.

See the following reference for more information: `VexRiscv DebugPlugin <https://github.com/SpinalHDL/VexRiscv#debugplugin>`_

