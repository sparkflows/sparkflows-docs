Copilot Examples
====

This guide provides examples of using Copilot to create and update workflows and pipelines. 

Follow the steps below to see how Copilot can assist in building and modifying your data processes.

Workflow Copilot Examples
----
Click on the **Copilot** button to open the Assistant window.

.. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Generate-Response.PNG
     :alt: copilot configuration
     :width: 60%

**Example Prompts**
+++++++++++++++++++++

Example 1
++++

**Step 1: Create the Initial Workflow using the prompt**

Prompt 1

Create a workflow by:

1. Reading Parquet data from the S3 location: **s3a://assume-role-bucket1/data/housing_parquet/**.

2. Selecting rows with a price greater than 42,000.

3. Selecting columns with names: **id**, **price**, **lotsize**, and **bedrooms**.

4. Saving the output as Parquet to the S3 location: **s3a://assume-role-bucket1/data/assit_output** with overwrite mode.

* After receiving the response, the user can select and preview it. The **Select** button converts the response into the workflow edit page.

  .. figure:: ../../_assets/user-guide/copilot/copilot-example-wf.png
     :alt: copilot configuration
     :width: 60%

**Step 2: Update the Created Workflow with more functions by using another prompt**

* Update the workflow by calculating ``totalprice = price * lotsize`` after the row filter. 
* Then select the final columns: **id**, **price**, **lotsize**, **bedrooms**, and **totalprice**.

  .. figure:: ../../_assets/user-guide/copilot/wf-add-math-expression.png
     :alt: copilot configuration
     :width: 60%
   
  In the above, a **MathExpression** is added with ``totalprice = price * lotsize``.


**Step 3: Add a New Field**

* Update the workflow with one more field to calculate: ``sqft_price = lotsize / price``


Example 2
++++

**Prompt 1**

Create a workflow that:

1. Reads a parquet file from this path “s3a://dp-nucleus-us-east-1-dev/Sparkflows-data/erics/270/”
2. Print the first 13 rows from Step 1 on a new branch
3. Filter rows where event_source = DirectGatewayRequest from Step 1
4. Select columns “record_uuid, event_source, payload” from Step 3
5. Save the output of Step 4 to this path "s3a://dp-nucleus-us-east-1-dev/Sparkflows-data/output" as a parquet file

 .. figure:: ../../_assets/user-guide/copilot/copilot-ex2-prompt1-wf.png
    :alt: copilot configuration
    :width: 60%


**Prompt 2**

Update the workflow by:

1. Print first 2 rows from output of node 4 as a new branch
2. Update node 1 to read from file 's3a://test'
3. Remove node 3 and connect node 1 to node 4
4. Remove node 2


 .. figure:: ../../_assets/user-guide/copilot/copilot-ex2-prompt2-wf.png
     :alt: copilot configuration
     :width: 60%


Example 3
++++

**Prompt 1**

Create a workflow that: 

1. Reads the CSV located at “/home/sparkflows/fire-data/TELCO/Telco-Churn-Prediction/Raw-Data/churn.csv”
2. Remove the rows from step 1 where any of the following columns are null “state, account_length, total_day_minutes, churned”
3. Use Data Cleansing Node to remove all whitespaces anywhere in the string on the “churned” column from step 2
4. Filter rows from step 3 by the rule: “churned = ‘True.’”
5. Print the first 20 rows from the output of step 4 as a new branch
6. Group the output of step 4 by “state” and calculate average of total_day_minutes as “avg_total_day_minutes”, average of total_day_charge as “avg_total_day_charge”, and count of churned customers as “churned_count”
7. Sort the output of step 6 by churn count in descending order 
8. Write the output of step 7 as a CSV to “/home/sparkflows/fire-data/TELCO/Telco-Churn-Prediction/Cleaned_aggregated/” in overwrite mode

 .. figure:: ../../_assets/user-guide/copilot/copilot-ex3-prompt1-wf.png
     :alt: copilot configuration
     :width: 60%



Pipeline Copilot Example
----

Click on the **Copilot** button to open the Assistant window.

.. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Generate-Response.PNG
     :alt: copilot configuration
     :width: 60%

**Example Prompt**
++++++++++++++++++++++++

* Create the pipeline:

  1. By adding an EMR cluster.

  2. Adding a step to EMR with the workflow name **ExampleWorkflow**.

  3. Adding a step sensor node to check the status of the above step.

  4. Terminating the cluster once the step sensor node is completed.

* After receiving the response, the user can select and preview it. The **Select** button converts the response into the pipeline edit page.

  .. figure:: ../../_assets/user-guide/copilot/copilot-example-pipeline.png
     :alt: copilot configuration
     :width: 60%










