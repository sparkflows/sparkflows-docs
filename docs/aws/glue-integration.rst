Glue Integration
================

Fire Insights can be configured to submit jobs to the AWS Glue cluster.


Architecture diagram
----------

.. figure:: ..//_assets/aws/glue/architecture.png
   :alt: aws
   :width: 60%

Below are the steps for AWS Glue Network Connection to call Fire Insights APIs in Aws Glue Jobs.

pre-requisite
--------

You need to have an AWS account with administrative access.

Create-vpc
------

You first create a VPC with a private and a public subnet. You need a VPC because the AWS Glue Job needs an Amazon Elastic network interfaces (ENI) to call the REST API over internet.

1. Login to the AWS Console. Select an AWS Region of your choice where AWS Glue is available as a service. You will see the exercise instructions using the Paris region. Go to the VPC Management Console. Click on the Elastic IPs menu item in the left and then click on the Allocate Elastic IP address button.


.. figure:: ..//_assets/aws/glue/vpc.png
   :alt: aws
   :width: 60%

2. On the next screen, click on the Allocate button. An Elastic IP address is created which you will use for the NAT Gateway when creating the VPC.

.. figure:: ..//_assets/aws/glue/ip_pool.png
   :alt: aws
   :width: 60%

3. On the VPC Management Console and click on the Launch VPC Wizard button.

.. figure:: ..//_assets/aws/glue/vpc_wizard.png
   :alt: aws
   :width: 60%
