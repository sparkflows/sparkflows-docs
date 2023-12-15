Fire Configurations & Job Submission on AWS Glue
==========================

After you have successfully established a connection between EC2 Machine on which Fire Insights is running and AWS Glue, you are now ready to create connection for Glue in Fire Insights and create workflow and submit the job on AWS Glue.

Follow the steps given below:

Step 1 : Login to Fire Insights
--------------
#. Login to Fire Insights application using your credentials.

Step 2 : Create Glue Connection
----------
#. To create Glue Connection, refer to the `AWS Documentation for connecting Fire Insights to AWS Glue. <https://docs.sparkflows.io/en/latest/installation/connection/compute-connection/glue.html>`_ 

Step 3 : Create Workflow in Fire
------------------------
#. You can go inside any project to create a Housing Analytics workflow in Fire which reads from S3 bucket doing some filter and calculations and save the workflow.

   .. figure:: ../../../_assets/aws/glue/aws_glue_2.PNG
      :alt: aws
      :width: 65%

   .. note:: Make sure that data reading from S3 in workflow should be accessible.

Step 4 : Submit the Job
-------------------
#. After saving Housing Analytics workflow, you can execute the job which will be submitted on AWS Glue Cluster using connection dropdown and you will see response in Fire Insights.

   .. figure:: ../../../_assets/aws/glue/aws_glue_3.PNG
      :alt: aws
      :width: 65%

   .. figure:: ../../../_assets/aws/glue/aws_glue_4.PNG
      :alt: aws
      :width: 65%


   .. note::  Make sure to use Glue Connection while Execution.   

Step 5 : Verify Job Execution on AWS Glue Cluster
-------------------------------
#. Now, you may verify the Job run on Fire Insights from AWS Glue Job by accessing the AWS Portal.

   .. figure:: ../../../_assets/aws/glue/aws_glue_5.PNG
      :alt: aws
      :width: 65%
   
