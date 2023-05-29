Introduction
============

Fire Insights is the flagship product from Sparkflows. It is seamlessly integrated with AWS. With Fire Insights you can perform self-serve data processing, analytics, and machine learning on AWS.

Fire Insights integrates with EMR, S3, Redshift, SageMaker, HIVE, and Kinesis.

Fire Insights comes with several components including:

- **Workflow Editor** : To create workflows for data processing, analytics, and machine learning.
- **400+ Processors** : These include reading data from various stores, data processing, machine learning, and visualizations.
- **Execution Engine**: To execute the workflow on EMR.
- **Scheduler**       : To schedule running of the workflows at specified time intervals.

Sparkflows Fire Insights can be deployed either to an existing Amazon EMR cluster, or you can use one of the Sparkflows' CloudFormation templates to set up a new Amazon EMR Cluster. If you prefer to use the CloudFormation templates provided by the Sparkflows, an EMR cluster can be created with/without MySQL running in RDS, depending on which template you choose.


Pre-requisites and Requirements
--------------------------------

Fire Insights needs an EMR cluster to run the workflows. You also need SSH access to one of the machines of the EMR cluster for installing the Fire Insights. 

* Getting started with EMR - https://aws.amazon.com/emr/getting-started/
* Opening SSH access to the EMR master node - https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html


Architecture
------------

Fire Insights runs either on the edge node or one of the master nodes of the EMR cluster and submits the jobs onto the cluster. By default, it runs on port 8080. However, this port needs to be changed to another available port as port 8080 (port 8085 can be used) in already in use.

When the jobs are fired onto the EMR cluster, it can read/write data from S3/HDFS/Redshift/Kinesis. It can also trigger Machine Learning jobs to SageMaker.

.. figure:: ../_assets/aws/aws-architecture-1.png
   :alt: Architecture
   :align: center
   :width: 70%
