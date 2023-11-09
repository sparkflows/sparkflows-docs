Testing Environment
=========

It is a good idea to run the below steps to ensure that the environment is set up and working right.

Run the steps which are relevant for your environment.

Java Version Check
--------

Problem
+++++
Uncertain about Java version.

Solution
+++++
Run the below to verify: 
::

  java --version 


Python 3.7+ Setup Check
------
Problem
+++++
Unsure if Python 3.7+ is configured.

Solution
+++++
Run the below to verify: 
::
  python --version


Internet Access Check
---------------

Problem
++++++
Doubtful about machine's internet access.

Solution
+++++
Ensure that the machine has access to the internet.

Storage Availability Check
-----------

Problem
++++++
Unsure about available disk storage.

Solution
++++++
Use the below to check:
::
  du -sh * 

Memory and vCPU Verification
---------

Problem
+++++
Uncertain about memory and vCPU configuration.

Solution
++++++
Use the below to check:
::
  top

.. Note:: It is recommended to have at least 16GB of RAM and 4+vCPU's on the machine.

Fire-UI Process Check
--------

Problem
++++
Uncertain if the fire-ui process is running.

Solution
++++
Verify with the below:
::
  ps -ef | grep fire-ui

.. Note:: fire-ui is the main webserver process.

Fire Insights Ports Check
--------------

Problem
++++
Uncertain about the ports on which Fire Insights is running.

Solution
++++
Check the configured ports.

.. note:: By default Fire Insights listens on 2 ports : 8080 and 8443.

SparkPi Cluster Verification
----------

Problem
++++++

Unsure if Apache Spark cluster is set up correctly.

Solution
++++++

Run SparkPi using the below:
::

  spark-submit ...

Airflow Setup Check
--------

Problem
+++++
Uncertain if Airflow has been correctly set up.

Solution
+++++
Check if Airflow URL configured in Sparkflows is accessible from Sparkflow Machine.

Check if you are able to submit a DAG to Airflow and execute it.

DAG 1
......

SparkPi via spark-submit

DAG 2
.....

A spark program which reads data from S3 and writes the output to another S3 location


DAG 3
....

Use MACROS

Kerberos Configuration Check
-----------

Problem
+++++
Unsure if Kerberos is set up correctly.

Solution
++++++
                   
Check if the kerberos keytab is correct with below:

Kinit:
::

  kinit -kt keytab_file principal

Access HDFS with below:
::
  hdfs dfs -ls /tmp

Logs Examination for Errors
------------

Problem
+++++
Checking for errors in fire-ui and fire logs.

Solution
+++++
Check there are no major errors in the fire-ui log file with below:
::

  grep -i exception fireserver.log

Check there are no major errors in fire log file with below:
::
  grep -i exception fire.log


HIVE Setup Verification
---------
Problem
++++++
Uncertain about HIVE setup.

Solution
+++++
Log into HIVE via Beeline and confirm the ability to:

* List databases and tables.
* Execute queries on a specific table.

Livy Configuration Check
--------------

Problem
++++
Verifying Livy configuration.

Solution
+++++
Check if SparkPi submission to Livy works good using the below:
::
  curl

AWS S3 Access Check
----------

Problem
++++++
Confirming access to files on AWS S3.

Solution
+++++
Check if you are able to access files on S3.






