EMR Livy Job Submission
===============

Sparkflows empowers you to submit jobs or workflows through a Livy connection once you've established one successfully. 

This document provides an in-depth guide to the steps required for submitting jobs via a Livy Connection.

Following the steps given below would allow you to successfully submit jobs using a Livy Connection:



Step 1 : Login to Fire Insights
------------
To login :

#. Open Fire Insights **Login page** to enter your credentials and click **Sign in**.

Step 2 : Create Sample Workflow
-----------

#. Create a sample workflow which reads some sample data from S3 and prints some sample output.
#. Save the workflow.

      .. figure:: ../../../_assets/aws/livy/sample_wf.PNG
         :alt: livy
         :width: 60%

Step 3 : Execute Sample Workflow
----------
#. Once you have saved the workflow, execute it and select the connection as Livy.

      .. figure:: ../../../_assets/aws/livy/wf_livy.PNG
         :alt: livy
         :width: 60%
   
      .. figure:: ../../../_assets/aws/livy/wf_livy_submission.PNG
         :alt: livy
         :width: 60%   
   
      .. figure:: ../../../_assets/aws/livy/wf_livy_Submitted.PNG
         :alt: livy
         :width: 60%   

Step 4 : View Job Status
--------------------

#. After successful execution, you can view the Job status from YARN application and from AWS Console too.

      .. figure:: ../../../_assets/aws/livy/emr_job.PNG
         :alt: livy
         :width: 60%
