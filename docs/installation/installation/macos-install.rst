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

There are various ways for Installing Java 8 on MacOS X. Some are listed below.

Installing JDK on Mac
+++++++++++++++++

- Download the ``DMG`` file and install it by double clicking on it: Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html
- Installing using ``brew`` by running ``brew install openjdk@8``

You would need to set ``JAVA_HOME`` as well.

Quick Installation Steps of Fire with H2 Database
===========================================

* Download the fire ``TGZ`` file from:

  * https://www.sparkflows.io/download

* Create a new directory named ``sparkflows`` and copy the TGZ file into it::

    mkdir sparkflows

  ::

    cp fire-x.y.z.tgz sparkflows

  ::

    cd sparkflows
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz

* Create H2 Database::

      cd <sparklows/fire-3.X.YY_spark_3.2.1>

  ::

      ./create-h2-db.sh

* Sparkflows can be configured to run with H2 Database or MySQL. H2 Database is very easy to set up with Sparkflows. For production deployments, MySQL is recommended.
    
* Launch Fire Server::

    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    http://<machine_name>:8080 OR https://<machine_name>:8443

* Login with:: 

    admin/admin or test/test

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

