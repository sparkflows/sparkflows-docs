MacOS Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can run independently on a machine since we package Apache Spark along with it. It can also be connected to a Spark cluster to submit jobs.

Prerequisites
=============

Supported MacOS Versions
-------------------------

::

  - MacOS released not older than 1 year is supported


Below are required for installing Sparkflows on Mac::

  - JDK 1.8+ installed.
  - java and jar have to be in the PATH
  - 8 GB+ of RAM.
  - Python 3.7+ (when running Python and PySpark, otherwise not needed)

    
Downloading and Installing Java 8
---------------------------------

Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html

You would need to set ``JAVA_HOME`` as well.

There are various ways for Installing Java 8 on MacOS X. Some are listed below.


Installing JDK on Mac
+++++++++++++++++

- Download the ``DMG`` file
- Install it by double clicking on it
- Installing using ``brew``


Quick Installation Steps of Fire with H2 Database
===========================================

* Download the fire ``TGZ`` file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives

* Create a new directory named ``sparkflows`` and copy the TGZ file into it:

  * cp fire-x.y.z.tgz ``sparkflows``
  * cd ``sparkflows``
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz

* Create H2 Database::

      cd <fire install_dir>

  ::

      ./create-h2-db.sh
    
* Launch Fire Server::

    cd <fire install_dir>

  ::

    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    http://<machine_name>:8080

* Login with:: 

    admin/admin or test/test

    

Detailed Installation Steps
===========================

* Glossary

  * ``<install_dir>`` : location where you unzipped Sparkflows tgz file. For example this can be your home directory.
  * ``<machine_name>`` : hostname where your installed Sparkflows
  * ``#`` : used for comments and documentation


* Download the Sparkflows tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unzip it::

    tar xvf fire-x.y.z.tgz


* Set up H2 or MySQL Database

  Sparkflows can be configured to run with H2 Database or MySQL. H2 Database is very easy to set up with Sparkflows. For production deployments, MySQL is recommended.
    
   
* Launch Fire server::

    cd <fire install_dir>

  ::

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

    Username: admin
    Password: admin


.. note::  Two user accounts come preconfigured with Fire.

           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Fire under the menu Administration/Users
    

Python Installation 
====================

Python is only needed if you need to use the PySpark engine enabled in Sparkflows. Python modules in Sparkflows is compatible with Python 3.7

Check if Python 3.7 is Installed
---------------------------------

Use one of the below commands to check if the Python is installed on the machine or not::

  python --version
  python3 --version


Install Python 3.7 (if not installed)
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


Stopping the Fire Server
------------------------

Stop the Fire Server with the below::

    ./run-fire-server.sh stop
    


Forwarding traffic to a port
+++++++++++++++++++++++++++++

::

    sudo firewall-cmd --add-forward-port=port=443:proto=tcp:toport=8443 --permanent

::

    sudo firewall-cmd --reload

