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

   To set up a job runtime role, first create a runtime role with a trust policy so that EMR Serverless can use the new role. Next, attach the required S3 access policy to that role. The following steps guide you through the process.


   #. Navigate to the IAM console at https://console.aws.amazon.com/iam/.

   #. In the left navigation pane, choose Roles.

   #. Choose Create role.

   #. For role type, choose Custom trust policy and paste the following trust policy. This allows jobs submitted to your Amazon EMR Serverless applications to access other AWS services on your behalf.

      ::

         {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
              "Service": "emr-serverless.amazonaws.com"
           },
              "Action": "sts:AssumeRole"
            }
          ]
         } 

   #. Choose Next to navigate to the Add permissions page, then choose Create policy.

   #. The Create policy page opens on a new tab. Paste the policy JSON below.

      ::

         {
          "Version": "2012-10-17",
         "Statement": [
         {
            "Sid": "ReadAccessForEMRSamples",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*.elasticmapreduce",
                "arn:aws:s3:::*.elasticmapreduce/*"
            ]
         },
         {
            "Sid": "FullAccessToOutputBucket",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::FIRE-EXAMPLE-BUCKET",
                "arn:aws:s3:::FIRE-EXAMPLE-BUCKET/*"
            ]
         },
         {
            "Sid": "GlueCreateAndReadDataCatalog",
            "Effect": "Allow",
            "Action": [
                "glue:GetDatabase",
                "glue:CreateDatabase",
                "glue:GetDataBases",
                "glue:CreateTable",
                "glue:GetTable",
                "glue:UpdateTable",
                "glue:DeleteTable",
                "glue:GetTables",
                "glue:GetPartition",
                "glue:GetPartitions",
                "glue:CreatePartition",
                "glue:BatchCreatePartition",
                "glue:GetUserDefinedFunctions"
            ],
            "Resource": ["*"]
            }
          ]
         }







