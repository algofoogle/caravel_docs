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

Caravel Pinouts
===============


Caravel QFN-64 pinout
---------------------

.. figure:: _static/i/caravel-qfn-pinout.svg
      :name: caravel-qfn-pinout
      :alt: Caravel QFN64 pinout
      :align: center

      Caravel QFN64 pinout

.. todo::
   Work out how to make pins/labels in the above image clickable. SVG "A" tags, maybe?

All chips fabricated using the Caravel harness have a standard pinout with some pins dedicated to the SoC (i.e. the CPU), some for power, most for user-configurable GPIOs, and a few with shared functions.

Caravel chips can be ordered in a 64-pin :term:`QFN` package, or as bare dice (unpackaged, bare silicon chips).

Older generations of chipIgnite and the Open MPW shuttles also supplied :term:`WLCSP` packaged parts.

.. todo::
  Work out the best way to present the pin placement/numbering for different packages, but also clarify the different pin functions (inc. shared pins). Maybe we need a pin-number-to-name list and a pin-name-to-function list that it can link to. Otherwise, just abandon all but QFN64 numbering? Also, should the list be sorted by function or by pin number, or by functional group? Maybe this can be dynamic on the web, but we need to decide for the PDF version too.

.. rst-class:: break_before, ssp-landscape, break_after

Caravel pins and functions
--------------------------

