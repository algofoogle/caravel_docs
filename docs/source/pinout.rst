.. raw:: html

   <!---
   # SPDX-FileCopyrightText: 2025 Efabless Corporation
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


.. figure:: _static/i/caravel-qfn-pinout.svg
      :name: caravel-qfn-pinout
      :alt: Caravel QFN64 pinout
      :align: center

      Caravel QFN64 pinout

.. todo::
   Work out how to make pins/labels in the above image clickable. SVG "A" tags, maybe?

All chips fabricated using the Caravel harness have a standard pinout with some pins dedicated to the SoC (i.e. the CPU), some for power, most for user-configurable GPIOs, and a few with shared functions.

Caravel chips can be ordered in a 64-pin :term:`QFN` package, or as bare dice (unpackaged, bare silicon chips).

Older generations of chipIgnite and the Open MPW shuttles also supplied :term:`WLCSP` packaged parts. These are no longer available with the standard chipIgnite prototyping service.

.. todo::
   Work out the best way to present the pin placement/numbering for different packages, but also clarify the different pin functions (inc. shared pins). Maybe we need a pin-number-to-name list and a pin-name-to-function list that it can link to. Otherwise, just abandon all but QFN64 numbering? Also, should the list be sorted by function or by pin number, or by functional group? Maybe this can be dynamic on the web, but we need to decide for the PDF version too.

.. rst-class:: break_before, ssp-landscape, break_after

Caravel pins and functions
--------------------------

