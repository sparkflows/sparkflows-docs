Amazon EMR Serverless Setup
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

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_1.png
         :alt: emrserverless
         :width: 60%


   #. Choose Create role.

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_1.png
         :alt: emrserverless
         :width: 60%


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

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_2.png
         :alt: emrserverless
         :width: 60%


   #. Choose Next to navigate to the Add permissions page, then choose Create policy.

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_3.png
         :alt: emrserverless
         :width: 60%


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

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_4.png
         :alt: emrserverless
         :width: 60%

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_5.png
         :alt: emrserverless
         :width: 60%


      .. note:: Replace ``FIRE-EXAMPLE-BUCKET`` in the policy below with the actual bucket name created in Prepare storage for EMR Serverless. This is a basic policy for S3 access. For more job runtime role examples, see Job runtime roles for Amazon EMR Serverless.

   #. On the Review policy page, enter a name for your policy, such as EMRServerlessS3AndGlueAccessPolicy.

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_6.png
         :alt: emrserverless
         :width: 60%


   #. Refresh the Attach permissions policy page, and choose EMRServerlessS3AndGlueAccessPolicy.

   #. In the Name, review, and create page, for Role name, enter a name for your role, for example, emr_serverless_role. To create this IAM role, choose Create role.  

      .. figure:: ../../../_assets/aws/emrserverless/emrserverless_7.png
         :alt: emrserverless
         :width: 60%

#. Enabled job runtime role to access Fire Insight application

   you can attach new policy with access to Network

   ::

      {
       "Version": "2012-10-17",
       "Statement": [
        {
            "Sid": "EC2PolicyStatement",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:DescribeDhcpOptions",
                "ec2:DescribeRouteTables"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchPolicyStatement",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": [
                        "AWS/EMRServerless",
                        "AWS/Usage"
                    ]
                }
            }
        }
     ]
     }


   `Click here <https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-user-access-policies.html>`_ follow the instructions on Network policy.

#. Create private subnet and attach security group with it

   Inorder to submit Job from Fire Insights application, you need to create private subnet in emrserverless region and attach security group with it, so Fire Insights application deployed on ecs or ec2 can have the access of that.


   `Click here <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html>`_ follow the instructions for creating private subnet.


   .. note:: Make sure to copy these two ie ``subnet Id & security group Id``, As it is being used while Configuring EMR Serverless connection in Fire Insights.



