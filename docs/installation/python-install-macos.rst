Python Installation on MacOS
++++++++++++++++++++++++++++++++

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.6+.

Check if Python is Installed
----------------

  * python --version
  * python3 --version


Install Python 3 (if not already there)
----------------
 
  * One way to install Python 3 on macOS is by installing Anaconda
       https://docs.anaconda.com/anaconda/install/mac-os/
  
  * Use `brew install python3`

Add below in .bash_profile
-----------

  * alias python='python3'
  * export PYSPARK_PYTHON=/usr/bin/python3
  * export PYSPARK_DRIVER_PYTHON=/usr/bin/python3  
  
Sometimes a soft link to Pythons’s executables is broken for some reason.  
   sudo ln -s /usr/bin/python3.x /usr/bin/python
   
Install Other Packages
----------------------

Install the required python packages for Fire Insights:

   * pip install -r requirements.txt
   
requirements.txt file is available in the installation directory of Fire Insights.

* fire-x.y.x/dist/fire/requirements.txt



