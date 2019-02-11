Running Apache Spark Standalone
=======================

Fire can be run on Spark Standalone cluster. In this case, Hadoop does not need to be installed.

Installing Spark Standalone
---------------------------

- First we need to make sure we have Java installed:
- Install Java 

  - wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.rpm"
  - yum localinstall jdk-8u201-linux-x64.rpm
  - Java -version
  
  .. figure:: ../_assets/user-guide/spark_standalone_java_version.PNG
   :scale: 100%
   :alt: Standalone spark
   :align: center
   

We need to install Scala
---------------------------

- Install Scala

  - wget http://www.scala-lang.org/files/archive/scala-2.10.1.tgz
  - tar xvf scala-2.10.1.tgz
  - sudo mv scala-2.10.1 /usr/lib
  - sudo ln -s /usr/lib/scala-2.10.1 /usr/lib/scala
  - export PATH=$PATH:/usr/lib/scala/bin ( we can add in .bash_profile)
  - scala -version
  
  
  .. figure:: ../_assets/user-guide/spark_standalone_scala_version.PNG
   :scale: 100%
   :alt: Standalone spark
   :align: center
   
  
Scala code runner version 2.10.1 -- Copyright 2002-2013, LAMP/EPFL

Install Apache Spark
--------------------

- Download Spark

  - wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz

- Extract, create a new directory under the /usr/local called spark and copy the extracted connect into it

  - tar xf spark-2.1.0-bin-hadoop2.7.tgz
  - mkdir /usr/local/spark
  - cp -r spark-2.1.0-bin-hadoop2.7/* /usr/local/spark

- Setup some Environment variables before you start spark-shell ( in .bash_profile)

  - export SPARK_EXAMPLES_JAR=/usr/local/spark/examples/jars/spark-examples_2.11-2.0.0.jar
  - PATH=$PATH:$HOME/bin:/usr/local/spark/bin

- Start you Scala Shell and run  Spark

  - Go to sparkflows home directory
  - cd /usr/local/spark/bin
  - ./spark-shell
  
  .. figure:: ../_assets/user-guide/spark_standalone_spark_version.PNG
   :scale: 100%
   :alt: Standalone spark
   :align: center
  
  
- You can start a standalone master server by executing:

  - ./sbin/start-master.sh  ( from spark home directory)

- Once started, the master will print out a spark://HOST:PORT URL
- You can also find this URL on the master’s web UI, 

  -  http://Master_host_ip:8080/ by default
  
  
  
  .. figure:: ../_assets/user-guide/spark_standalone_master_url.PNG
   :scale: 100%
   :alt: Standalone spark
   :align: center

Setup Spark Slave(Worker) Node
------------------------------

- Go to SPARK_HOME/conf/ directory.
- Edit the file spark-env.sh – Set SPARK_MASTER_HOST

  - If spark-env.sh is not present, spark-env.sh.template would be present. Make a copy of spark-env.sh.template with name spark-env.sh and add/edit the field SPARK_MASTER_HOST. Part of the file with SPARK_MASTER_HOST
  - cp ./conf/spark-env.sh.template ./conf/spark-env.sh
- Add a line in spark-env.sh :

  - SPARK_MASTER_HOST='MASTER_HOST_IP' 

Start spark as slave
-----------------------

- Goto SPARK_HOME/sbin and execute the following command.

  - ./start-slave.sh spark://localhost:7077 


Installing Fire
---------------

We install Fire on the master node.

- Download Fire Jar from website
  - wget https://s3.amazonaws.com/sparkflows-release/fire/rel-x.y.z/2/fire-x.y.z.tgz
  - tar xvf fire-x.y.z.tgz

- Go to below directory:

  - cd fire-x.y.z
  - Update the port of Fire-ui & Fire to 8090 & 8082 as default port 8080 & 8081 is used by standalone spark, we can chose any other also.

- Create database & run fire & fire-ui server

  - ./create-h2-db.sh
  - ./run-fire.sh start
  - ./run-fire-server.sh start


Configuring Fire
----------------

Below are the configuration for Fire to submit the jobs to the Spark Standalone Cluster.

- Once The server fire & fire-ui start
   - Login to http://Machine_ip:8090/#/dashboard
   - With password admin/admin.
   - Upload default applications.
   - Create a user ec2-user.
   - Login with ec2-user
  

Need to Make configurations in spark 
--------------------------------------
 
- Go to administration section and open Spark configuration there we need to add Below details in specific setup like below
   - spark.master: spark://Master_host_ip:7077
   - spark.deploy-mode: client
   - spark.sql-context: SQLContext
   - After above updates save the configurations.

  .. figure:: ../_assets/user-guide/spark_configuration_standalonespark.PNG
   :scale: 100%
   :alt: Standalone spark
   :align: center


Now goto application and try to run any workflows
-------------------------------------------------------

  .. figure:: ../_assets/user-guide/spark_standalone_workflow_executions.PNG
   :scale: 100%
   :alt: Standalone spark
   :align: center
