Python Installation on Ubuntu 18.04 and 20.04
=============================

Python is only needed if you need to use the PySpark engine enabled in Sparkflows. Python modules in Sparkflows is compatible with Python 3.7.

Check if Python 3.8 is Installed
---------------------------------

Use the below commands::

  python --version
  python3.8 --version

Install Python 3.8 (if not installed)
-------------------------------------

Some References for Installing Python: (https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/ )


* Update the packages list and install the packages necessary to build Python source::

    sudo apt update

  .. figure:: ../../_assets/configuration/update_ubuntu.PNG
   :alt: Installations
   :width: 90%

* Install needed dependency::

   sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev

  .. figure:: ../../_assets/configuration/software_update.PNG
   :alt: Installations
   :width: 90%   

  
* Download python from below Link

  * https://www.python.org/downloads/
  * https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz

* Download and untar::
  
    wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz

  ::
  
      tar xzf Python-3.8.10.tgz

  .. figure:: ../../_assets/configuration/python_download.png
         :alt: Installations
         :width: 90%

* Next, navigate to the Python source directory and run the configure script which will perform a number of checks to make sure all of the dependencies on your system are present::

    cd Python-3.8.10

  .. figure:: ../../_assets/configuration/cd_python.PNG
   :alt: Installations
   :width: 90%

* Build & compile::

    sudo ./configure --enable-optimizations
 
  .. figure:: ../../_assets/configuration/configure_ubuntu.PNG
   :alt: Installations
   :width: 90%
   
* Install the Python binaries by running the following command:: 
 
   sudo make altinstall

  .. figure:: ../../_assets/configuration/make.PNG
   :alt: Installations
   :width: 90%

Note: Do not use the standard make install as it will overwrite the default system python3 binary.

Verify it by typing::

  python3.8 –-version

::

  cd ..

.. figure:: ../../_assets/configuration/python_version.png
   :alt: Installations
   :width: 60% 

Create Python virtual environment & Activate it
---------------------------------

Create Python virtual environment & Activate it::

  python3.8 -m venv venv

::

  source venv/bin/activate

::

  python --version
  
.. figure:: ../../_assets/configuration/python_version1.png
   :alt: Installations
   :width: 60% 
  

Upgrade pip version
-------------------
Upgrade pip version with 20.0 or above::

 pip install pip --upgrade
  
.. figure:: ../../_assets/configuration/pipupdate.PNG
   :alt: Installations
   :width: 90%  
   
Install dependency for prophet package (Ubuntu 18.04)
-----------------------------------------

* pystan dependency::
  
   pip install pystan

  .. figure:: ../../_assets/configuration/pystan.PNG
   :alt: Installations
   :width: 90% 


* convertdate dependency::

   pip install convertdate

  .. figure:: ../../_assets/configuration/convertdate.PNG
   :alt: Installations
   :width: 90% 

* prophet dependency::

   pip install prophet

  .. figure:: ../../_assets/configuration/fbprophet.PNG
   :alt: Installations
   :width: 90% 

* Check pip list::
   
   pip list

  .. figure:: ../../_assets/configuration/piplist.PNG
   :alt: Installations
   :width: 90% 

Install required packages
-------------------------

Install the required python packages for Fire Insights::

  pip install -r fire-x.y.x/dist/fire/requirements.txt
   
``requirements.txt`` file is available in the installation directory of Fire Insights.

If connecting to S3 buckets from PySpark
----------------------------------------
If connecting to S3 buckets to read/write data, one would need to download these following JAR's and place them in the virtualenv ``SPARKFLOWS_INSTALL_DIR/venv/lib/python3.7/site-packages/pyspark/jars/`` being used by Sparkflows::

   wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar
   wget https://repo1.maven.org/maven2/com/google/guava/guava/23.0/guava-23.0.jar
   wget https://repo1.maven.org/maven2/org/postgresql/postgresql/42.3.2/postgresql-42.3.2.jar


If using read excel node from PySpark
-------------------------------------
If using read excel node from PySpark, one would need to download these following JAR's and place them in the virtualenv ``SPARKFLOWS_INSTALL_DIR/venv/lib/python3.7/site-packages/pyspark/jars/`` being used by Sparkflows::

   wget https://repo1.maven.org/maven2/com/crealytics/spark-excel_2.12/3.2.2_0.18.5/spark-excel_2.12-3.2.2_0.18.5.jar

Delete a venv
+++++++++++++

To delete a virtual environment, follow below steps::

    source venv/bin/activate

::

    pip freeze > requirements.txt

::

    pip uninstall -r requirements.txt -y

::

    deactivate

::

    rm -r venv/
