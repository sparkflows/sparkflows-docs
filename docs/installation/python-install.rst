Python Installation
++++++++++++++++++++++++++++++++

Python is only needed is you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.X.

Install Python 3
----------------

Below are the steps for installing Python-3.6 on Centso7 if it is not already installed. They need to be performed as the root user.

  * cat /etc/os-release
  * curl -O https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
  * tar xf Python-3.6.4.tgz
  * cd Python-3.6.4
  * yum install gcc
  * ./configure
  * make
  * make install
  * yum install libffi-devel
  * export PATH=$PATH:/usr/local/bin/python3.6

Install pip/wheel
-----------------

  * yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  * yum install python-pip
  * yum install python-wheel


Install Other Packages
----------------------
Check the requirements.txt https://github.com/sparkflows/writing-new-node/blob/master/requirements.txt to install all the required packages.

   * pip install -r requirements.txt
