.. This file gets included via conf.py (rst_prolog) to provide convenient, replaceable references to things that are likely to be renamed or redirected at some point in the future.

.. NOTE: For some reason, I can't use links in these substitutions. It generates an error about invalid <target> elements.

.. |caravel_board|      replace:: :term:`Caravel Eval Board`
.. |clkin|              replace:: :ref:`clock <clock>`
.. |debug|              replace:: :ref:`debug <debug>`
.. |clk1|               replace:: :ref:`wb_clk_i`
.. |clk2|               replace:: :ref:`user_clock2`
.. |upw|                replace:: :term:`User Project Wrapper`
.. |upw_ports|          replace:: |upw| edge ports
.. |mgmt_out|           replace:: :ref:`GPIO_MODE_MGMT_STD_OUTPUT <GPIO_MODE_MGMT_STD_OUTPUT>`
.. |vddio|              replace:: :ref:`vddio <vddio>`
.. |hkspi|              replace:: :doc:`HKSPI <housekeeping>`
.. |dll|                replace:: :ref:`DLL <dll>`
.. |dco|                replace:: :ref:`DCO <dco>`
.. |gpio|               replace:: :ref:`User GPIO pins <user_gpio>`
.. |mgmt_gpio|          replace:: :ref:`Management GPIO pin <mgmt_gpio>`
.. |user_defines|       replace:: :ref:`user_defines configuration <user_defines>`
.. |spi_master|         replace:: :doc:`SPI Controller <spi-controller>`
.. |flash_spi|          replace:: :ref:`Firmware Flash SPI <firmware-spi>`
.. |alow|               replace:: :term:`active-low`
.. |soc|                replace:: Management SoC
.. |uart|               replace:: :doc:`UART <uart>`
.. |hkspi-user-pass|    replace:: :ref:`User SPI pass-thru <hkspi-user-pass>`
.. |TBC|                replace:: :tbc:`(TBC! TO BE CONFIRMED or COMPLETED)`
.. |user_mode|          replace:: :ref:`"USER" mode <user_mode>`
.. |mgmt_mode|          replace:: :ref:`"MGMT" mode <mgmt_mode>`
.. |reserved_gpios|     replace:: :ref:`GPIOs reserved for HKSPI and debugging <reserved_gpios>`

.. |resetb|             replace:: :ref:`resetb <resetb>`
.. |sck|                replace:: :ref:`SCK <sck>`
