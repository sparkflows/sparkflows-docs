Python Installation on Windows
++++++++++++++++++++++++++++++++

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.6+.

Check if Python is Installed
----------------

  * ``python --version``
  * ``python3 --version``

Ensure that you have python version 3.6+ installed.

Install Python 3.6+ (if not already installed)
----------------

  * Download python from below Link
     * https://www.python.org/downloads/
     * https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe
  * Install and configure it. Check the option for adding path by default on first page of installation, so that you do not need to add it to the path manually. 

Once the installation is complete, open command prompt to see if python is installed or not

  * ``python --version`` 
  
Create System Variable PYTHONPATH
----------------------------------

Create a new system variable called ``PYTHONPATH`` with values like shown in the screenshots below.

.. figure:: ../_assets/installation/pythonpathvariable.PNG
   :alt: Installations
   :align: center
   :width: 60%

.. figure:: ../_assets/installation/python_path.PNG
   :alt: Installations
   :align: center
   :width: 60%

Also add to system path
-----------------------

.. figure:: ../_assets/installation/systempath.PNG
   :alt: Installations
   :align: center
   :width: 60%
 
   
Upgrade pip version
-------------------

  * ``pip install --user --upgrade pip``


Install Other Dependent Packages
----------------------

Install the other required packages:

   * pip install -r requirements.txt
   
``requirements.txt`` file is available in the installation directory of Fire Insights : fire-x.y.x/dist/fire/requirements.txt

Once the above steps have completed successfully, run the below command to ensure everything was setup correctly.

* ``python ./dist/__main__.py``

.. figure:: ../_assets/installation/pyspark_server.PNG
   :alt: Installations
   :align: center
   :width: 60%

Enable PySpark Engine in Fire Insights
--------------------------------------

Login to Fire Insights application and go to configurations and set ``app.enablePySparkEngine`` to ``true`` and save the changes. Now you can start using PySpark engine in Fire Insights. 

.. figure:: ../_assets/installation/pyspark_url.PNG
   :alt: Installations
   :align: center
   :width: 60%
