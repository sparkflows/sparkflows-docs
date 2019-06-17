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

