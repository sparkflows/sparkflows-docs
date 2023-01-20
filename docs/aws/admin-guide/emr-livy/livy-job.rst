EMR Livy Job Submission
===============

This is a stepwise guide to enable you to use a Livy Connection to submit jobs or workflows after you have successfully created an Apache Livy Connection in Sparkflows.

Detailed Steps
++++++++++

Following the steps given below would allow you to successfully submit jobs using a Livy Connection. 

1. Login to Fire Insights application and Create a sample workflow as shown below:

   Create a workflow which reads some sample data from S3 and Print some sample output.

      .. figure:: ../../../_assets/aws/livy/sample_wf.PNG
         :alt: livy
         :width: 60%

2. Execute the workflow

   Once you have saved the workflow, execute it and select the connection as Livy.

      .. figure:: ../../../_assets/aws/livy/wf_livy.PNG
         :alt: livy
         :width: 60%
   
      .. figure:: ../../../_assets/aws/livy/wf_livy_submission.PNG
         :alt: livy
         :width: 60%   
   
      .. figure:: ../../../_assets/aws/livy/wf_livy_Submitted.PNG
         :alt: livy
         :width: 60%   

3. View Job status from YARN application and AWS Console

   After successful execution, you can view the Job status from YARN application and from AWS Console too.

      .. figure:: ../../../_assets/aws/livy/emr_job.PNG
         :alt: livy
         :width: 60%
