Python Installation on Linux - Ubuntu
============================

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.7+.

Check if Python 3.7+ is Installed
----------------

  * ``python --version``
  * ``python3.7 --version``

Install Python 3.7 (if not installed)
----------------

Some References for Installing Python:

* Ubuntu : https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/

Prerequisites
+++++++++++++

update the packages list and install the packages necessary to build Python source:

  * ``sudo apt update``
   
.. figure:: ../_assets/configuration/update_ubuntu.PNG
   :alt: Installations
   :align: center
   :width: 60%

  * ``sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev``

.. figure:: ../_assets/configuration/software_update.PNG
   :alt: Installations
   :align: center
   :width: 60%   
