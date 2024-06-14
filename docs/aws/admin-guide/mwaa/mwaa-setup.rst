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

Step two: Configure advanced settings
----------------

To configure advanced settings
=========

#. On the Configure advanced settings page, under Networking:

   #. Choose your Amazon VPC.

      This step populates two of the private subnets in your Amazon VPC.

#. Under Web server access, select your preferred Apache Airflow access mode:

   #. Private network. This limits access of the Apache Airflow UI to users within your Amazon VPC that have been granted access to the IAM policy for your environment. You need permission to create Amazon VPC endpoints for this step.

      .. note:: Choose the Private network option if your Apache Airflow UI is only accessed within a corporate network, and you do not require access to public repositories for web server requirements installation. If you choose this access mode option, you need to create a mechanism to access your Apache Airflow Web server in your Amazon VPC. For more information, see Accessing the VPC endpoint for your Apache Airflow Web server (private network access).

   #. Public network. This allows the Apache Airflow UI to be accessed over the Internet by users granted access to the IAM policy for your environment.

#. Under Security group(s), choose the security group used to secure your Amazon VPC:

   #. By default, Amazon MWAA creates a security group in your Amazon VPC with specific inbound and outbound rules in 
      ``Create new security group``.

   #. Optional. Deselect the check box in Create new security group to select up to 5 security groups.


      .. note:: An existing Amazon VPC security group must be configured with specific inbound and outbound rules to allow network traffic. To learn more, see Security in your VPC on Amazon MWAA.

#. Under Environment class, choose an environment class.

   We recommend choosing the smallest size necessary to support your workload. You can change the environment class at any time.

#. For Maximum worker count, specify the maximum number of Apache Airflow workers to run in the environment.

   For more information, see Example high performance use case.

#. Specify the Maximum web server count and Minimum web server count to configure how Amazon MWAA scales the Apache Airflow web servers in your environment.

   For more information about web server automatic scaling, see Configuring Amazon MWAA web server automatic scaling.

#. Under Encryption, choose a data encryption option:

   #. By default, Amazon MWAA uses an AWS owned key to encrypt your data.

   #. Optional. Choose Customize encryption settings (advanced) to choose a different AWS KMS key. If you choose to specify a Customer managed key in this step, you must specify an AWS KMS key ID or ARN. AWS KMS aliases and multi-region keys are not supported by Amazon MWAA. If you specified an Amazon S3 key for server-side encryption on your Amazon S3 bucket, you must specify the same key for your Amazon MWAA environment.


   .. note:: You must have permissions to the key to select it on the Amazon MWAA console. You must also grant permissions for Amazon MWAA to use the key by attaching the policy described in Attach key policy.

#. Recommended. Under Monitoring, choose one or more log categories for Airflow logging configuration to send Apache Airflow logs to CloudWatch Logs:

   #. Airflow task logs. Choose the type of Apache Airflow task logs to send to CloudWatch Logs in Log level.

   #. Airflow web server logs. Choose the type of Apache Airflow web server logs to send to CloudWatch Logs in Log level.

   #. Airflow scheduler logs. Choose the type of Apache Airflow scheduler logs to send to CloudWatch Logs in Log level.

   #. Airflow worker logs. Choose the type of Apache Airflow worker logs to send to CloudWatch Logs in Log level.

   #. Airflow DAG processing logs. Choose the type of Apache Airflow DAG processing logs to send to CloudWatch Logs in Log level.

#. Optional. For Airflow configuration options, choose Add custom configuration option.

    You can choose from the suggested dropdown list of Apache Airflow configuration options for your Apache Airflow version, or specify custom configuration options. For example, core.default_task_retries : 3.

#. Optional. Under Tags, choose Add new tag to associate tags to your environment. For example, Environment: Staging.

#. Under Permissions, choose an execution role:

   #. By default, Amazon MWAA creates an execution role in Create a new role. You must have permission to create IAM roles to use this option.

   #. Optional. Choose Enter role ARN to enter the Amazon Resource Name (ARN) of an existing execution role.

#. Choose Next.




