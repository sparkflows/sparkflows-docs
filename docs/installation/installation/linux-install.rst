Linux/Mac OS Installation
^^^^^^^^^^^^^^^^^^^^^^^

Fire can run independently on any machine, since we package Apache Spark along with or it can be connected to a Spark cluster.

If Sparkflows Fire needs to be connected to a Spark Cluster, install it on an edge node of the cluster. The edge node has the hadoop binaries and spark configs.

Prerequisites
=============

Supported Linux Versions
-------------------------

::

  - CentOS : 7+
  - Ubuntu : 18+
  - RHEL : 8+

Prerequisites
-------------

Below are the Prerequisites for installing Fire Insights on a Mac or Linux machine::

  - JDK 1.8+ installed.
  - java and jar have to be in the PATH
  - 8 GB+ of RAM.
  - Python 3.7+ (when running Python and PySpark, otherwise not needed)


If Fire would be connected to an Apache Spark Cluster::

  - Spark 2.X is needed on the cluster
  - Fire has to be installed on an Edge node of the Spark Cluster


If using Python and PySpark (not needed for the core features of Fire Insights) ::

  - Python 3.X can be set up with the Python virtual environment and activated

    
Downloading and Installing Java 8
---------------------------------

Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html

You may have to set JAVA_HOME after the installation.

There are various ways for Installing Java 8 on Linux. Some are listed below.


Using Linux RPM Package
+++++++++++++++++++

- Download the Linux x64 RPM Package

- Install the package::

    yum localinstall jdk-8u202-linux-x64.rpm (this has to be run as the root user)

- Update ``.bash_profile`` to add the below::

    export JAVA_HOME=/usr/java/jdk1.8.0_202-amd64/
    export PATH=$PATH:$JAVA_HOME/bin

Install OpenJDK8 JDK using yum
++++++++++++++++++

::

  yum -y update
  yum install java-1.8.0-openjdk-devel

Installing on Mac
+++++++++++++++++

- Download the dmg file
- Install it


Reference
---------

Links
+++++

* https://www.digitalocean.com/community/tutorials/how-to-install-java-on-centos-and-fedora



Download OpenJDK
+++++++++++++

- https://openjdk.java.net/install/

- Install OpenJDK on Ubuntu

https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html



Quick Installation Steps of Fire with H2 DB
====================================

* Download the fire tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz

* Create H2 DB::

      cd <fire install_dir>
      ./create-h2-db.sh
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    <machine_name>:8080

* Login with:: 

    admin/admin or test/test

    

Detailed Installation Steps
===========================

* Glossary

    * ``<install_dir>`` : location where you unzipped fire tgz file. For example this can be your home directory.
    * ``<machine_name>`` : hostname where your installed Fire
    * ``#`` : used for comments and documentation


* Download the fire tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unzip it::

    tar xvf fire-x.y.z.tgz


* Set up H2 or MySQL DB

Fire can be configured to run with H2 db or MySQL. H2 is very easy to set up with Fire. For production deployments MySQL is recommended.

    * :doc:`../database/h2-db`
    * :doc:`../database/mysql-db`
    
   
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start
    
* Test by opening your web browser and going to::

    http://localhost:8080

    OR

    http://<machine_name>:8080
    
    OR
    
    https://localhost:8443
    
    OR
    
    https://<machine_name>:8443

* Login with::

    username: admin and password: admin.


.. note::  Two user accounts come preconfigured with Fire.

           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Fire under the menu Administration/Users
    
  
    
Stopping the Fire Server
------------------------

Stop the Fire Server with the below::

    ./run-fire-server.sh stop
    
    
Connecting to Apache Spark Cluster
----------------------------------

Now that you have Fire installed, you may want to connect it to your Apache Spark Cluster.

* :doc:`../configuration/connecting-spark-cluster`


.. _Download: https://www.sparkflows.io/download


Python Installation on Linux - Redhat/CentOS
============================

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.7+.

Check if Python 3.7+ is Installed
----------------

Use the below commands::

    python --version
    python3.7 --version
    

Install Python 3.7 (if not installed)
----------------

Some References for Installing Python:

  * CentOS : https://tecadmin.net/install-python-3-7-on-centos/

Prerequisites
+++++++++++++

Python installation requires the GCC compiler to be available on the machine. Use the following command to install the prerequisites for installing Python::

    yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel
    

Download and extract the downloaded package  
++++++++++++++++++++++++++++++
  
  * Download python from below Link
     * https://www.python.org/downloads/
     * https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

Download and untar::
  
     wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
     tar xzf Python-3.7.0.tgz
     

Compile Python source code
+++++++++++++++++++

Compile the Python source code on your system using altinstall::

    cd Python-3.7.0
    ./configure --enable-optimizations
    make altinstall
    python3.7 –-version
  
.. figure:: ../../_assets/configuration/python3_7.PNG
   :alt: Installations
   :width: 60% 

Create Python virtual environment & Activate it
---------------------------------

Create Python virtual environment & Activate it::

  python3.7 -m venv venv
  source venv/bin/activate
  python --version

.. figure:: ../../_assets/configuration/venv_python.PNG
   :alt: Installations
   :width: 60%

.. figure:: ../../_assets/configuration/version_python.PNG
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

Install Other Packages
----------------------

Install the required packages
::

  cd fire-x.y.x/dist/fire
  pip install -r requirements.txt
   
``requirements.txt`` file is available in the installation directory of fire insights::

  fire-x.y.x/dist/fire/requirements.txt

Reference
---------

Links
+++++

  * https://docs.aws.amazon.com/cli/latest/userguide/install-linux-python.html
  * https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-python3-boto3/
  * https://blog.teststation.org/centos/python/2016/05/11/installing-python-virtualenv-centos-7/
  
Delete a venv
+++++++++++++

To delete a virtual environment, follow below steps::

  source venv/bin/activate
  pip freeze > requirements.txt
  pip uninstall -r requirements.txt -y
  deactivate
  rm -r venv/

Installing pip & wheel
+++++++++++++++++++

  * yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  * yum install python-pip
  * yum install python-wheel
  
  
Add below in .bash_profile
++++++++++++++++++++++++++

  * export PYSPARK_PYTHON=/usr/bin/python3
  * export PYSPARK_DRIVER_PYTHON=/usr/bin/python3  



   
For Ubuntu
----------

  * Ubuntu : https://docs.python-guide.org/starting/install3/linux/
  
   
Helpful Commands
----------------

Creating a new Linux user
+++++++++++++++++++++++
::

    sudo useradd -p password sparkflows

Changing the password of a user
+++++++++++++++++++++++
::

    sudo passwd sparkflows


Forwarding traffic to a port
+++++++++++++++++++++++++++++

::

    sudo firewall-cmd --add-forward-port=port=443:proto=tcp:toport=8443 --permanent
    sudo firewall-cmd --reload

