Python Installation on Red Hat and CentOS
====================================

Python is only needed if you need to use the PySpark engine enabled in Sparkflows. Python modules in Sparkflows is compatible with Python 3.9.

Check if Python 3.9 is Installed
---------------------------------

Use one of the below commands to check if the Python is installed on the machine or not::

  python --version

::

  python3 --version

    

Install Python 3.9 (if not installed)
-------------------------------------

Some References for Installing Python:

* CentOS : https://tecadmin.net/install-python-3-7-on-centos/

Prerequisites
+++++++++++++

Python installation requires the GCC compiler to be available on the machine. Use the following command to install the prerequisites for installing Python::

    sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget make
    

Download and extract the downloaded package  
++++++++++++++++++++++++++++++
  

Download python from below Link

* https://www.python.org/downloads/
* https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz

Download and untar::
  
     wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz

::

     tar xzf Python-3.9.10.tgz
     

Compile Python source code
+++++++++++++++++++

Compile the Python source code on your system using altinstall::

    cd Python-3.8.10

::

    ./configure --enable-optimizations

::

    sudo make altinstall

::

    python3.9 --version

::

    cd ..
  
.. figure:: ../../_assets/configuration/python_version.png
   :alt: Installations
   :width: 60% 

Create Python virtual environment & Activate it
---------------------------------

Create Python virtual environment & Activate it::

  python3.9 -m venv venv

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

.. figure:: ../../_assets/configuration/upgrade-pip.PNG
   :alt: Installations
   :width: 60%

Install dependency for prophet package (CentOS 7)
-----------------------------------------

Run below command with sudo privilege
++++++++++++++++++++++++++++++++++

* Install development tool

::

      yum install -y xz-devel
    
.. figure:: ../../_assets/configuration/develop-tool.PNG
   :alt: Installations
   :width: 60%   

* Install the CentOS SCL release file

::

     yum install centos-release-scl
  
.. figure:: ../../_assets/configuration/scl-tool.PNG
   :alt: Installations
   :width: 60% 
   
* Install Developer Toolset version 7

::

    yum install devtoolset-7
  
.. figure:: ../../_assets/configuration/devtool7.PNG
   :alt: Installations
   :width: 60%  
 
* launch a new shell instance using the Software Collection scl tool & Check GCC version
::
 
    scl enable devtoolset-7 bash

::

    gcc --version
   
.. figure:: ../../_assets/configuration/gcc_version.PNG
   :alt: Installations
   :width: 60%    

* Install prophet package
::
   
   pip install prophet

.. figure:: ../../_assets/configuration/fbprophet.PNG
   :alt: Installations
   :width: 60%

* Check pip list
::
   
   pip list

.. figure:: ../../_assets/configuration/list-pip.PNG
   :alt: Installations
   :width: 60%


Reference
---------

Links
+++++

  * https://linuxize.com/post/how-to-install-gcc-compiler-on-centos-7/

Install required Packages
----------------------

Install the required python packages for Fire Insights::

  pip install -r fire-3.x.y_spark_3.2.1/dist/fire/requirements.txt
   
``requirements.txt`` file is available in the installation directory of Fire Insights.

.. Note:: This can run into `Memory error` if there is not enough free RAM on the machine. In that case, please split the dependencies in `requirements.txt` into multiple parts and install.

If connecting to S3 buckets from PySpark
----------------------------------------
If connecting to S3 buckets to read/write data, one would need to download these following JARs and place them in the virtual env ``SPARKFLOWS_INSTALL_DIR/venv/lib/python3.7/site-packages/pyspark/jars/`` being used by Sparkflows::

   wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar

::

   wget https://repo1.maven.org/maven2/com/google/guava/guava/23.0/guava-23.0.jar

::

  wget https://repo1.maven.org/maven2/org/postgresql/postgresql/42.3.2/postgresql-42.3.2.jar


If using read excel node from PySpark
-------------------------------------
If using read excel node from PySpark, one would need to download these following JARs and place them in the virtual env ``SPARKFLOWS_INSTALL_DIR/venv/lib/python3.7/site-packages/pyspark/jars/`` being used by Sparkflows::

   wget https://repo1.maven.org/maven2/com/crealytics/spark-excel_2.12/3.2.2_0.18.5/spark-excel_2.12-3.2.2_0.18.5.jar
   

Reference
---------

* https://docs.aws.amazon.com/cli/latest/userguide/install-linux-python.html
* https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-python3-boto3/
* https://blog.teststation.org/centos/python/2016/05/11/installing-python-virtualenv-centos-7/
  
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

Installing pip & wheel
+++++++++++++++++++

yum install 

::

  yum install python-pip

::

  yum install python-wheel
  
  
Add below in bash_profile
++++++++++++++++++++++++++

::

  export PYSPARK_DRIVER_PYTHON=/usr/bin/python3  

