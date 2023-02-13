Fire Configurations & Job Submission on AWS Glue
==========================

Since, you have successfully established a connection between VM on which Fire Insights is running and AWS Glue, so now we can configure Fire Insights for Glue and create workflow and submit the job on AWS Glue.

1. Login to Fire Insights application and Create Glue Connection.

Refer the below page for connecting Fire Insights to AWS Glue.

https://docs.sparkflows.io/en/latest/installation/connection/compute-connection/glue.html


2. Create workflow in Fire.

Now, you can create an example workflow in Fire which reads from S3 bucket and save the workflow.

.. figure:: ../../../_assets/aws/glue/wf.PNG
   :alt: aws
   :width: 60%

4. Submit the Job.

After saving example workflow, you can execute the job which will be submitted on AWS Glue Cluster and you will see response in Fire Insights.

.. figure:: ../../../_assets/aws/glue/job_submit.PNG
   :alt: aws
   :width: 80%

5. Verify the Job on AWS Glue Cluster.

Now you may verify the Job run on Fire Insights from AWS Glue Job by accessing the AWS Portal.

.. figure:: ../../../_assets/aws/glue/glue_job_verify.PNG
   :alt: aws
   :width: 60%
   
.. note::  Make sure to use Glue Connection while Execution.   