.. csv-table:: Newer pin description
   :header: QFN64 #,User function,User type,User description,Mgmt function,Mgmt type,Mgmt description

   1,,,,``vssa2``,Ground,|upw| analog ground 2
   2,``mprj_io[25]``,Digital I/O or Analog,:port:`GPIO[25]` [#f1]_ or :port:`analog_io[18]` [#f4]_,,,
   3,``mprj_io[26]``,Digital I/O or Analog,GPIO[26] [#f1]_ or analog_io[19] [#f4]_,,,
   4,``mprj_io[27]``,Digital I/O or Analog,GPIO[27] [#f1]_ or analog_io[20] [#f4]_,,,
   5,``mprj_io[28]``,Digital I/O or Analog,GPIO[28] [#f1]_ or analog_io[21] [#f4]_,,,
   6,``mprj_io[29]``,Digital I/O or Analog,GPIO[29] [#f1]_ or analog_io[22] [#f4]_,,,
   7,``mprj_io[30]``,Digital I/O or Analog,GPIO[30] [#f1]_ or analog_io[23] [#f4]_,,,[#f5]_
   8,``mprj_io[31]``,Digital I/O or Analog,GPIO[31] [#f1]_ or analog_io[24] [#f4]_,,,[#f5]_
   9,,,,``vdda2``,3.3V Power,|upw| analog power supply 2
   10,,,,``vssd2``,Ground,|upw| digital ground 2
   11,``mprj_io[32]``,Digital I/O or Analog,GPIO[32] [#f2]_ or analog_io[25] [#f4]_,``spi_sck``,Digital out,|spi_master| clock
   12,``mprj_io[33]``,Digital I/O or Analog,GPIO[33] [#f2]_ or analog_io[26] [#f4]_,``spi_csb``,Digital out,|spi_master| chip select (|alow|)
   13,``mprj_io[34]``,Digital I/O or Analog,GPIO[34] [#f2]_ or analog_io[27] [#f4]_,``spi_sdi``,Digital in,|spi_master| data input
   14,``mprj_io[35]``,Digital I/O or Analog,GPIO[35] [#f2]_ or analog_io[28] [#f4]_,``spi_sdo``,Digital out,|spi_master| data output
   15,``mprj_io[36]``,Digital I/O,GPIO[36] [#f2]_,``flash_io2``,Digital I/O,[#f6]_
   16,``mprj_io[37]``,Digital I/O,GPIO[37] [#f2]_,``flash_io3``,Digital I/O,[#f6]_
   17,,,,``vddio``,3.3V Power,ESD and padframe power supply [#f7]_
   18,,,,``vccd``,1.8V Power,|soc| digital power supply
   19,N/C,--,No connection,N/C,--,No connection
   20,,,,``vssa``,Ground,|soc| analog ground
   21,,,,``resetb``,Digital in,|soc| system reset (|alow|)
   22,,,,``clock``,Digital in,:doc:`External CMOS 3.3V clock source <clocking>`
   23,,,,``vssd``,Ground,|soc| digital ground
   24,,,,``flash_csb``,Digital out,|flash_spi| chip select (|alow|)
   25,,,,``flash_clk``,Digital out,|flash_spi| clock
   26,,,,``flash_io[0]``,Digital out,|flash_spi| serial data out
   27,,,,``flash_io[1]``,Digital in,|flash_spi| serial data in
   28,,,,``gpio``,Digital I/O,|mgmt_gpio|/:tbc:`user power enable`
   29,,,,``vssio``,Ground,ESD and padframe ground [#f7]_
   30,,,,``vdda``,3.3V Power,|soc| analog power supply
   31,``mprj_io[0]``,Digital I/O,GPIO[0] [#f3]_,``debug``,Digital I/O,:doc:`CPU debug port <debug>`
   32,``mprj_io[1]``,Digital I/O,GPIO[1] [#f3]_,``SDO``,Digital out,|hkspi| data output
   33,``mprj_io[2]``,Digital I/O,GPIO[2] [#f3]_,``SDI``,Digital in,|hkspi| data input
   34,``mprj_io[3]``,Digital I/O,GPIO[3] [#f3]_,``CSB``,Digital in,|hkspi| chip select (|alow|)
   35,``mprj_io[4]``,Digital I/O,GPIO[4] [#f3]_,``SCK``,Digital in,|hkspi| clock
   36,``mprj_io[5]``,Digital I/O,GPIO[5] [#f3]_,``ser_rx``,Digital in,|uart| receive channel
   37,``mprj_io[6]``,Digital I/O,GPIO[6] [#f3]_,``ser_tx``,Digital out,|uart| transmit channel
   38,,,,``vssa1``,Ground,|upw| analog ground 1
   39,,,,``vssd1``,Ground,|upw| digital ground 1
   40,,,,``vdda1``,3.3V Power,|upw| analog power supply 1
   41,``mprj_io[7]``,Digital I/O or Analog,GPIO[7] [#f2]_ or analog_io[0] [#f4]_,``irq``,Digital in,:doc:`External interrupt request <irq>`
   42,``mprj_io[8]``,Digital I/O or Analog,GPIO[8] [#f2]_ or analog_io[1] [#f4]_,``flash2_csb``,Digital out,|hkspi-user-pass| enable (|alow|)
   43,``mprj_io[9]``,Digital I/O or Analog,GPIO[9] [#f2]_ or analog_io[2] [#f4]_,``flash2_sck``,Digital out,|hkspi-user-pass| clock
   44,``mprj_io[10]``,Digital I/O or Analog,GPIO[10] [#f2]_ or analog_io[3] [#f4]_,``flash2_io[0]``,DO :tbc:`??`,|hkspi-user-pass| data :tbc:`out`
   45,``mprj_io[11]``,Digital I/O or Analog,GPIO[11] [#f2]_ or analog_io[4] [#f4]_,``flash2_io[1]``,DI :tbc:`??`,|hkspi-user-pass| data :tbc:`in`
   46,``mprj_io[12]``,Digital I/O or Analog,GPIO[12] [#f2]_ or analog_io[5] [#f4]_,``irq2``,DI :tbc:`??`,:tbc:`External interrupt request` :doc:`IRQ <irq>`
   47,,,,``vdda1``,3.3V Power,|upw| analog power supply 1
   48,``mprj_io[13]``,Digital I/O or Analog,GPIO[13] [#f2]_ or analog_io[6] [#f4]_,``trap``,:tbc:`Digital ??`,[#f8]_
   49,,,,``vccd1``,1.8V Power,|upw| digital power supply 1
   50,``mprj_io[14]``,Digital I/O or Analog,GPIO[14] [#f2]_ or analog_io[7] [#f4]_,``mprj_clock``,Digital out,Clock monitoring output for wb_clk_i
   51,``mprj_io[15]``,Digital I/O or Analog,GPIO[15] [#f2]_ or analog_io[8] [#f4]_,``mprj_clock2``,Digital out,Clock monitoring output for user_clock2
   52,,,,``vssa1``,Ground,|upw| analog ground 1
   53,``mprj_io[16]``,Digital I/O or Analog,GPIO[16] [#f1]_ or analog_io[9] [#f4]_,,,
   54,``mprj_io[17]``,Digital I/O or Analog,GPIO[17] [#f1]_ or analog_io[10] [#f4]_,,,
   55,``mprj_io[18]``,Digital I/O or Analog,GPIO[18] [#f1]_ or analog_io[11] [#f4]_,,,
   56,,,,``vssio``,Ground,ESD and padframe ground [#f7]_
   57,``mprj_io[19]``,Digital I/O or Analog,GPIO[19] [#f1]_ or analog_io[12] [#f4]_,,,
   58,``mprj_io[20]``,Digital I/O or Analog,GPIO[20] [#f1]_ or analog_io[13] [#f4]_,,,
   59,``mprj_io[21]``,Digital I/O or Analog,GPIO[21] [#f1]_ or analog_io[14] [#f4]_,,,
   60,``mprj_io[22]``,Digital I/O or Analog,GPIO[22] [#f1]_ or analog_io[15] [#f4]_,,,
   61,``mprj_io[23]``,Digital I/O or Analog,GPIO[23] [#f1]_ or analog_io[16] [#f4]_,,,
   62,``mprj_io[24]``,Digital I/O or Analog,GPIO[24] [#f1]_ or analog_io[17] [#f4]_,,,
   63,,,,``vccd2``,1.8V Power,|upw| digital power supply 2
   64,,,,``vddio``,3.3V Power,ESD and padframe power supply [#f7]_

.. [#f1] **GPIOs** are General purpose configurable digital I/O with pullup/pulldown, input/output/bidirectional, enable/disable, and slew rate control. GPIO pins are shared between the user project area and the management SoC: any configured in "USER" mode are directly connected/controlled via logic in the :ref:`user_project_wrapper`; any configured in "MGMT" mode are directly under control of the Management SoC, *plus* their respective "Mgmt function" (if any) can optionally also be enabled. The power-on :ref:`mode configuration <gpio_modes>` of most GPIO pins is mask-programmed, defined by |user_defines| during tapeout. **NOTE**: Some GPIOs can be configured for direct "analog" connections [#f4]_

.. [#f2] GPIO function same as above [#f1]_, but with an alternate management function (i.e. a specific peripheral device in the management SoC) that can optionally also be activated in combination with the pin being put into "MGMT" mode.

.. [#f3] GPIO function same as above [#f2]_, but always powers up initially in MGMT mode, *and* with its respective management function activated by default (to ensure :doc:`Housekeeping <housekeeping>` can always be made available). Unlike [#f1]_ and [#f2]_, these pins cannot be overridden by |user_defines| but can still be temporarily overridden by :ref:`firmware or HKSPI <gpio_reconfiguration>`.

.. [#f4] "mrpj_io" pins, where specified, can also be configured for "analog_io" mode. In this case, digital buffers are disabled, thus enabling custom analog circuits in the |upw| to make direct connections to the respective bare pad. See: :doc:`analog`; and note the internal "``analog_io[#]``" numbering differences.

.. [#f5] **Caravan** can only provide its two clock monitoring pins via mprj_io 30 and 31 (instead of 14 and 15) as Caravan repurposes ``mprj_io[24:14]`` as bare analog pads only, with no built-in digital configuration options. This alternate function mapping to 30/31 only exists on Caravan, not on Caravel.

.. [#f6] :tbc:`For more information on QSPI and the two additional flash IO pins,` see: https://github.com/efabless/caravel/blob/27cbe49c90ba5362ad52c9968dd98e035c30c74f/verilog/rtl/housekeeping.v#L776-L793

.. [#f7] ``vddio`` sets the digital I/O 'high' voltage level, automatically handling level shifting. ``vddio`` (supply) and ``vssio`` (ground) are also connected to pad clamping diodes for ESD protection. ``vddio`` is nominally 3.3V; see also: :doc:`specs`.

.. [#f8] :tbc:`Caravel Registers TRM says this is not available;` See: ``reg_clk_out_dest``


.. This is the old table format. Harder to maintain but possibly a better COMPILED format for including extra markers:
   .. list-table:: Pin description
      :name: pin-description
      :header-rows: 1
  
      * - Name
        - Type
        - Description
      * - .. _mprj_io:
  
          ``mprj_io[37:0]``
        - Digital I/O
        - General purpose configurable digital I/O with pullup/pulldown, input or output, enable/disable, analog output, high voltage output, slew rate control.
          Shared between the user project area and the management SoC.
      * - .. _flash_clk:
  
          ``flash_clk``
        - Digital out
        - Flash SPI clock
      * - .. _flash_csb:
  
          ``flash_csb``
        - Digital out
        - Flash SPI chip select
      * - .. _flash_io:
  
          ``flash_io[1:0]``
        - Digital I/O
        - Flash SPI data input/output
      * - .. _clock:
  
          ``clock``
        - Digital in
        - External CMOS 3.3V clock source
      * - .. _resetb:
  
          ``resetb``
        - Digital in
        - SoC system reset (sense inverted)
      * - .. _sdo:
  
          ``SDO``
        - Digital out
        - Housekeeping serial interface data output
      * - .. _sdi:
  
          ``SDI``
        - Digital in
        - Housekeeping serial interface data input
      * - .. _csb:
  
          ``CSB``
        - Digital in
        - Housekeeping serial interface chip select
      * - .. _sck:
  
          ``SCK``
        - Digital in
        - Housekeeping serial interface clock
      * - .. _ser_tx:
  
          ``ser_tx``
        - Digital out
        - UART transmit channel
      * - .. _ser_rx:
  
          ``ser_rx``
        - Digital in
        - UART receive channel
      * - .. _irq:
  
          ``irq``
        - Digital in
        - External interrupt
      * - .. _gpio:
  
          ``gpio``
        - Digital I/O
        - Management GPIO/user power enable
      * - .. _debug:
  
          ``debug``
        - Digital I/O
        - CPU debug port
      * - .. _flash2_csb:
  
          ``flash2_csb``
        - Digital out
        - User area QSPI flash enable (sense inverted)
      * - .. _flash2_sck:
  
          ``flash2_sck``
        - Digital out
        - User area QSPI flash clock
      * - .. _flash2_io:
  
          ``flash2_io[1:0]``
        - Digital I/O
        - User area QSPI flash data
      * - .. _spi_sdo:
  
          ``spi_sdo``
        - Digital out
        - Serial interface controller data output
      * - .. _spi_sck:
  
          ``spi_sck``
        - Digital out
        - Serial interface controller clock
      * - .. _spi_csb:
  
          ``spi_csb``
        - Digital out
        - Serial interface controller chip select
      * - .. _spi_sdi:
  
          ``spi_sdi``
        - Digital in
        - Serial interface controller data input
      * - .. _vddio:
  
          ``vddio``
        - 3.3V Power
        - ESD and padframe power supply
      * - .. _vdda:
  
          ``vdda``
        - 3.3V Power
        - Management area power supply
      * - .. _vccd:
  
          ``vccd``
        - 1.8V Power
        - Management area digital power supply
      * - .. _vssio_vssa_vssd:
  
          ``vssio``/``vssa``/``vssd``
        - Ground
        - ESD, padframe, and management area ground
      * - .. _vdda1:
  
          ``vdda1``
        - 3.3V Power
        - User area 1 power supply
      * - .. _vccd1:
  
          ``vccd1``
        - 1.8V Power
        - User area 1 digital power supply
      * - .. _vssa1:
  
          ``vssa1``
        - Ground
        - User area 1 ground
      * - .. _vssd1:
  
          ``vssd1``
        - Ground
        - User area 1 digital ground
      * - .. _vdda2:
  
          ``vdda2``
        - 3.3V Power
        - User area 2 power supply
      * - .. _vccd2:

          ``vccd2``
        - 1.8V Power
        - User area 2 digital power supply
      * - .. _vssa2:
  
          ``vssa2``
        - Ground
        - User area 2 ground
      * - .. _vssd2:
  
          ``vssd2``
        - Ground
        - User area 2 digital ground



Caravel bare die pinout
-----------------------

Caravel bare dice have bond pads in a standard padring and are numbered starting at 1 on the top of the left-hand edge, incrementing counter-clockwise up to pad 63.



Caravel WLCSP pinout
--------------------

Wafer-level chip-scale packaging is no longer offered by Efabless for standard chipIgnite orders, but may be specially-ordered and customized for large-volume production orders.

Older generations of Caravel chip already fabricated as WLCSP instead of QFN or bare dice had the following pinout:

.. todo::
   Put in BGA diagram, X/Y labeling, and table. **Otherwise,** make the table above support pin numbering for all variants in separate columns.


