Python Installation
=======

Python installations from source with version 3.6.5 

Showing warning message with missing package while restarting pyspark server
---------------

Problem
++++++

Showing warning message with missing package while restarting pyspark server::

   UserWarning: Could not import the lzma module. Your installed Python is incomplete
  
Possible Solution
++++++

For centos: Install development tool::

  sudo yum install -y xz-devel

Recompile python from source code::

 cd Python-3.6.5
 sudo ./configure --enable-optimizations
 sudo make altinstall
