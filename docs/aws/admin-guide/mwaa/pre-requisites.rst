Pre-requisites
=======

This document outlines the essential infrastructure pre-requisites needed to setup and configure Amazon MWAA environment with Fire Insights.

#. AWS account with permissions to use Amazon MWAA
#. permission in AWS Identity and Access Management (IAM) to create IAM roles
#. S3 Bucket access
#. Python dependency Installation
#. If you choose the Private network access mode for the Apache Airflow web server, which limits Apache Airflow access within your Amazon VPC, you'll need permission in IAM to create Amazon VPC endpoints.

.. Note:: The following Apache Airflow versions are supported on Amazon Managed Workflows for Apache Airflow.


#. Beginning with Apache Airflow v2.2.2, Amazon MWAA supports installing Python requirements, provider packages, and custom plugins directly on the Apache Airflow web server.

#. Beginning with Apache Airflow v2.7.2, your requirements file must include a --constraint statement. If you do not provide a constraint, Amazon MWAA will specify one for you to ensure the packages listed in your requirements are compatible with the version of Apache Airflow you are using.

For more information on setting up constraints in your requirements file, see Installing Python dependencies.

