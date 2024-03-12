Python Installation on Macbook
====================

Python is only needed if you need to use the PySpark engine enabled in Sparkflows. Python modules in Sparkflows is compatible with Python 3.7

Check if Python 3.8 is Installed
---------------------------------

Use one of the below commands to check if the Python is installed on the machine or not::

  python --version
  python3 --version


Install Python 3.8 (if not installed)
---------------------------------------
 
* One way to install Python 3 on macOS is by installing Anaconda https://docs.anaconda.com/anaconda/install/mac-os/
* Use ``brew install python3``

Add below in bash_profile
--------------------------

For the python to be available system wide, add the below into bash_profile::

  alias python='python3'
  export PYSPARK_PYTHON=/usr/bin/python3
  export PYSPARK_DRIVER_PYTHON=/usr/bin/python3
  
Sometimes a soft link to Pythons’s executables is broken for some reason::

  sudo ln -s /usr/bin/python3.x /usr/bin/python
   
Create Python virtual environment & Activate it
-----------------------------------------------

Create Python virtual environment & Activate it::

  python -m venv venv

::

  source venv/bin/activate

::

  python --version

Install required Packages
-------------------------

Install the required python packages for Fire Insights::

  pip install -r fire-x.y.x/dist/fire/requirements.txt
   
``requirements.txt`` file is available in the installation directory of Fire Insights.

Restart the Fire Server to start the Python engine
---------------------------------------------------

To make use of Python engine of Fire, restart the server using the below command::

    ./run-fire-server.sh restart
