AWS MWAA
=====

This document provides comprehensive guide for setting up AWS MWAA Environment, ensuring a smooth integration process. 

Below are  the steps required to Create an Amazon MWAA environment.

Step one: Specify details
----

To specify details for the environment
====
  
#. Open the Amazon MWAA console.

#. Use the AWS Region selector to select your region.

#. Choose Create environment.

   #. On the Specify details page, under Environment details:

   #. Type a unique name for your environment in Name.

#. Choose the Apache Airflow version in Airflow version.


   .. note:: If no value is specified, defaults to the latest Airflow version. The latest version available is Apache Airflow v2.8.1.

#. Under DAG code in Amazon S3 specify the following:

   #. S3 Bucket. Choose Browse S3 and select your Amazon S3 bucket, or enter the Amazon S3 URI.

   #. DAGs folder. Choose Browse S3 and select the dags folder in your Amazon S3 bucket, or enter the Amazon S3 URI.

   #. Plugins file - optional. Choose Browse S3 and select the plugins.zip file on your Amazon S3 bucket, or enter the Amazon S3 URI.

   #. Requirements file - optional. Choose Browse S3 and select the requirements.txt file on your Amazon S3 bucket, or enter the Amazon S3 URI.

   #. Startup script file - optional, Choose Browse S3 and select the script file on your Amazon S3 bucket, or enter the Amazon S3 URI.

#. Choose Next.



