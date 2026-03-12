Create Pipeline Examples
====

This guide shows how to structure effective prompts and use Copilot to create new pipelines.


**Opening the Copilot Assistant**
+++++++++++++++++++++
Click on the **Copilot** button to open the Assistant window. Type your queries into the text field and click **Enter** to interact with Copilot.

.. figure:: ../../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Generate-Response.PNG
    :alt: copilot configuration
    :width: 60%


**Create - Example Prompts**
+++++++++++++++++++++

Example 1
++++

**Prompt**

Create the pipeline that:

1. Adds an emr cluster
2. Adds a step to the emr with the workflow name "wf_token_size" after step 1
3. Adds a step sensor to check the status from step 2
4. Terminate the cluster once the step sensor is completed after step 3
 
**Generated Pipeline**

After receiving the response, you can choose to **preview** or **select** it. The **Preview** button lets you review the generated pipeline before making a decision. Selecting **Select** converts the response into the pipeline edit page, where you can continue refining it.

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-1.png
    :alt: copilot configuration
    :width: 60%


Example 2
++++

**Prompt**

Create a pipeline that:

1. Adds an S3 Sensor to wait for a file arrival in the bucket “raw-data-uploads”
2. Adds a Branch Python Operator node after step 1 which checks the file extension between .csv and .parquet
3. Adds a Run Snowflake Command as a new branch from node 2
4. Adds a Create Cluster node as a new branch from node 2
5. Adds a Run Notebook node with notebook name “process_parquet” after step 4
6. Adds a Terminate Cluster node after step 5
7. Joins output from step 3 and step 6 using the Empty Operator node after step 6
8. Adds Email Notification to send a success status after step 7
9. Adds a Trigger Next DAG node with name “downstream_analytics" after step 8
 
**Generated Pipeline**

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-2.png
    :alt: copilot configuration
    :width: 60%


Example 3
++++

**Prompt**

Create a pipeline that:

1. Runs snowflake command "CALL SAMPLE_DB.SAMPLE_SCHEMA.SP_RUN_JOB('JOB_NAME')" with task name "run_job"
 
**Generated Pipeline**

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-3.png
    :alt: copilot configuration
    :width: 60%


Example 4
++++

**Prompt**

Create a pipeline that:

1. Runs the workflow "Create Example 1"
2. Runs the workflow "Create Example 2" after step 1
3. Runs the workflow "Create Example 3" after step 2
 
**Generated Pipeline**

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-4.png
    :alt: copilot configuration
    :width: 60%


Example 5
++++

**Prompt**

Create a pipeline that:

1. Adds a S3 Sensor node with task name "monitor_incoming_sales_data", bucket name "incoming-sales-data", bucket key "*.csv", poke interval "60", and timeout "3600"
2. Adds a Run Notebook node after step 1 with task name "clean_sales_data_task", notebook path "clean_sales_data"
3. Adds a Run Snowflake Command node after step 2 with task name "load_sales_stage" and sql query "COPY INTO sales_stage FROM @incoming_sales_stage FILE_FORMAT = (TYPE = CSV);"
4. Adds an Email Notification node after step 3 with taks name "send_success_notification", email address "data-team@example.com", subject "Sales Data Pipeline Success", and content "The sales data pipeline completed successfully and data has been loaded into the sales_stage table."
 
**Generated Pipeline**

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-5.png
    :alt: copilot configuration
    :width: 60%


Example 6
++++

**Prompt**

Create a pipeline that:

1. Adds an S3 Sensor node
2. Adds a Create Cluster node after step 1
3. Adds a Run Notebook node after step 2
4. Adds a Run Snowflake Command node after step 3
5. Adds a Terminate Cluster node after step 4
6. Adds Email Notification after termination after step 5

**Generated Pipeline**

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-6.png
    :alt: copilot configuration
    :width: 60%


Example 7
++++

**Prompt**

Create a pipeline that:

1. Adds an S3 Sensor to wait for files in bucket “raw-sales-data”
2. Adds a Run Notebook node with path “clean_sales_data” after step 1
3. Adds a Run Snowflake Command node after step 2 with task name "load_sales_stage" after step 2
4. Adds an Email Notification node on a new branch from step 2
   
**Generated Pipeline**

 .. figure:: ../../../_assets/user-guide/copilot/create-pipeline-examples/example-7.png
    :alt: copilot configuration
    :width: 60%
