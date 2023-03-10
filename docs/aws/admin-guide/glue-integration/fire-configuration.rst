Fire Configurations & Job Submission on AWS Glue
==========================

Since, you have successfully established a connection between EC2 Machine on which Fire Insights is running and AWS Glue, so now you can create connection for Glue in Fire Insights and create workflow and submit the job on AWS Glue.

1. Login to Fire Insights application and Create Glue Connection.

Refer the below page for connecting Fire Insights to AWS Glue.

https://docs.sparkflows.io/en/latest/installation/connection/compute-connection/glue.html


2. Create workflow in Fire.

Now, you can create a Housing Analytics workflow in Fire which reads from S3 bucket doing some filter and calculations and save the workflow.

.. figure:: ../../../_assets/aws/glue/aws_glue_2.PNG
   :alt: aws
   :width: 60%

.. note:: Make sure that data reading from s3 in workflow should be accessible.

4. Submit the Job.

After saving Housing Analytics workflow, you can execute the job which will be submitted on AWS Glue Cluster using connection dropdown and you will see response in Fire Insights.

.. figure:: ../../../_assets/aws/glue/aws_glue_3.PNG
   :alt: aws
   :width: 80%

.. figure:: ../../../_assets/aws/glue/aws_glue_4.PNG
   :alt: aws
   :width: 80%


.. note::  Make sure to use Glue Connection while Execution.   

5. Verify the Job on AWS Glue Cluster.

Now you may verify the Job run on Fire Insights from AWS Glue Job by accessing the AWS Portal.

.. figure:: ../../../_assets/aws/glue/aws_glue_5.PNG
   :alt: aws
   :width: 60%
   
