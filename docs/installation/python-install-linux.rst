Python Installation on Linux
++++++++++++++++++++++++++++++++

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.X.

Check if Python is Installed
----------------

  * python --version
  * python3 --version

Install Python 3 (if not there)
----------------

  * sudo yum install python36
  
Add below in .bash_profile
-----------

  * alias python='python3'
  * export PYSPARK_PYTHON=/usr/bin/python3
  * export PYSPARK_DRIVER_PYTHON=/usr/bin/python3  

Sometimes a soft link to Pythons’s executables is broken for some reason.  
   sudo ln -s /usr/bin/python3.6 /usr/bin/python
   
Install pip/wheel
-----------------

  * yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  * yum install python-pip
  * yum install python-wheel


Install Other Packages
----------------------

Install the required packages:

   * pip install -r requirements.txt
   
requirements.txt file is available in the installation directory of fire insights.

* fire-x.y.x/dist/fire/requirements.txt

Reference
---------

  * https://docs.aws.amazon.com/cli/latest/userguide/install-linux-python.html
  


