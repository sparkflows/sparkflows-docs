Architecture diagram
=================

Fire Insights can be configured to AWS Glue cluster with below architecture diagram.

.. figure:: ../../_assets/aws/glue/architecture.png
   :alt: aws
   :width: 60%
   


1. Fire Insights is installed on an EC2 instance.
2. Users create Analytics and Data Prep workflows via a web interface.
3. Fire Insights submits the job onto AWS Glue throught Rest API.
4. It reads in data from AWS S3.
5. The jobs running on AWS Glue also send back results to Sparkflows via HTTP
6. IAM Roles is used to access AWS Glue, S3 etc.

