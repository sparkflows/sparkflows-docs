Introduction
============

Fire Insights is seamlessly integrated with AWS. With Fire Insights you can perform self-serve data processing, analytics and machine learning on AWS.

Fire Insights integrates with EMR, S3, Redshift, SageMaker, HIVE and Kinesis.

Fire Insights comes with a number of components including:

- Workflow Editor : To create workflows for data processing, analytics and machine learning.
- Execution Engine : For executing the workflow on EMR
- Scheduler : For scheduling running the workflows at certain time intervals


Pre-requisites and Requirements
--------------------------------

Fire Insights needs EMR for running the workflows. So, you have to have a running EMR cluster for using Fire Insights.

You also need ssh access to one of the machines of the EMR cluster for installing Fire Insights. This machine is typically an edge node or a master node of the EMR cluster.


Architecture
------------

Fire Insights runs on the edge node or one of the master nodes of the EMR cluster. It submits the processing jobs onto the cluster. By default it runs on port 8080. This port needs to be changes to some port which is open on the machine. Lets assume port 8085.

When the jobs are fired onto the EMR cluster, it can read/write data from S3/HDFS/Redshift/Kinesis. It can also fire Machine Learning modeling jobs to SageMaker.

.. figure:: ../_assets/aws/aws-architecture-1.png
   :alt: Architecture
   :align: center
