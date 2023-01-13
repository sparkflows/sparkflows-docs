S3 Integration
==========

Fire Insights allows you to access your files on S3. This document describes the S3 integration of Fire.

We recommend to control access to S3 with the use of IAM Roles. 

- Run Fire Insights on an EC2 machine with an appropriate S3 IAM Role.
- Run the EMR cluster with the appropriate S3 IAM Role.

If you run Fire Insights on an independent machine, you can also use ``aws configure`` to set the AWS Access Key and Secret Access Key on the machine.

AWS CLI S3 Reference: https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html

Install AWS CLI
---------------
Please find the user guide for installation at the following link:

- http://docs.aws.amazon.com/cli/latest/userguide/installing.html
                   :code:`pip install awscli --upgrade --user`


Configure AWS Access Key and Password
-----------------------------------

Run ``aws configure`` to configure your credentials on the machine which runs the Fire Insights.

   
Access S3 in Fire-UI
---------------------

In Fire Insights, you can browse S3 under the menu: Data Browsers/AWS S3.

.. figure:: ../../_assets/tutorials/awscli/AWS3.PNG
   :alt: s3
   :align: center
   
- Click on AWS S3 to view the files on S3.

.. figure:: ../../_assets/tutorials/awscli/AWS4.PNG
   :alt: s3
   :align: center
   

Protect Data Using Server Side Encryption
--------------

Data encryption settings on S3 buckets are available at: https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html

   
   
REFERENCE : Create Access Key & Secret Key
--------------

1. You need to create a user with programmatic access by following the steps at: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html

 

2. Now, you need to create an IAM policy that defines the access limit in your AWS account.  It's important to grant only restricted access to this user within your account. Please refer the documentation availble at the below link to find details on creation of IAM Policies: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html

 

3. Lastly, you need to create an access key and secret key for this user. For further information follow the steps provided at the below link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey

.. note:: It's important to regularly rotate your access and secret keys. Please refer the document available at the below link for further information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console

