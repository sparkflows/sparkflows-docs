Fire Configurations for Assuming Role
==============

Since the IAM AssumeRole was successfully set up in the previous steps, we are now ready to configure it in Sparkflows. Follow the steps below to complete the configuration.

Step 1 : Login to Sparkflows
----------------------
#. Go to the Sparkflows login page.

#. Enter your **credentials**, then click **Login**. You will be directed to the **Fire Dashboard**, as shown below.

   .. figure:: ../../../_assets/aws/glue/Login.png
      :alt: metrics
      :width: 60%

Step 2 : Go to Configurations Page
-------------------------
#. From the dashboard, click the **ADMINISTRATION** tab located in the top menu bar.
#. From the Administration page, click the **Configurations** to reach the configurations page.

   .. figure:: ../../../_assets/aws/glue/administration_sparkflows.png
      :alt: aws
      :width: 60%

Step 3 : Update Parameters
---------------
#. Update the following parameters according to the AWS configuration:
 
   **For AWS tab**

   .. list-table:: 
      :widths: 10 20 30
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Enable AWS
        - Enable AWS for accessing the AWS S3 buckets
        - true
      * - Enable AssumeRole
        - Enable AWS Assume Role to access AWS Resources
        - true
      * - Home Dir
        - Home Directory Path on S3 
        - s3a://bucketName/sampleData 
      * - AWS Region
        - As per resource in the region
        - Input the aws region

   .. figure:: ../../../_assets/aws/iam-assume-role/assume_role_enabled.PNG
       :alt: aws
       :width: 60%

Step 4 : Create/Update Group in Sparkflows
----------------------------

#. Navigate to **Administration -> Group List**.

   .. figure:: ../../../_assets/aws/iam-assume-role/group_sparkflows.png
      :alt: aws
      :width: 60%

#. Copy the **ARN** set up for assume role in AWS IAM Role and Update in **AWS ROLE NAME** text field.

   ::

       arn:aws:iam::<account-1-id>:role/assume-role-bucket1
    
    
   .. figure:: ../../../_assets/aws/iam-assume-role/assume_role_group.PNG
      :alt: aws
      :width: 60%

#. Once the Group is attached to any User in Sparkflows, **Save** the Configurations.

Step 5 : Access S3 Bucket
--------------
#. Navigate to **DATA > AWS S3**, you will see the S3 Buckets lists,  as shown below. You can now use it to create a workflow in the Node.

   .. figure:: ../../../_assets/aws/iam-assume-role/assume_role_s3.PNG
      :alt: aws
      :width: 60%

.. note:: Currently, users can access S3 resources by assuming the role. When a user belongs to multiple groups and each group is associated with a different role, the role from the first group will be assumed during the S3 access.