.. csv-table:: Caravel QFN-64 pin descriptions
   :header: QFN64 #,User function,User type,User description,Mgmt function,Mgmt type,Mgmt description

   1,,,,".. _vssa2:

   ``vssa2``",Ground,|upw| analog ground 2
   2,".. _mprj_io25:

   ``mprj_io[25]``",Digital I/O or Analog,:io:`25` [#f1]_ or :aio:`18` [#f4]_,,,
   3,".. _mprj_io26:

   ``mprj_io[26]``",Digital I/O or Analog,:io:`26` [#f1]_ or :aio:`19` [#f4]_,,,
   4,".. _mprj_io27:

   ``mprj_io[27]``",Digital I/O or Analog,:io:`27` [#f1]_ or :aio:`20` [#f4]_,,,
   5,".. _mprj_io28:

   ``mprj_io[28]``",Digital I/O or Analog,:io:`28` [#f1]_ or :aio:`21` [#f4]_,,,
   6,".. _mprj_io29:

   ``mprj_io[29]``",Digital I/O or Analog,:io:`29` [#f1]_ or :aio:`22` [#f4]_,,,
   7,".. _mprj_io30:

   ``mprj_io[30]``",Digital I/O or Analog,:io:`30` [#f1]_ or :aio:`23` [#f4]_,,,[#f5]_
   8,".. _mprj_io31:

   ``mprj_io[31]``",Digital I/O or Analog,:io:`31` [#f1]_ or :aio:`24` [#f4]_,,,[#f5]_
   9,,,,".. _vdda2:

   ``vdda2``",3.3V Power,|upw| analog power supply 2
   10,,,,".. _vssd2:

   ``vssd2``",Ground,|upw| digital ground 2
   11,".. _mprj_io32:

   ``mprj_io[32]``",Digital I/O or Analog,:io:`32` [#f2]_ or :aio:`25` [#f4]_,".. _spi_sck:

   ``spi_sck``",Digital out,|spi_master| clock
   12,".. _mprj_io33:

   ``mprj_io[33]``",Digital I/O or Analog,:io:`33` [#f2]_ or :aio:`26` [#f4]_,".. _spi_csb:

   ``spi_csb``",Digital out,|spi_master| chip select (|alow|)
   13,".. _mprj_io34:

   ``mprj_io[34]``",Digital I/O or Analog,:io:`34` [#f2]_ or :aio:`27` [#f4]_,".. _spi_sdi:

   ``spi_sdi``",Digital in,|spi_master| data input
   14,".. _mprj_io35:

   ``mprj_io[35]``",Digital I/O or Analog,:io:`35` [#f2]_ or :aio:`28` [#f4]_,".. _spi_sdo:

   ``spi_sdo``",Digital out,|spi_master| data output
   15,".. _mprj_io36:

   ``mprj_io[36]``",Digital I/O,:io:`36` [#f2]_,".. _flash_io2:

   ``flash_io2``",Digital I/O,[#f6]_
   16,".. _mprj_io37:

   ``mprj_io[37]``",Digital I/O,:io:`37` [#f2]_,".. _flash_io3:

   ``flash_io3``",Digital I/O,[#f6]_
   17,,,,".. _vddio:

   ``vddio``",3.3V Power,|esd| and padframe power supply [#f7]_
   18,,,,".. _vccd:

   ``vccd``",1.8V Power,|soc| digital power supply
   19,N/C,--,No connection,N/C,--,No connection
   20,,,,".. _vssa:

   ``vssa``",Ground,|soc| analog ground
   21,,,,".. _resetb:

   ``resetb``",Digital in,|soc| system reset (|alow|)
   22,,,,".. _clock:

   ``clock``",Digital in,:doc:`External CMOS 3.3V clock source <clocking>`
   23,,,,".. _vssd:

   ``vssd``",Ground,|soc| digital ground
   24,,,,".. _flash_csb:

   ``flash_csb``",Digital out,|flash_spi| chip select (|alow|)
   25,,,,".. _flash_clk:

   ``flash_clk``",Digital out,|flash_spi| clock
   26,,,,".. _flash_io0:

   ``flash_io[0]``",Digital out,|flash_spi| serial data out
   27,,,,".. _flash_io1:

   ``flash_io[1]``",Digital in,|flash_spi| serial data in
   28,,,,".. _gpio:

   ``gpio``",Digital I/O,|mgmt_gpio|/:tbc:`user power enable`
   29,,,,".. _vssio:

   ``vssio``",Ground,|esd| and padframe ground [#f7]_
   30,,,,".. _vdda:

   ``vdda``",3.3V Power,|soc| analog power supply
   31,".. _mprj_io0:

   ``mprj_io[0]``",Digital I/O,:io:`0` [#f3]_,".. _debug:

   ``debug``",Digital I/O,:doc:`CPU debug port <debug>`
   32,".. _mprj_io1:

   ``mprj_io[1]``",Digital I/O,:io:`1` [#f3]_,".. _SDO:

   ``SDO``",Digital out,|hkspi| data output
   33,".. _mprj_io2:

   ``mprj_io[2]``",Digital I/O,:io:`2` [#f3]_,".. _SDI:

   ``SDI``",Digital in,|hkspi| data input
   34,".. _mprj_io3:

   ``mprj_io[3]``",Digital I/O,:io:`3` [#f3]_,".. _CSB:

   ``CSB``",Digital in,|hkspi| chip select (|alow|)
   35,".. _mprj_io4:

   ``mprj_io[4]``",Digital I/O,:io:`4` [#f3]_,".. _SCK:

   ``SCK``",Digital in,|hkspi| clock
   36,".. _mprj_io5:

   ``mprj_io[5]``",Digital I/O,:io:`5` [#f3]_,".. _ser_rx:

   ``ser_rx``",Digital in,|uart| receive channel
   37,".. _mprj_io6:

   ``mprj_io[6]``",Digital I/O,:io:`6` [#f3]_,".. _ser_tx:

   ``ser_tx``",Digital out,|uart| transmit channel
   38,,,,".. _vssa1:

   ``vssa1``",Ground,|upw| analog ground 1
   39,,,,".. _vssd1:

   ``vssd1``",Ground,|upw| digital ground 1
   40,,,,".. _vdda1:

   ``vdda1``",3.3V Power,|upw| analog power supply 1
   41,".. _mprj_io7:

   ``mprj_io[7]``",Digital I/O or Analog,:io:`7` [#f2]_ or :aio:`0` [#f4]_,".. _irq:

   ``irq``",Digital in,:doc:`External interrupt request <irq>`
   42,".. _mprj_io8:

   ``mprj_io[8]``",Digital I/O or Analog,:io:`8` [#f2]_ or :aio:`1` [#f4]_,".. _flash2_csb:

   ``flash2_csb``",Digital out,|hkspi-user-pass| enable (|alow|)
   43,".. _mprj_io9:

   ``mprj_io[9]``",Digital I/O or Analog,:io:`9` [#f2]_ or :aio:`2` [#f4]_,".. _flash2_sck:

   ``flash2_sck``",Digital out,|hkspi-user-pass| clock
   44,".. _mprj_io10:

   ``mprj_io[10]``",Digital I/O or Analog,:io:`10` [#f2]_ or :aio:`3` [#f4]_,".. _flash2_io0:

   ``flash2_io[0]``",DO :tbc:`??`,|hkspi-user-pass| data :tbc:`out`
   45,".. _mprj_io11:

   ``mprj_io[11]``",Digital I/O or Analog,:io:`11` [#f2]_ or :aio:`4` [#f4]_,".. _flash2_io1:

   ``flash2_io[1]``",DI :tbc:`??`,|hkspi-user-pass| data :tbc:`in`
   46,".. _mprj_io12:

   ``mprj_io[12]``",Digital I/O or Analog,:io:`12` [#f2]_ or :aio:`5` [#f4]_,".. _irq2:

   ``irq2``",DI :tbc:`??`,:tbc:`External interrupt request` :doc:`IRQ <irq>`
   47,,,,"``vdda1``",3.3V Power,|upw| analog power supply 1
   48,".. _mprj_io13:

   ``mprj_io[13]``",Digital I/O or Analog,:io:`13` [#f2]_ or :aio:`6` [#f4]_,".. _trap:

   ``trap``",:tbc:`Digital ??`,[#f8]_
   49,,,,".. _vccd1:

   ``vccd1``",1.8V Power,|upw| digital power supply 1
   50,".. _mprj_io14:

   ``mprj_io[14]``",Digital I/O or Analog,:io:`14` [#f2]_ or :aio:`7` [#f4]_,".. _mprj_clock:

   ``mprj_clock``",Digital out,Clock monitoring output for wb_clk_i
   51,".. _mprj_io15:

   ``mprj_io[15]``",Digital I/O or Analog,:io:`15` [#f2]_ or :aio:`8` [#f4]_,".. _mprj_clock2:

   ``mprj_clock2``",Digital out,Clock monitoring output for user_clock2
   52,,,,"``vssa1``",Ground,|upw| analog ground 1
   53,".. _mprj_io16:

   ``mprj_io[16]``",Digital I/O or Analog,:io:`16` [#f1]_ or :aio:`9` [#f4]_,,,
   54,".. _mprj_io17:

   ``mprj_io[17]``",Digital I/O or Analog,:io:`17` [#f1]_ or :aio:`10` [#f4]_,,,
   55,".. _mprj_io18:

   ``mprj_io[18]``",Digital I/O or Analog,:io:`18` [#f1]_ or :aio:`11` [#f4]_,,,
   56,,,,"``vssio``",Ground,|esd| and padframe ground [#f7]_
   57,".. _mprj_io19:

   ``mprj_io[19]``",Digital I/O or Analog,:io:`19` [#f1]_ or :aio:`12` [#f4]_,,,
   58,".. _mprj_io20:

   ``mprj_io[20]``",Digital I/O or Analog,:io:`20` [#f1]_ or :aio:`13` [#f4]_,,,
   59,".. _mprj_io21:

   ``mprj_io[21]``",Digital I/O or Analog,:io:`21` [#f1]_ or :aio:`14` [#f4]_,,,
   60,".. _mprj_io22:

   ``mprj_io[22]``",Digital I/O or Analog,:io:`22` [#f1]_ or :aio:`15` [#f4]_,,,
   61,".. _mprj_io23:

   ``mprj_io[23]``",Digital I/O or Analog,:io:`23` [#f1]_ or :aio:`16` [#f4]_,,,
   62,".. _mprj_io24:

   ``mprj_io[24]``",Digital I/O or Analog,:io:`24` [#f1]_ or :aio:`17` [#f4]_,,,
   63,,,,".. _vccd2:

   ``vccd2``",1.8V Power,|upw| digital power supply 2
   64,,,,"``vddio``",3.3V Power,|esd| and padframe power supply [#f7]_

.. [#f1] **GPIOs** are General purpose configurable digital I/O with pullup/pulldown, input/output/bidirectional, enable/disable, and slew rate control. GPIO pins are shared between the user project area and the management SoC: any configured in |user_mode| are directly connected/controlled via logic in the :ref:`user_project_wrapper`; any configured in |mgmt_mode| are directly under control of the Management SoC, *plus* their respective "Mgmt function" (if any) can optionally also be enabled. The power-on :ref:`mode configuration <gpio_modes>` of most GPIO pins is mask-programmed, defined by |user_defines| during tapeout. **NOTE**: Some GPIOs can be configured for direct "analog" connections [#f4]_

.. [#f2] GPIO function same as above [#f1]_, also optionally supporting activation of an alternate management function (i.e. a specific peripheral device in the management SoC that can optionally be activated when the pin is in |mgmt_mode|).

.. [#f3] GPIO function same as above [#f2]_, but always powers up initially in |mgmt_mode|, *and* with its respective management function activated by default (to ensure :doc:`Housekeeping <housekeeping>` can always be made available). Unlike [#f1]_ and [#f2]_, these pins cannot be overridden by |user_defines| but can still be temporarily overridden by :ref:`firmware or HKSPI <gpio_reconfiguration>`.

.. [#f4] "mrpj_io" pins, where specified, can also be configured for "analog_io" mode. In this case, digital buffers are disabled, thus enabling custom analog circuits in the |upw| to make direct connections to the respective bare pad. See: :doc:`analog`; and note the internal "``analog_io[#]``" numbering differences.

.. [#f5] **Caravan** can only provide its two clock monitoring pins via mprj_io 30 and 31 (instead of 14 and 15) as Caravan repurposes ``mprj_io[24:14]`` as bare analog pads only, with no built-in digital configuration options. This alternate function mapping to 30/31 only exists on Caravan, not on Caravel.

.. [#f6] :tbc:`For more information on QSPI and the two additional flash IO pins,` see: https://github.com/efabless/caravel/blob/27cbe49c90ba5362ad52c9968dd98e035c30c74f/verilog/rtl/housekeeping.v#L776-L793

.. [#f7] ``vddio`` sets the digital I/O 'high' voltage level, automatically handling level shifting. ``vddio`` (supply) and ``vssio`` (ground) are also connected to pad clamping diodes for |esd| protection. ``vddio`` is nominally 3.3V; see also: :doc:`specs`.

.. [#f8] :tbc:`Caravel Registers TRM says this is not available;` See: ``reg_clk_out_dest``


.. This is the old table format. Harder to maintain but possibly a better COMPILED format for including extra markers:
   .. list-table:: Pin description
      :name: pin-description
      :header-rows: 1

      *  -  Name
         -  Type
         -  Description
      *  -  .. _mprj_io:

            ``mprj_io[37:0]``
         -  Digital I/O
         -  General purpose configurable digital I/O with pullup/pulldown, input or output, enable/disable, analog output, high voltage output, slew rate control.
            Shared between the user project area and the management SoC.
      *  -  .. _flash_clk:
      
            ``flash_clk``
         -  Digital out
         -  Flash SPI clock
      *  -  .. _flash_csb:
      
            ``flash_csb``
         -  Digital out
         -  Flash SPI chip select
      *  -  .. _flash_io:
      
            ``flash_io[1:0]``
         -  Digital I/O
         -  Flash SPI data input/output
      *  -  .. _clock:
      
            ``clock``
         -  Digital in
         -  External CMOS 3.3V clock source
      *  -  .. _resetb:
      
            ``resetb``
         -  Digital in
         -  SoC system reset (sense inverted)
      *  -  .. _sdo:
      
            ``SDO``
         -  Digital out
         -  Housekeeping serial interface data output
      *  -  .. _sdi:
      
            ``SDI``
         -  Digital in
         -  Housekeeping serial interface data input
      *  -  .. _csb:
      
            ``CSB``
         -  Digital in
         -  Housekeeping serial interface chip select
      *  -  .. _sck:
      
            ``SCK``
         -  Digital in
         -  Housekeeping serial interface clock
      *  -  .. _ser_tx:
      
            ``ser_tx``
         -  Digital out
         -  UART transmit channel
      *  -  .. _ser_rx:
      
            ``ser_rx``
         -  Digital in
         -  UART receive channel
      *  -  .. _irq:
      
            ``irq``
         -  Digital in
         -  External interrupt
      *  -  .. _gpio:
      
            ``gpio``
         -  Digital I/O
         -  Management GPIO/user power enable
      *  -  .. _debug:
      
            ``debug``
         -  Digital I/O
         -  CPU debug port
      *  -  .. _flash2_csb:
      
            ``flash2_csb``
         -  Digital out
         -  User area QSPI flash enable (sense inverted)
      *  -  .. _flash2_sck:
      
            ``flash2_sck``
         -  Digital out
         -  User area QSPI flash clock
      *  -  .. _flash2_io:
      
            ``flash2_io[1:0]``
         -  Digital I/O
         -  User area QSPI flash data
      *  -  .. _spi_sdo:
      
            ``spi_sdo``
         -  Digital out
         -  Serial interface controller data output
      *  -  .. _spi_sck:
      
            ``spi_sck``
         -  Digital out
         -  Serial interface controller clock
      *  -  .. _spi_csb:
      
            ``spi_csb``
         -  Digital out
         -  Serial interface controller chip select
      *  -  .. _spi_sdi:
      
            ``spi_sdi``
         -  Digital in
         -  Serial interface controller data input
      *  -  .. _vddio:
      
            ``vddio``
         -  3.3V Power
         -  ESD and padframe power supply
      *  -  .. _vdda:
      
            ``vdda``
         -  3.3V Power
         -  Management area power supply
      *  -  .. _vccd:
      
            ``vccd``
         -  1.8V Power
         -  Management area digital power supply
      *  -  .. _vssio_vssa_vssd:
      
            ``vssio``/``vssa``/``vssd``
         -  Ground
         -  ESD, padframe, and management area ground
      *  -  .. _vdda1:
      
            ``vdda1``
         -  3.3V Power
         -  User area 1 power supply
      *  -  .. _vccd1:
      
            ``vccd1``
         -  1.8V Power
         -  User area 1 digital power supply
      *  -  .. _vssa1:
      
            ``vssa1``
         -  Ground
         -  User area 1 ground
      *  -  .. _vssd1:
      
            ``vssd1``
         -  Ground
         -  User area 1 digital ground
      *  -  .. _vdda2:
      
            ``vdda2``
         -  3.3V Power
         -  User area 2 power supply
      *  -  .. _vccd2:

            ``vccd2``
         -  1.8V Power
         -  User area 2 digital power supply
      *  -  .. _vssa2:
      
            ``vssa2``
         -  Ground
         -  User area 2 ground
      *  -  .. _vssd2:
      
            ``vssd2``
         -  Ground
         -  User area 2 digital ground



Caravel bare die pinout
-----------------------

Caravel bare dice have bond pads in a standard padring and are numbered starting at 1 on the top of the left-hand edge, incrementing counter-clockwise up to pad 63.



Caravel WLCSP pinout
--------------------

Wafer-level chip-scale packaging is no longer offered by Efabless for standard chipIgnite orders, but may be specially-ordered and customized for large-volume production orders.

Older generations of Caravel chip already fabricated as WLCSP instead of QFN or bare dice had the following pinout:

.. todo::
   Put in BGA diagram, X/Y labeling, and table. **Otherwise,** make the table above support pin numbering for all variants in separate columns.

