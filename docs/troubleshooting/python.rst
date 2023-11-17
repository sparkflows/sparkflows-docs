Python Installation
=======

This document segment addresses common challenges encountered by our users during Python installations from source with version 3.6.5 and provides effective resolutions for each issue.


1. Showing Warning Message for Missing Package
----------------

**Problem**
++++++

Showing warning message with missing package while restarting pyspark server::

   UserWarning: Could not import the lzma module. Your installed Python is incomplete
  
**Solution**
++++++

For centos: Install development tool::

  sudo yum install -y xz-devel

Recompile python from source code::

 cd Python-3.6.5
 sudo ./configure --enable-optimizations
 sudo make altinstall


2. Issue with Python Version 3.9
---------------------

**Problem**
+++++++
I installed Python 3.9 and running into issues.

**Solution**
+++++
Only Python 3.7 or 3.8 are supported. Please terminate the machine on which you installed 3.9 and start with a fresh machine.

To know where the python is installed, on the machine:

* To know all locations python:
  ::

   whereis python3

* To know location of python being used:
  ::

   which python3
