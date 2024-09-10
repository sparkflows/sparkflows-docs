Pre-requisites
=======

This document outlines the key infrastructure prerequisites for setting up and configuring an Amazon MWAA environment with Fire Insights.

The required prerequisites are as follows:

#. An AWS account with permissions to use Amazon MWAA.
#. IAM permissions to create IAM roles.
#. Access to an S3 bucket.
#. Python dependency installation.
#. If opting for Private network access mode for the Apache Airflow web server, which restricts access to within your Amazon VPC, you will need IAM permissions to create Amazon VPC endpoints.

1. An AWS Account with permissions to use Amazon MWAA
-------------------------------------------------

You will need an AWS account with the appropriate permissions to create and configure Amazon Managed Workflows for Apache Airflow (MWAA). These permissions typically include full access to MWAA, allowing you to create, update, and manage MWAA environments. 

Ensure that your account has sufficient privileges to access and modify necessary AWS services like S3 and IAM required for MWAA.

2. IAM Permissions to Create IAM Roles
--------------------------------------------------------------------------

Ensure that you have the necessary permissions in AWS Identity and Access Management (IAM) to create IAM roles. These roles will allow Amazon MWAA to access other AWS services such as Amazon S3, AWS Lambda, Amazon CloudWatch, and others.

3. S3 Bucket Access
----------------
Amazon MWAA requires access to Amazon S3 buckets to store Apache Airflow DAGs, logs, plugins, and environment variables. You need permissions to create and manage S3 buckets, as well as to upload files (such as DAGs and dependencies) to the bucket. Ensure that the appropriate access control policies are set for both read and write access as required.

4. Python Dependency Installation
------------------------------
For Apache Airflow to function correctly within Amazon MWAA, you will need to install any required Python dependencies. These dependencies can be specified in a requirements.txt file, which is uploaded to the S3 bucket associated with your MWAA environment.

5. Private Network Access Mode for the Apache Airflow Web Server (Optional)
------------------------------------------------------------------------
If you choose to limit access to the Apache Airflow web server by configuring it to be accessed only within your Amazon Virtual Private Cloud (VPC), additional IAM permissions may be required. Specifically, you will need the necessary IAM permissions to create and manage VPC endpoints, which enable private network access to the web server from within your VPC. Ensure that you can create and configure these endpoints before proceeding with this option. For more information, you can go through `AWS documentation <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_.

Installing / Managing Python Packages
---------------------------

The following Apache Airflow versions are supported on Amazon Managed Workflows for Apache Airflow (MWAA):

#. Starting with Apache Airflow v2.2.2, Amazon MWAA supports installing Python requirements, provider packages, and custom plugins directly on the Apache Airflow web server.

#. Starting with Apache Airflow v2.7.2, your requirements file must include a --constraint statement. If you don't provide a constraint, Amazon MWAA will specify one for you to ensure that the packages listed in your requirements are compatible with the version of Apache Airflow you're using.

#. Fire Insights currently supports Airflow v2.8.1 for integration, as it includes the required Airflow API features.

For more information on setting up constraints in your requirements file, see `Installing Python dependencies <https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt>`_.



