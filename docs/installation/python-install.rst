Python Installation
++++++++++++++++++++++++++++++++

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.X.

Install Python 3
----------------

Below are the steps for installing Python-3.6 on CentOS 7 if it is not already installed. They need to be performed as the root user.

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

All the required packages can be installed with the below:

   * pip install -r requirements.txt
   
requirements.txt file is available in the insallation directory of fire insights.

* fire-x.y.x/dist/fire/requirements.txt




