Deployment Guide
=======================

Fire can be easily installed on an EC2 machine. It can submit jobs to EMR Livy or AWS Glue. It can also run the jobs locally on the same EC2 machines.

Below are the detailed steps for installing Fire Insights on EMR:

1. Start EMR Cluster on AWS
2. Update inbound rules for Master Node, if necessary
3. SSH into the Master node
4. Download Fire Insights from https://www.sparkflows.io/download
5. Unzip it
6. Create H2 Database
7. Start Fire

Details of each of the above Steps:
----------------------------------

* Start EMR cluster on AWS:

   Start EMR cluster on AWS if it is not already running on your machine.

.. Note:: Inorder to use PySpark engine, you need to add ``bootscript`` to emr cluster before starting from below location:

https://sparkflows-release.s3.amazonaws.com/fire/docker/docker-ubuntu/emr-bootstrap_nump_fix.sh

* Update the inbound rules for the Master Node:

   Fire by default listens on **8080** and **8443**, but EMR clusters have other processes listening on these ports. So, the corresponding settings need to be updated accordingly to listen on ports **8085** and **8086**. This can be done by updating the inbound rules/settings for the master node to allow to listen on ports **8085** and **8086**.
* SSH into the Master EMR node as the ``hadoop`` user::

    ssh -i my.pem hadoop@ec2-xx-yyy-zz-aaa.compute-1.amazonaws.com

* Download the fire tgz file by any one of the following options:

  * https://www.sparkflows.io/download    
       OR
  * wget https://s3.amazonaws.com/sparkflows-release/fire/rel-x.y.z/2/fire-x.y.z.tgz
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz
    
* Copy hadoop-lzo.jar::

    cp /usr/lib/hadoop-lzo/lib/hadoop-lzo.jar /home/hadoop/fire-3.1.0/fire-user-lib
    
* Configure Fire to listen on ports 8085 and 8086::

    - cd <fire install_dir>
    - Edit conf/application.properties
    - Set the HTTP port and the HTTPS port to below:
        http.port=8085
        https.port=8086

* Create H2 Database::

      Fire stores its metadata into the embedded H2 database. You can also connect it to an external MySQL database.

      cd <fire install_dir>
      ./create-h2-db.sh
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    <machine_name>:8085

* Login with the following default username and password:: 

    username : admin
    password : admin
    
* Connect Fire with the EMR cluster::

    - Go to Administration/Configuration.
    - Click on 'Infer Hadoop Configs'.
    - Click on 'Save'.
    
    - If your EMR cluster is not running HIVE, update 'spark.sql-context = SQLContext'.
    
* Create the ``hadoop`` user in Fire::

    - Under Administration/Users, add the 'hadoop' user.
    
Loading Example Workflows
-------------------------

* From the home page of Fire Insights, click on **Load Example Applications**.

* Upload the Fire examples data onto HDFS::

    cd <fire install_dir>
    hadoop fs -put data /tmp
    
Install and Running Example Workflows
------------------------

* Start off with executing the example workflows::

    - Fire comes pre-packaged with a number of example workflows.
    - You can install them by clicking on the 'Install example workflows' link on the landing page when logged in as the `admin` user.
    
* Logout from the current session and login again with the 'hadoop' user.    
    
    - Execute the workflows
    
Adding a New User
-----------------

Create the home directory on HDFS for the new user.

For example, for user 'test'::

 hadoop fs -mkdir /user/test
 hadoop fs -chown test:test /user/test

Create the user in Fire Insights if not already created.


Extra Configuration for Running H2O Workflow
-----------------------------------------

EMR needs additional configurations for running H2O workflow, which can be added while running those workflows.

::

    Spark-submit-conf:  --conf spark.dynamicAllocation.enabled=false


Extra Configuration for Running PySpark
---------------------------------------

EMR needs additional configurations when running PySpark. Below are the steps required for installing the python 3.6 virtual environment in the directory /home/hadoop/venv::

 export SPARK_HOME=/usr/lib/spark/
 export PYSPARK_PYTHON=/home/hadoop/venv/bin/python
 export YARN_CONF_DIR=/etc/hadoop/conf
