Read Databricks Tables
======================

Fire Insights enables users to read from and write to Databricks tables by using the Read Databricks Table processor.

This document explains the detailed steps required to read Databricks Tables in Fire Insights.

Step 1 : Create Workflow 
----------------------
#. Create a workflow with following processors:

   * **Read Databricks Table**: Use this processor to read tables from Databricks.
   * **Other Processors**: Use the other processors available in Fire for processing the data read from the Databricks table.

   **Example Workflow:**

   * Below is an example workflow which reads data from the Databricks table **xyz**. It then processes the data and prints some sample results.

     .. figure:: ../../_assets/configuration/databricks-workflow.png
        :alt: Databricks
        :width: 60%

Step 2 : Configure Processor
-----------------

#. Configure the **Read Databricks Table** processor as below:

   * DATABRICKS DATABASE : Click on **BROWSE STUDIO DB** and select specified database.
   * DATABRICKS TABLE : Click on **BROWSE STUDIO TABLE** and select specified Table.


      .. figure:: ../../_assets/configuration/databricks-editor.PNG
         :alt: Databricks
         :width: 80%
#. Refresh schema for Read Databricks Table processor.

   * Click on **Refresh Schema** button to view schema and click **Okay** button.

     .. figure:: ../../_assets/configuration/databricks-refreshschema.PNG
        :alt: Databricks
        :width: 60% 

#. View processor executions for Read Databricks Table.

   * Click on the **play button** to view executions as below:
     
     .. figure:: ../../_assets/configuration/databrcks-interactiveexecutions.PNG
        :alt: Databricks
        :width: 60%

Step 3 : Execute Workflow
-----------------------
#. To view the output, click on **Execute** button.

   * Below is the output of executing the above workflow which reads data from a Databricks table.

     .. figure:: ../../_assets/configuration/databricks-workflowexecutions.PNG
        :alt: Databricks
        :width: 60%
   
   
