Install on Linux/Mac OS
^^^^^^^^^^^^^^^^^^^^^^^

Fire can run independently on any machine, since we package Apache Spark along with or it can be connected to a Spark cluster.

If Sparkflows Fire needs to be connected to a Spark Cluster, install it on an edge node of the cluster. The edge node has the hadoop binaries and spark configs.

Prerequisites
-------------

Below are the Prerequisites for installing Fire on a machine::

  - JDK 1.8+ installed.
  - java and jar have to be in the PATH
  - 5GB+ of RAM.
  - Python 3.X (when running Python and PySpark, otherwise not needed)


If Fire would be connected to an Apache Spark Cluster::

  - Spark 1.6+ or Spark 2.X is needed on the cluster
  - Fire has to be installed on an Edge node of the Spark Cluster


Quick Installation Steps of Fire with H2 DB
-------------------------------------------

* Download the fire tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz


* Create H2 DB::

      cd <fire install_dir>
      ./create-h2-db.sh

* Launch Fire::

    cd <fire install_dir>
    ./run-fire.sh start
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    <machine_name>:8080/index.html

* Login with:: 

    admin/admin or test/test

::Note
    Python can be set up with the Python virtual environment.
    source venv/bin/activate

    

Detailed Installation Steps
---------------------------

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
    
* Launch Fire::

    cd <fire install_dir>
    ./run-fire.sh start
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start
    
* Test by opening your web browser and going to::

    localhost:8080/index.html

    OR

    <machine_name>:8080/index.html

* Login with::

    username: admin and password: admin.


.. note::  Two user accounts come preconfigured with Fire.

           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Fire under the menu Administration/Users
    
    
.. note:: In Local mode, Sparkflows Fire runs in a Jetty server and all the spark jobs are executed within the web-server


Stopping Fire
------------------------

Stop Fire with the below::

    ./run-fire.sh stop
    
    
Stopping the Fire Server
------------------------

Stop the Fire Server with the below::

    ./run-fire-server.sh stop
    
    
Connecting to Apache Spark Cluster
----------------------------------

Now that you have Fire installed, you may want to connect it to your Apache Spark Cluster.

* :doc:`../connecting-spark-cluster`


.. _Download: https://www.sparkflows.io/download



