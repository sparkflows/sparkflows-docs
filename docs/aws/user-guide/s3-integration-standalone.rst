**S3 Integration**
==========

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
     
Step 3 : Configure AWS Access Key and Secret Key in Fire Insights Machine
-------

#. To configure your credentials, run *aws configure* on the machine which runs the Fire Insights.

Step 4 : Access S3 in Fire-UI
--------

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
          
