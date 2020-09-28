Python Installation on Windows
++++++++++++++++++++++++++++++++

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.X.

Check if Python is Installed
----------------

  * python --version
  * python3 --version

Install Python 3 (if not there)
----------------

Just ensure that Windows machine should have python with version 3.6+

  * Download python from below Link
     * https://www.python.org/downloads/
     * https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe
  * Installed and configured it, Checkbox the option of adding path by default on first page of installations, so that we dont need to add in the path. 
  
Once the installation complete, open command prompt to see if python installed or not

  * python --version 
  
Upgrade pip version
-------------------

  * ``pip install --user --upgrade pip``


Install Other Packages
----------------------

Install the required packages:

   * pip install -r requirements.txt
   
``requirements.txt`` file is available in the installation directory of Fire Insights.

* fire-x.y.x/dist/fire/requirements.txt

Once the above steps completed successfully, just run the below command, if its running fine

* ``python ./dist/__main__.py``

.. figure:: ../_assets/installation/pyspark_server.PNG
   :alt: Installations
   :align: center
   :width: 60%

* Once you start fire server, login to Fire Insights application and go to configurations and enable ``app.enablePySparkEngine as true`` and save the changes and start using PySpark engine in Fire Insights. 

.. figure:: ../_assets/installation/pyspark_url.PNG
   :alt: Installations
   :align: center
   :width: 60%


