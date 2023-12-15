AWS Glue & EC2 Network Connection
==================

Fire Insights EC2 instance can communicate with AWS Glue using a Network connection.

Below are the steps for creating the AWS Glue Network Connection with the EC2 machine on which Fire Insights has been installed.

Step 1 : Check Pre-requisites
--------

Ensure you have an AWS account with administrative access.

Step 2 : Create VPC for ENI
------

Firstly, you have to create a VPC with a private and a public subnet. You need a VPC because the AWS Glue Job needs an Amazon Elastic network interface (ENI) to call the REST API over the internet. To create ENI in the private subnet as below:

#. Allocate Elastic IP:
   
   Login to the **AWS Console**. Select an AWS Region of your choice where AWS Glue is available as a service. You will see the exercise instructions using the Paris region. Go to the **VPC Management Console**. Click on the **Elastic IPs menu item** in the left and then click on the **Allocate Elastic IP address** button.


   .. figure:: ../../../_assets/aws/glue/vpc.png
      :alt: aws
      :width: 60%

   On the next screen, click on the **Allocate** button. An Elastic IP address is created which you will use for the NAT Gateway when creating the VPC.

#. Enter Connection name as **dojoconnection**. Select **Network** as the Connection type and click on the **Next** button.

   .. figure:: ../../../_assets/aws/glue/ip_pool.png
      :alt: aws
      :width: 60%

#. On the VPC Management Console, click on the **Launch VPC Wizard** button.

   .. figure:: ../../../_assets/aws/glue/vpc_wizard.png
      :alt: aws
      :width: 50%

#. On the next screen, select **VPC with Public and Private Subnets** option and click on the **Select** button.

   .. figure:: ../../../_assets/aws/glue/vpc_configuration.png
      :alt: aws
      :width: 50%

#. On the next screen, enter **GlueVPC** as the VPC Name and select the **Elastic IP address** (created in the previous steps) for the Elastic IP Allocation ID field. Keep the rest of the values as default and click on the **Create VPC** button.

   .. figure:: ../../../_assets/aws/glue/vpc_public.png
      :alt: aws
      :width: 50%

  The VPC will be created in a couple of minutes. Please wait for it to finish. You will use VPC private subnet and the default security group, later, to create ENI to call the REST API using AWS Glue Connection.

Step 2 : Create IAM Role
------------

Now, you need to create an Amazon IAM Role which the AWS Glue Job will use for the authorization to perform the task.

#. Go to the **IAM Management Console**. Click on the **Roles menu item** in the left and then click on the **Create role** button.

   .. figure:: ../../../_assets/aws/glue/roles.png
      :alt: aws
      :width: 50%

#. Select **Glue** as the AWS Service on the next screen and click the **Next: Permissions** button.

   .. figure:: ../../../_assets/aws/glue/aws_glue_1.PNG
      :alt: aws
      :width: 50%


#. On the next screen, select **AdministratorAccess** as the policy and click on the **Next: Tags** button. In actual production use, you will not use administrative access permission.

   .. figure:: ../../../_assets/aws/glue/role_admin.png
      :alt: aws
      :width: 50%

#. On the next screen, click on the **Next: Review** button.

#. On the next screen, enter the Role name and click on the **Create role** button. The role is created in no time.

Step 3 : Create S3 Bucket
--------------

You will create an Amazon S3 bucket which serves many purposes. It will be used to store Python script for the AWS Glue job. It will also be used by AWS Glue job to copy data returned by the REST API call.

#. Go to the **S3 Management Console** and create a S3 bucket. Please make sure you select the region of the bucket the same as the VPC created in the previous steps. If this bucket name is not available, kindly use another bucket name and make note of the name as you will need it for the configuration and scripting purposes.

Step 4 : Create Glue Connection
-----------------

Creating AWS Glue Connection is a very important step in completing this exercise. The connection is used to create an ENI in the private subnet of the VPC. AWS Glue job uses ENI to make call to the internet based REST API. The connection type used is Network.

#. Go to the **AWS Glue Console**, select **Connections** in the left menu and click on the **Add connection** button.

   .. figure:: ../../../_assets/aws/glue/connection.png
      :alt: aws
      :width: 50%

#. Enter the Connection name as **dojoconnection**. Select **Network** as the Connection type and click on the **Next** button.

   .. figure:: ../../../_assets/aws/glue/add_connection.PNG
      :alt: aws
      :width: 50%

#. On the next screen, select **GlueVPC** as the VPC. Select **Private Subnet** for the Subnet. Select the **default Security Group**. Finally click on the **Next** button.

   .. figure:: ../../../_assets/aws/glue/vpc_connection.PNG
      :alt: aws
      :width: 50%

#. On the next screen, click on the **Finish** button. It will create the network type connection. Select the **connection** and click on the **Test connection** button to test the connection.

   .. figure:: ../../../_assets/aws/glue/connection_success.PNG
      :alt: aws
      :width: 50%

#. On the popup screen, select the role specified and specific S3 bucket, then use that one. Click on the **Test connection** button.

   .. figure:: ../../../_assets/aws/glue/test_connection.PNG
      :alt: aws
      :width: 50%

   The connection test will take some time. Wait till the test status is displayed as successful.

   .. figure:: ../../../_assets/aws/glue/success_test_connection.PNG
      :alt: aws
      :width: 50%

Step 5 : VPC Peering Connections
----------

Now, since Fire Insights and AWS Glue are running on separate VPC's, we can use VPC Peering connection to enable communication from AWS Glue VPC to Fire Insights VPC.

#. Create Peering connection.

   .. figure:: ../../../_assets/aws/glue/peering_communication.PNG
      :alt: aws
      :width: 50%
   

#. On successful creation, you will be able to see peering connection with Status active.

   .. figure:: ../../../_assets/aws/glue/peering_connection_list.PNG
      :alt: aws
      :width: 50%
   
   .. note:: Ignore the above steps if Fire Insights and AWS Glue are running on same VPC.   
