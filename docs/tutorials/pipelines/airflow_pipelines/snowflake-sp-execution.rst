Snowflake Stored Procedure Execution
======
This document provides instructions for executing a Snowflake stored procedure—using Airflow with the Snowflake Command node and running a Python script on EMR.

Execute Stored Procedure Using Airflow
------
#. Use the **Run Snowflake Command** node in your pipeline.
#. Ensure your Airflow connection is configured with **Connection Type** as **Snowflake**.
#. In the **SQL Query** field, add the command to execute the desired Snowflake stored procedure, as shown below. The execution below will be triggered on the Airflow machine.
   
   .. figure:: ../../../_assets/tutorials/pipeline/run-sf-command-node-config.png
       :alt: Pipeline Tutorials
       :width: 60%

Execute Stored Procedure Using a Python Script on EMR
------
#. Use the **AddStepToEMR** with a Python script to execute the stored procedure on EMR.
#. Upload your Python script to EMR.
#. On the EMR cluster, install the required packages:
   
   * snowflake-connector-python
   * boto-core

#. Also, provide necessary permissions:

   * To fetch secrets (for authentication/credentials)
   * To upload content to S3

   .. figure:: ../../../_assets/tutorials/pipeline/add-step-emr.png
       :alt: Pipeline Tutorials
       :width: 60%

#. You can also include the following command in your EMR step to copy and install as part of the execution.

   ::

      "aws s3 cp s3://assume-role-bucket1/snowflake_sp/snowflake_exec.py . && sudo python3 -m pip install snowflake-connector-python && spark-submit --master yarn --deploy-mode client snowflake_exec.py"













