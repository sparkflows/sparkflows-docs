**S3 Integration**
==========

Fire Insights allows users to access files on S3. The steps involved are: 

#. Fulfill AWS Account Requirements
   
   * Create IAM User in AWS Account
   * Create IAM Policy in AWS Account
   * Create AWS Access Key and Secret Key in AWS Account

#. Fulfill Fire UI Requirements
   
   * Install AWS CLI in Fire UI
   * Configure AWS Access Key and Secret Key in Fire UI
   * Access S3 in Fire UI

This document describes the steps involved in S3 integration of Fire.


**Step 1 : Fulfill AWS Account Requirements**
---------

#. **Create IAM User in AWS Account**
   
   To create a user with programmatic access follow the steps given in `AWS User Guide.<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>`_


#. **Create IAM Policy in AWS Account**

   To create IAM policy that defines the access limit to your AWS account follow the steps given in `AWS User Guide.<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html>`_

   Note: It is recommended to grant only restricted access to the user within your account.
         
           To control the access to S3 it is always recommended to use IAM Roles:
        
            - Run Fire Insights on an EC2 machine with an appropriate S3 IAM Role.
            - Run the EMR cluster with the appropriate S3 IAM Role.

#. **Create AWS Access Key and Secret Key in AWS Account**

   To create access key and secret key for the above-created user, follow the step given in `AWS User Guide.<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey>`_
   
   
**Step 2 : Fulfill Fire UI Requirements**
--------

#. **Install AWS CLI in Fire UI**
   
   To install the AWS CLI in Fire UI run the below command:
   
    :code:`pip install awscli --upgrade --user`
 
   For more details on installation refer the `installation guide.<http://docs.aws.amazon.com/cli/latest/userguide/installing.html>`_
     
#. **Configure AWS Access Key and Secret Key in Fire UI** 

   To configure your credentials, run *aws configure* on the machine which runs the Fire Insights.
   
   If you run Fire Insights on an independent machine, the also you can use the *aws configure* to set the AWS Access Key and Secret Access Key on the machine.

   For more details refer the `AWS CLI S3 guide.<https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html>`_

#. **Access S3 in Fire-UI**

   * From Fire Inights Dashboard, place the cursor over **DATA BROWSERS** to view the drop-down list.

     .. figure:: ../../_assets/tutorials/awscli/aws_s3.PNG
        :alt: S3 integration
        :width: 70%
   
  * From the list, click **AWS S3** to view the files on S3.

     .. figure:: ../../_assets/tutorials/awscli/aws_s3_list.PNG
        :alt: S3 integration
        :width: 70%
   

**Protect Data Using Server Side Encryption**
--------------

`Details on data encryption settings on S3 buckets are available here.<https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`_

   
.. note:: It is recommended to regularly rotate your access and secret keys. 
          
          `For more details refer the documentation available here.<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console>`_
          
