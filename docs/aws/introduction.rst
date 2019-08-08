Introduction
============

Fire Insights is the flagship product from Sparkflows. It is seamlessly integrated with AWS. With Fire Insights you can perform self-serve data processing, analytics and machine learning on AWS.

Fire Insights integrates with EMR, S3, Redshift, SageMaker, HIVE and Kinesis.

Fire Insights comes with a number of components including:

- **Workflow Editor** : To create workflows for data processing, analytics and machine learning.
- **260+ Processors** : These include reading data from various stores, data processing, machine learning and visualizations.
- **Execution Engine** : For executing the workflow on EMR
- **Scheduler** : For scheduling running the workflows at certain time intervals

Sparkflows Fire Insights can be deployed to an existing Amazon EMR cluster, or you can use one of our CloudFormation templates to set up a new Amazon EMR Cluster. If you use our provided CloudFormation templates we'll create an EMR cluster for you or even an EMR cluster and MySQL instance running in RDS, depending on which template you choose.


Pre-requisites and Requirements
--------------------------------

Fire Insights needs EMR for running the workflows. So, you have to have a running EMR cluster for using Fire Insights.

You also need ssh access to one of the machines of the EMR cluster for installing Fire Insights. This machine is typically an edge node or a master node of the EMR cluster.

* Getting started with EMR - https://aws.amazon.com/emr/getting-started/
* Opening SSH access to the EMR master node - https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html


Architecture
------------

Fire Insights runs on the edge node or one of the master nodes of the EMR cluster. It submits the processing jobs onto the cluster. By default it runs on port 8080. This port needs to be changes to some port which is open on the machine. Lets assume port 8085.

When the jobs are fired onto the EMR cluster, it can read/write data from S3/HDFS/Redshift/Kinesis. It can also fire Machine Learning modeling jobs to SageMaker.

.. figure:: ../_assets/aws/aws-architecture-1.png
   :alt: Architecture
   :align: center
