Linux/Mac OS X Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can run independently on a machine since we package Apache Spark along with it. It can also be connected to a Spark cluster to submit jobs.

If Sparkflows needs to be connected to a Spark Cluster, install it on an edge node of the cluster. The edge node would have the hadoop binaries and spark configs which will be picked up while submitting the jobs.

Prerequisites
=============

Supported Linux Versions
-------------------------

::

  - CentOS : 7+
  - Ubuntu : 18+
  - RHEL : 8+


Below are required for installing Sparkflows on Mac or Linux machine::

  - JDK 1.8+ installed.
  - java and jar have to be in the PATH
  - 8 GB+ of RAM.
  - Python 3.7+ (when running Python and PySpark, otherwise not needed)


If Sparkflows would be connected to an Apache Spark Cluster::

  - Spark 2.X is needed on the cluster
  - Sparkflows has to be installed on an Edge node of the Spark Cluster


If using Python and PySpark (optional) ::

  - Python 3.7+ needs to be set up on the machine

    
Downloading and Installing Java 8
---------------------------------

Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html

You would need to set ``JAVA_HOME`` as well.

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

Installing JDK on Mac
+++++++++++++++++

- Download the ``dmg`` file
- Install it by double clicking on it
- Installing using ``brew``


References
----------

* Install JAVA on CentOS and Fedora - https://www.digitalocean.com/community/tutorials/how-to-install-java-on-centos-and-fedora
* OpenJDK download link - https://openjdk.java.net/install/
* Install OpenJDK on Ubuntu - https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html



Quick Installation Steps of Fire with H2 DB
===========================================

* Download the fire ``TGZ`` file from:

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

  * ``<install_dir>`` : location where you unzipped Sparkflows tgz file. For example this can be your home directory.
  * ``<machine_name>`` : hostname where your installed Sparkflows
  * ``#`` : used for comments and documentation


* Download the Sparkflows tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unzip it::

    tar xvf fire-x.y.z.tgz


* Set up H2 or MySQL DB

  Sparkflows can be configured to run with H2 DB or MySQL. H2 DB is very easy to set up with Sparkflows. For production deployments, MySQL is recommended.
    
   
* Launch Fire server::

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

    Username: admin
    Password: admin


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

