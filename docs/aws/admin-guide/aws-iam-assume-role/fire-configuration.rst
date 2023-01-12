Fire Configurations for Assuming Role
==============

Since the IAM Assume Role has been successfully set up, in the previous steps, so now we are ready to configure it in the Fire Insights. Follow the below steps to complete the configuration:

1. Login to Fire Insights application:

Once you login to Fire Insights application click on ``ADMINISTRATION`` tab located on top, it will take you to the configuration page.

.. figure:: ../../../_assets/aws/glue/config.PNG
   :alt: aws
   :width: 60%

2. Update the below parameters as per the AWS configurations:

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

.. figure:: ../../../_assets/aws/iam-assume-role/aws_configurations.PNG
   :alt: aws
   :width: 60%


3. Create/Update Group in Fire Insights:

Copy the ``ARN`` set up for assume role in AWS IAM Role and update in ``AWS ROLE NAME`` text field.

::

    arn:aws:iam::<account-1-id>:role/assume-role-bucket1
    
    
.. figure:: ../../../_assets/aws/iam-assume-role/assume_role_arn.PNG
   :alt: aws
   :width: 60%

Once the Group is attached to any User in Fire Insights application, save the Configurations.

4. Open DATA/AWS S3, you will see the S3 Bucket listed:

Now, you can use it for creating workflow in the Node.

.. figure:: ../../../_assets/aws/iam-assume-role/aws_s3_lists.PNG
   :alt: aws
   :width: 60%

.. note:: Currently users can access the S3 resources by assumming the role.
When user belongs to multiple user groups and each group is attached with different roles, then role from the first group will be assumed during the S3 access.
