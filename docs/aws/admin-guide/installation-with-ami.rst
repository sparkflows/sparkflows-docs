Install Sparkflows using AWS Custom AMI
=======================================

You can install Sparkflows using the custom AWS AMI image, which has all the necessary configurations baked into it, and ready to use for evaulation purpose.
Sparkflows AMI submitted in AWS Marketplace can be easily available using search in Google page or you can use below link:

https://aws.amazon.com/marketplace/pp/prodview-h7bpihqpr7ios#pdp-usage

Requirements
--------

In Order to use Sparkflows AMI, user should have:

- AWS Account with sufficient Privilege.
- System Distributions that have SystemD as init system.


Installation Steps
--------

- Make sure to read all instructions updated on the usage Instructions of Sparkflows AMI.
- Once done with above instructions, Click on Continue to Subscribe
  
  .. figure:: ../../_assets/aws/aws-marketplace.png
   :alt: aws marketplace
   :width: 80%
   
- Next Click on Continue to Configuration where detail information of the product will be displayed.

  .. figure:: ../../_assets/aws/aws-ami-configure.png
     :alt: aws configure sparkflows
     :width: 80%

- Configure the EC2 instance with the appropriate Software version and region.

  .. figure:: ../../_assets/aws/aws-fulfillment-options.png
     :alt: aws fulfillment options for sparkflows
     :width: 80%
     
- Select the EC2 instance type, which has atleast 8vCPU and 64GB RAM. Also select your preferred VPC.

  .. figure:: ../../_assets/aws/vpc-ec2-setting.png
     :alt: aws fulfillment options for sparkflows with vpc
     :width: 60%

- Finally choose the EC2 key pair and click on launch.

  .. figure:: ../../_assets/aws/marketplace-launch-ec2.png
     :alt: aws fulfillment options for sparkflows with ec2 keypair
     :width: 80%

Access the application
--------

Once the Instance is in Running state and stable, you can login to below url as updated in usage instructions:

- http://host_name:8080 (hostname or ip)
- Login with admin/Instance ID(you can copy from aws instance running)

