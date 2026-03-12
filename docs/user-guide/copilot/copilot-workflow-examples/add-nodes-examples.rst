Add Nodes Examples
====

This guide shows how to structure effective prompts and use Copilot to add nodes to existing workflows.

Follow the steps below to explore how Copilot can help you modify and enhance your existing data processes more efficiently.


**Opening the Copilot Assistant**
+++++++++++++++++++++
Click on the **Copilot** button to open the Assistant window. Type your queries into the text field and click **Enter** to interact with Copilot.

.. figure:: ../../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Generate-Response.PNG
    :alt: copilot configuration
    :width: 60%


**Add Nodes - Example Prompts**
+++++++++++++++++++++

Example 1
++++

**Prompt**

Add a Row Filter node after node 4 with condition "total_day_minutes > 250"
 
**Before**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-1-before.png
    :alt: copilot configuration
    :width: 60%

**After**

After receiving the response, you can choose to **preview** or **select** it. The **Preview** button lets you review the generated workflow before making a decision. Selecting **Select** converts the response into the workflow edit page, where you can continue refining it.

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-1-after.png
    :alt: copilot configuration
    :width: 60%


Example 2
++++

**Prompt**

Add a Save CSV node as a new branch after node 4 to save to "/path/to/file/output" with overwrite mode
 
**Before**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-2-before.png
    :alt: copilot configuration
    :width: 60%

**After**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-2-after.png
    :alt: copilot configuration
    :width: 60%


Example 3
++++

**Prompt**

Add a node between node 4 and 6 to convert the time in column "time" with format "yyyy-MM-dd HH:mm:ss" to UNIX time and name the new column "time_unix"
 
**Before**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-3-before.png
    :alt: copilot configuration
    :width: 60%

**After**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-3-after.png
    :alt: copilot configuration
    :width: 60%


Example 4
++++

**Prompt**

Add a Data Cleansing node to remove all whitespace from the "churned" column after node 2. 
Then add a Row Filter node after it with condition "churned = 'True'"". 
Then add a Group node to group the results by "state" and "usage_flag" columns. 
Then add a node to print the first 20 rows.
 
**Before**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-4-before.png
    :alt: copilot configuration
    :width: 60%

**After**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-4-after.png
    :alt: copilot configuration
    :width: 60%


Example 5
++++

**Prompt**

Add a Rest API Client Node to send a GET reqeust to "https://api.example.com/data" with header "Authorization : Bearer example_token". 
Then add a node to drop the columns "col1", "col2", and "col3".
Then add a ndoe to print the first 20 rows.
 
**Generated Workflow**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-5.png
    :alt: copilot configuration
    :width: 60%


Example 6
++++

**Prompt**

Add a Case When node on a new branch after node 3 to create a new column "usage_flag" with the following values:
1. When "total_day_minutes > 200" the value is "High"
2. When "total_day_minutes < 100" the value is "Low"
 
**Before**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-6-before.png
    :alt: copilot configuration
    :width: 60%

**After**

 .. figure:: ../../../_assets/user-guide/copilot/add-nodes-workflow-examples/example-6-after.png
    :alt: copilot configuration
    :width: 60%