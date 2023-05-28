Linux Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed to run natively on Linux machines using the binary bundled as a TAR. It can also be connected to a Spark cluster to submit jobs to cluster.


Prerequisites
=============

Supported Linux Versions
-------------------------

::

  - CentOS : 7+
  - Ubuntu : 18.04 and 20.04
  - RHEL : 8


Below are required for installing Sparkflows on Linux machine::

  - JDK 1.8 installed.
  - Java and JAR should be in the PATH
  - 8 GB+ of RAM (16 GB+ recommended).


Below is needed if Sparkflows would connect and submit jobs to an Apache Spark Cluster::

  - Spark 3.X is needed on the cluster


If there is need to run the PySpark engine (optional)::

  - Python 3.7 needs to be set up on the machine

    
Downloading and Installing Java 8
---------------------------------

* Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html

* Set the ``JAVA_HOME`` property.

There are various ways for Installing Java 8 on Linux. Some are listed below.


Install using Linux RPM Package
+++++++++++++++++++

- Download the Linux x64 RPM Package.

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


References
----------

* Install JAVA on CentOS and Fedora: https://www.digitalocean.com/community/tutorials/how-to-install-java-on-centos-and-fedora
* OpenJDK download link: https://openjdk.java.net/install/
* Install OpenJDK on Ubuntu: https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html



Quick Installation Steps of Fire with H2 Database
===========================================

To get started quickly with minimal install and configuration of Sparkflows, please use the steps given below. If you want a production ready environment, please follow the steps in the next section.

* Download the fire ``TGZ`` file from: https://www.sparkflows.io/download
  
* Unpack it::

    tar xvf fire-x.y.z.tgz

* Create H2 Database::

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

Use the below steps to deploy Sparkflows in production grade environment. Once, the Install steps are complete, you would ideally like to visit the Configuration section of the doc to configure LDAP, S3 and others: https://docs.sparkflows.io/en/latest/installation/configuration/index.html

* Glossary:

  * ``<install_dir>`` : location where you unzipped Sparkflows TGZ file. For example, this can be your home directory.
  * ``<machine_name>`` : hostname where your installed Sparkflows.
  * ``#`` : used for comments and documentation.


* Download the Sparkflows ``TGZ`` file from:

  * https://www.sparkflows.io/download
  
  
* Unzip it::

    tar xvf fire-x.y.z.tgz


* Set up the metadata Database.

  Sparkflows can be configured to store its metadata into H2 Database, MySQL, Microsoft SQL Server or Aurora MySQL database. For production grade install, one can use any of the above except for H2 Database. More details can be found here: https://docs.sparkflows.io/en/latest/installation/configuration/database/index.html
    
* Launch Fire server::

    cd <fire install_dir>
    ./run-fire-server.sh start
    
* Test by opening your web browser and going to::

    http://localhost:8080 OR http://<machine_name>:8080 (Access over http)
    
    https://localhost:8443 OR https://<machine_name>:8443 (Access over https)

* Login with::

    Username: admin
    Password: admin


.. note::  Two user accounts come preconfigured with Fire.

           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Fire under the menu Administration/Users.
    

Installing and starting the Python engine
=========================================

Sparkflows comes with Java engine and Python engine. Following the above steps, we have installed Sparkflows and started it only with Java engine. If you want to leverage the capabilities of python Machine Learning libraries as well, please install the Python engine by following the below:

* On Ubuntu, the python dependencies can be installed by following the steps here: :ref:`Python install on Ubuntu<Python Installation on Ubuntu>`

* On RedHat and CentOS, the python dependencies can be installed by following the steps here: :ref:`Python install on RedHat and CentOS<Python Installation on Red Hat and CentOS>`

  
Helpful Commands
===========================

* Stopping the Fire Server::
   
  ./run-fire-server.sh stop


* Creating a new Linux user::

   sudo useradd -p password sparkflows


* Changing the password of a user::

   sudo passwd sparkflows


* Forwarding traffic to a port::
  
   sudo firewall-cmd --add-forward-port=port=443:proto=tcp:toport=8443 --permanent
   sudo firewall-cmd --reload


Upgrading Steps
==============

To upgrade Sparkflows, one needs to follow the steps given below:

* Download the new Fire TGZ file from::

    https://www.sparkflows.io/download  
  
  
* Stop Fire Server using the below command from Fire home directory using the command::

      run-fire-server.sh stop
  
* Unpack the TGZ file using the command::

      tar xvf fire-x.y.z.tgz

* Upgrade the H2 database or MySQL database:

   * If you have updated the ``conf/db.properties`` file, copy it from your old location to the new directory.
   * Backup your existing H2 database files. By default they are in your home directory as ``firedb.mv.db``.
   * If you are using MySQL, backup the fire database in MySQL.
   * Execute the following commands to create and upgrade the Fire database schema::

        cd <install_dir>/fire-x.y.z
    
        Run this create and upgrade database script if using H2 database: ./create-h2-db.sh           OR      
        Run this create and upgrade database script if using MySQL database: ./create-mysql-db.sh
    

* If PySpark engine is installed, upgrade python dependencies.

  * Activate the python environment by running from Fire home directory::

       source env/bin/activate 
    
  * Upgrade the dependencies in the environment via::
    
       pip install -r fire-x.y.x/dist/fire/requirements.txt

* Restart Fire Server.

   Restart the Fire server using the below command from Fire home directory using the command::

      run-fire-server.sh start

