Architecture diagram
=================

Fire Insights can be configured to AWS Glue cluster with below architecture diagram.

.. figure:: ../../_assets/aws/glue/architecture.png
   :alt: aws
   :width: 60%
   
   
Fire Insights is installed on an EC2 instance
Users create Analytics and Data Prep workflows via a web interface
Fire Insights submits the job onto AWS Glue throught Rest API.
It reads in data from AWS S3.
The jobs running on AWS Glue also send back results to Sparkflows via HTTP
IAM Roles is used to access AWS Glue, S3 etc.

