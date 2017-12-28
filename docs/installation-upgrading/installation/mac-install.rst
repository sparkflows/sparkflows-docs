Install on Linux/Mac OS
^^^^^^^^^^^^^^^^^^^^^^^

Fire can run independently on any machine, since we package Apache Spark along with or it can be connected to a Spark cluster.

If Sparkflows Fire needs to be connected to a Spark Cluster, install it on an edge node of the cluster. The edge node has the hadoop binaries and spark configs.

Prerequisites
-------------

  * JDK 1.7+ installed.
  * java and jar have to be in the PATH
  * If running on a Spark cluster, Spark 1.6+ is needed on the cluster.
  * 3GB+ of RAM.


Quick Installation Steps of Fire with H2 DB
-------------------------------------------

  * Download and unpack  :  fire-1.4.2.tgz
  * Create H2 DB

      cd <fire install_dir>
      ./create-h2-db.sh

  * Launch fire server

      cd <fire install_dir>
      ./run-fire-server.sh start

  * Open your web browser and navigate to: <machine_name>:8080/index.html.

      Login with admin/admin or test/test


Detailed Installation Steps
---------------------------

  * **Glossary**

    * <install_dir> : location where you unzipped fire tgz file. For example this can be your home directory.
    * <machine_name> : hostname where your installed Fire
    * # : used for comments and documentation


  * Download and unzip the sparkflows tgz file

    * Download the fire tgz file
    * Unzip it : tar xvf fire-1.4.2.tgz


  * Set up H2 or MySQL DB


    Fire can be configured to run with H2 db or MySQL. H2 is very easy to set up with Fire. For production deployments MySQL is recommended.

​
      * H2 DB Configuration
      * MySQL Configuration

Launching Fire after Installation
---------------------------------

  * cd <install_dir>/fire-1.4.2
  * Execute ./run-fire-server.sh
  * Test by opening your web browser and going to:
    localhost:8080/index.html

    OR

    <machine_name>:8080/index.html

  * When you see the login window, enter username: admin and password: admin.

    Note: You may change the password for the two accounts which come pre-configured to your choice of password from the Fire UI - Administration tab.

        admin/admin
        test/test

    Note: In Local mode, Sparkflows Fire runs in a Jetty server and all the spark jobs are executed within the web-server

    `Connecting Fire to a Spark cluster`_


Stopping the Fire Server
------------------------

  * ./run-fire-server.sh stop
