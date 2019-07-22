Deployment Guide
=======================

Fire can be easily installed on an AWS EMR Cluster.

Below are the overall steps for installing Fire Insights on EMR.

- *ssh into the Master node*
- *Download Fire Insights* from https://www.sparkflows.io/download
- *Unzip it*
- *Create H2 Database*
- *Start Fire*

Steps
------

* Start your EMR cluster on AWS::

    Start your EMR cluster on AWS if you do not already have it running.

* Update the inbound rules for the Master Node::

    - We would have Fire listening on ports 8085 and 8086
    - Fire by default listens on 8080 and 8443. But EMR clusters have another process listening these ports. 
    - So we change it to listen on port 8085 and 8086
    - Update the inbound rules for the Master Node to allow ports 8085 and 8086

* ssh into the Master EMR node as the ``hadoop`` user::

    ssh -i my.pem hadoop@ec2-xx-yyy-zz-aaa.compute-1.amazonaws.com

* Download the fire tgz file by one of the following options:

  * https://www.sparkflows.io/download    
       OR   
  * https://www.sparkflows.io/archives
       OR
  * wget https://s3.amazonaws.com/sparkflows-release/fire/rel-x.y.z/2/fire-x.y.z.tgz
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz
    
* Copy hadoop-lzo.jar::

    cp /usr/lib/hadoop-lzo/lib/hadoop-lzo.jar /home/hadoop/fire-3.1.0/fire-user-lib
    
* Configure Fire to listen on ports 8085 and 8086::

    - cd <fire install_dir>
    - Edit conf/application.properties
    - Update the last two lines to below:
        http.port=8085
        https.port=8086

* Create H2 DB::

    Fire stores its metadata into the embedded H2 database. You can also connect it to an external MySQL database.

      cd <fire install_dir>
      ./create-h2-db.sh

* Launch Fire::

    cd <fire install_dir>
    ./run-fire.sh start
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    <machine_name>:8085/index.html

* Login with the following default username and password:: 

    username : admin
    password : admin
    
* Connect Fire with the EMR Cluster::

    - Go to Administration/Configuration
    - Click on 'Infer Hadoop Configs'
    - Save
    
    - If your EMR cluster is not running HIVE, update 'spark.sql-context = SQLContext'
    
* Create the ``hadoop`` user in Fire::

    - Under Administration/Users, add the 'hadoop' user
    - Logout from the current session and login again with the 'hadoop' user
    
Running Example Workflows
-------------------------

* Upload the Fire examples data onto HDFS::

    cd <fire install_dir>
    hadoop fs -put data /tmp
    
    
* Start off with executing the example workflows::

    - Fire comes pre-packaged with a number of example workflows
    - You can install them by clicking on the 'Install example workflows' link in the landing page when logged in as the `admin` user.
    
    - Execute the workflows
    
Adding a new user
-----------------

Create the home directory on HDFS for the new user.

For example, for user 'test':

- hadoop fs -mkdir /user/test
- hadoop fs -chown test:test /user/test

Create the user in Fire Insights if not already created.


Extra configuration for running PySpark
---------------------------------------

EMR needs extra configurations when running PySpark. In the below the python 3.6 virtual environment is installed in the directory /home/hadoop/venv

- export SPARK_HOME=/usr/lib/spark/
- export PYSPARK_PYTHON=/home/hadoop/venv/bin/python
- export YARN_CONF_DIR=/etc/hadoop/conf

Fire-UI Port to be updated if running on other port
----------------------------------------------------

- Go to /etc/spark/conf/spark-env.sh & Update the Master_WebUI_Port as per its running
 - export SPARK_MASTER_WEBUI_PORT=****

