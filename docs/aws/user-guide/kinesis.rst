Integration with Kinesis
==============================

This documentation provides a comprehensive guide on integrating Fire Insights with Kinesis, enabling seamless data processing and analysis. 

Fire Insights leverages the Apache Spark Structured Streaming Connector from Qubole. 

For detailed information, refer to the `qubole-kinesis documentation <https://github.com/qubole/kinesis-sql>`_ available on GitHub.

To integrate Fire with Kinesis, follow the steps outlined below:

Step 1 : Install AWS-CLI
----------

To proceed with the integration, you must have AWS-CLI installed.

For detailed information on installation steps refer to the `AWS Installation Guide. <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html>`_

Step 2 : Create Access Key and Secret Key
-----------------

#. Create user with programmatic access. Refer to the steps given in the `AWS User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>`_
#. Create an access key and secret key for the user to establish a connection. Refer to the steps given in the `AWS User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey>`_

   **Note: Regularly rotate your access and secret keys for security purposes.** 
   
   For more information on rotation, refer to the `AWS Rotating Access Keys Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console>`_

Step 3 : Configure AWS-CLI
------------
 
Configure AWS-CLI to establish the necessary credentials. Ensure that you set the appropriate region: ::

 aws configure region: us-east-1 aws_access_key_id = accesskeyid aws_secret_access_key = awssecretaccesskey

For detailed configuration instructions, refer to the `AWS-CLI Guide. <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html>`_

Step 4 : Create an AWS Kinesis Stream
---------

Create an AWS Kinesis Stream by executing the following command: ::

 aws kinesis create-stream --stream-name sparkflows_kinesis_test --shard-count 1

Step 5 : Send Messages to AWS Kinesis from AWS CLI
----------

To send messages to Kinesis, utilize the following command: ::

 aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

Step 6 : Update EMR_EC2_Default_Role
---------

* Update the EMR_EC2_DefaultRole with the **AmazonKinesisFullAccess Policy**. 

  This action grants the EMR Cluster full access to Kinesis.

* Alternatively, you can create an **IAM policy** specifically to access Amazon Kinesis. 

  Ensure that you grant restricted access to the user within your AWS account. 
   
  For more information refer to the `AWS-IAM User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html>`_

Step 7 : Create EMR Cluster with the Above Role
----------

Create an EMR Cluster using the role configured in step 6, which grants full access to Amazon Kinesis.

Step 8 : Push Data to Kinesis
-------------

AWS provides a Kinesis Data Generator that allows you to configure and push random data in the desired format to Kinesis. 

For more information on this, refer to the documentation related to `Amazon Kinesis Data Generator. <https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html>`_

  .. figure:: ../../_assets/aws/kinesis-data-generator-1.png
     :alt: Kinesis Data Generator
     :width: 65%
   
   
  .. figure:: ../../_assets/aws/kinesis-data-generator-2.png
     :alt: Kinesis Data Generator
     :width: 65%
   
Step 9 : Kinesis Workflow in Fire
----------

Fire enables the creation of workflows that can seamlessly read data from Kinesis, process it, and save the results as required.












