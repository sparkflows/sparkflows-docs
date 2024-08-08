Amazon EMR Serverless
===============

This document provides comprehensive guide for setting up Amazon EMR Serverless, ensuring a smooth integration process with Fire Insights. 

#. Grant permissions to use EMR Serverless

   To use EMR Serverless, you need a user or IAM role with an attached policy that grants permissions for EMR Serverless. To create a user and attach the appropriate policy to that user.

   `Click here <https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/setting-up.html#setting-up-iam>`_ follow the instructions in Grant permissions.

#. Prepare storage for EMR Serverless

   you'll use an S3 bucket to store output files and logs from the sample Spark or Hive workload that you'll run using an EMR Serverless application. To create a bucket, follow the instructions in Creating a bucket in the Amazon Simple Storage Service Console. Replace any further reference to FIRE-EXAMPLE-BUCKET with the name of the newly created bucket. 

   `Click here <https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html>`_ follow the instructions for Creating a bucket.

#. Create a job runtime role

   Job runs in EMR Serverless use a runtime role that provides granular permissions to specific AWS services and resources at runtime. In this tutorial, a public S3 bucket hosts the data and scripts. The bucket FIRE-EXAMPLE-BUCKET stores the output.


