Amazon S3 Integration
==================

Fire Insights can be configured to read data from S3 via one of the two approaches below:

* Via Access Key and Secret Key
* Via IAM roles

The details of each of the above is listed out below.

Amazon S3 Integration via Access Key and Secret Key
+++++++++++

Fire Insights allows users to access files on S3. The steps involved are: 

#. Fulfill AWS Account Requirements
   
   * Create IAM User in AWS Account
   * Create IAM Policy in AWS Account
   * Create AWS Access Key and Secret Key in AWS Account
   
#. Install AWS CLI in Fire Insights Machine
#. Configure AWS Access Key and Secret Key in Fire Insights Machine
#. Access S3 in Fire UI
#. Protect Data Using Server Side Encryption

This document explains in detail the steps involved in S3 integration of Fire.

.. note:: It is important to note that the VM on which you want S3 integration should be the same on which Fire is installed.

Step 1 : Fulfill AWS Account Requirements
---------

#. **Create IAM User in AWS Account**
   
   To create a user with programmatic access follow the steps given in `AWS User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>`_


#. **Create IAM Policy in AWS Account**

   To create IAM policy that defines the access limit to your AWS account follow the steps given in `AWS User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html>`_

   Note: 
  
   It is recommended to grant only restricted access to the user within your account.
   
   To control the access to S3 it is recommended that you use IAM Roles:
       
     - Run Fire Insights on an EC2 machine with an appropriate S3 IAM Role.
     - Run the EMR cluster with the appropriate S3 IAM Role.
 
#. **Create AWS Access Key and Secret Key in AWS Account**

   To create access key and secret key for the above-created user, follow the step given in `AWS User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey>`_
   
   
Step 2 : Install AWS CLI in Fire Insights Machine
--------

#. To install the AWS CLI in Fire UI run the below command:
   
    :code:`pip install awscli --upgrade --user`
 
   For more details on installation refer the `installation guide. <http://docs.aws.amazon.com/cli/latest/userguide/installing.html>`_
     
Step 3 : Configure Amazon Access Key and Secret Key in Fire Insights Machine
-------

#. To configure your credentials, run *aws configure* on the machine which runs the Fire Insights.

Step 4 : Access S3 in Fire-UI
--------

#. On Fire Inights Dashboard page, place the cursor over **ADMINISTRATION/Configurations** and select AWS tab with below needed configurations.

     .. figure:: ../../_assets/tutorials/awscli/aws_config.PNG
        :alt: S3 integration
        :width: 70%

#. On Fire Inights Dashboard page, place the cursor over **DATA** to view the drop-down list.

     .. figure:: ../../_assets/tutorials/awscli/aws_s3.PNG
        :alt: S3 integration
        :width: 70%

#. In the list, click **AWS S3** to view the files on S3.

     .. figure:: ../../_assets/tutorials/awscli/aws_s3_list.PNG
        :alt: S3 integration
        :width: 70%
   

Step 5 : Protect Data Using Server Side Encryption
--------------

#. It is recommended to protect your data using server side encryption settings.

   For detailed steps read documentation on `data encryption settings on S3 buckets. <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`_

   
.. note:: It is recommended to regularly rotate your access and secret keys. For more details refer the `AWS documentation. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console>`_ 
          

Amazon S3 Integration via IAM Role
++++++++++++++

Fire Insights enables you to configure with S3 running on EC2 instance using IAM role.

Following steps are required to create a role for S3 bucket access and attach the role to EC2 instance on which Fire is running:

Step 1 : Create a Role
-------------

Login to AWS Console which has sufficient privilege to create a role with name **assume-role-bucket1**.

Step 2 : Create Inline Policy
------------

Create an **inline policy** which has access to S3 policy which in turn has access to the different buckets e.g. **assume-role-bucket1** & **assume-role-bucket2** and then attach it to the role.

::

    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:GetBucketLocation",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:List*",
                "s3:GetObject*",
                "s3:PutObject*",
                "s3:GetBucketAcl"
            ],
            "Resource": [
                "arn:aws:s3:::assume-role-bucket1",
                "arn:aws:s3:::assume-role-bucket1/*",
                "arn:aws:s3:::assume-role-bucket2",
                "arn:aws:s3:::assume-role-bucket2/*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:DeleteBucketPolicy",
                "s3:DeleteBucketWebsite",
                "s3:PutAccelerateConfiguration",
                "s3:PutBucketAcl",
                "s3:PutBucketCORS",
                "s3:PutBucketLogging",
                "s3:PutBucketPolicy",
                "s3:PutBucketRequestPayment",
                "s3:PutBucketTagging",
                "s3:PutBucketVersioning",
                "s3:PutBucketWebsite",
                "s3:PutReplicationConfiguration"
            ],
            "Resource": "*",
            "Effect": "Deny"
        }
    ]
  }


Step 3 : Attach Policy to EC2 Instance
------------

Now, the policy **assume_role_bucket1** needs to be attached to the EC2 instance where Fire is running.

#. In order to attach the above role to EC2 instance, you need to Login to AWS Console and go to **EC2 Dashboard** and select the EC2 instance where Fire is running and choose **Security**, from **Actions** dropdown and click on **Modify IAM role**.

   .. figure:: ../../_assets/aws/aws_s3_ec2/role_added.PNG
      :alt: aws
      :width: 60%

#. Select **IAM role** which was created in **step 1** and click on **Update IAM role**.

   .. figure:: ../../_assets/aws/aws_s3_ec2/role_selected.PNG
      :alt: aws
      :width: 60%

   Once the above steps get successfully completed, you need to configure S3 in Fire.

Step 4 : Set Fire Configurations for S3
-----------------------

Since the Role has been successfully set up, in the previous steps, so now we are ready to configure it in the Fire Insights. 

Follow the steps given below to complete the configuration:

1. Login to Fire Insights application:

   Once you login to Fire Insights application, click on **ADMINISTRATION** tab located on top, it will take you to the configuration page.

   .. figure:: ../../_assets/aws/glue/config.PNG
      :alt: aws
      :width: 60%

2. Update the below given parameters as per the AWS configurations:

   .. list-table:: 
      :widths: 10 20 30
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Enable AWS
        - Enable AWS for accessing the Amazon S3 buckets
        - true
      * - Enable AssumeRole
        - Enable AWS Assume Role to access AWS Resources
        - false
      * - Home Dir
        - Home Directory Path on S3 
        - s3a://bucketName/sampleData 
      * - AWS Region
        - As per resource in the region
        - Input the AWS region

   .. figure:: ../../_assets/aws/iam-assume-role/aws_configurations.PNG
      :alt: aws
      :width: 60%

3. Now, save the configurations and click on **DATA/AWS S3**.

   If previous steps were successful, it will point to the S3 location configured.

   .. figure:: ../../_assets/aws/aws_s3_ec2/s3_access.PNG
      :alt: aws
      :width: 60%

   Now, you can use the data available in S3 from workflow editor, using different nodes available.


