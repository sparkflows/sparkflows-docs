Fire Configuartions & Job Submission on AWS Glue
==========================

Now you have connection between vm on which Fire Insights is running and AWS Glue, so now we can configure Fire Insights for Glue and create workflow and submit the job on AWS Glue.

1. Login to Fire Insights application and go inside Configurations

Once you login to Fire Insights application Click on ADMINISTRATION tab on top, it will take you to configuration page, on clicking, it will take to configuration page.

.. figure:: ..//_assets/aws/glue/config.PNG
   :alt: aws
   :width: 60%

2. Update below parameter as per our configurations

Now update below parameter as per AWS configurations

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Enable/Disable workflow execution on AWS Glue
     - Enable/Disable workflow execution on AWS Glue
     - true
   * - Script Location
     - Glue script location
     - s3://aws-glue-scripts/scripts/FireGlueApp.scala
   * - IAM Role
     - AWS IAM Role
     - AWSGlueServiceRole-Sparkflows
   * - Glue Main Class  
     - Glue Main class to execute
     - FireGlueApp
   * - Default Arguments
     - Pass any parameters as default arguments
     - --TempDir s3://aws-glue-temporary
   * - Glue Version
     - Glue Version. If empty it takes default glue version.
     - 2.0
   * - Glue Language
     - Glue Language. Input should scala or python
     - scala
   * - Extra Jars
     - Extra Jar file path pass in default arguments
     - s3://aws-glue-scripts/fire-spark_2.4-core-3.1.1-jar-with-dependencies.jar
   * - S3 Path
     - S3 bucket location where workflow json file gets uploaded for execution
     - s3://aws-glue-scripts/workflow-json
   * - Glue Connections
     - Glue connection names. Input the glue connection names as comma separated value like Glue-conn, Glue-conn1
     - Glue-Fire

.. figure:: ..//_assets/aws/glue/glue_parameter.PNG
   :alt: aws
   :width: 80%

3. Create Workflow in Fire

Now you can create an example workflow in Fire, which reads from S3 bucket and save the workflow.

.. figure:: ..//_assets/aws/glue/wf.PNG
   :alt: aws
   :width: 60%

4. Submit the Job

After saving example workflow, now you can execute the job which will be submitted on AWS Glue Cluster and you will see response in Fire Insights.

.. figure:: ..//_assets/aws/glue/job_submit.PNG
   :alt: aws
   :width: 80%

5. Verify the Job on AWS Glue Cluster

Now you may verify the Job run on Fire Insights from AWS Glue Job from AWS Portal too.

.. figure:: ..//_assets/aws/glue/glue_job_verify.PNG
   :alt: aws
   :width: 60%
