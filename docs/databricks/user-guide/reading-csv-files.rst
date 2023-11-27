Read CSV Files
=================================

There are multiple ways to read and process CSV files in Fire Insights.

#. Use Read CSV node in the workflow for reading the CSV file from DBFS.
#. Create an unmanaged Databricks Table on the CSV file. Then, use the Read Databricks Table node in the workflow.
#. Create a dataset in Fire Insights on the CSV file in DBFS. Then, use that Dataset in a workflow.

This document describes the detailed steps involved in the multiple ways to read and process CSV files.

1. Use of Read CSV Node
-------------------

**Step 1 : Create Workflow and Configure the Read CSV Node**
++++++++++

#. Create a workflow using a **Read CSV** node. For more details, read `Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/quick-start/4-create-workflow.html>`_
   
   The workflow  given below has a Read CSV node which reads CSV files from DBFS and processes them.

   .. figure:: ../../_assets/databricks/csv_file.PNG
       :alt: Databricks
       :width: 60%

#. Open the configuration window by double-clicking on the node.
#. Enter the path of the file, which can either be the CSV file itself or a folder containing many CSV files of the same schema.
#. Click on **Refresh Schema** button to update the schema.
#. After successful refresh, click on the **Okay** button to save the configuration settings.

**Step 2 : Save and Execute the Workflow**
+++++++++

#. Give a name to your workflow and click on the **Save** button.
#. Now, click on the **Execute** button to execute the workflow. 

   For more details, read `Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/quick-start/5-execute-workflow.html>`_ 

    
2. Use of Read Databricks Table Node
-------------

**Step 1 : Create an unmanaged Databricks Table on the CSV File**
++++++++++++++++++

#. The command given below shows an example of creating an unmanaged Databricks Table on the CSV file.

   ::

       CREATE TABLE `housing` ( `id` INT, `price` DOUBLE, `lotsize` INT, `bedrooms` INT, `bathrms` INT, `stories` INT, `driveway` STRING, `recroom` STRING, `fullbase` STRING, `gashw` STRING, `airco` STRING, `garagepl` STRING, `prefarea` STRING) USING com.databricks.spark.csv OPTIONS ( `multiLine` 'false', `escape` '"', `header` 'true', `delimiter` ',', path 'dbfs:/FileStore/sample-data/data/housing.csv' ) 

**Step 2 : Create Workflow and Configure Read Databricks Table Node**
++++++++++++++

#. Create a workflow utilizing a **Read Databricks Table** node. For more details, read `Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/quick-start/4-create-workflow.html>`_
   
   The workflow given below uses the Read Databricks Table Node to read in the data from the Databricks table created above.

   .. figure:: ../../_assets/databricks/databrick_table.PNG
      :alt: Databricks
      :width: 60%

#. Open the configuration window by double-clicking on the node.
#. Specify the table from which data is to be read and click on the **Okay** button.

**Step 3 : Save and Execute the Workflow**
++++++++++++++++++

#. Give a name to your workflow and click on the **Save** button.
#. Now, click on the **Execute** button to execute the workflow. 

   For more details, read `Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/quick-start/5-execute-workflow.html>`_ 

3. Use of Dataset Created in Fire Insights on the CSV File
---------------
Fire Insights supports the concept of Datasets. Dataset is the definition of the data it represents. This way the Dataset can be defined just once and used in multiple workflows.

**Step 1 : Create Dataset**
++++++++++++

#. Create a dataset in Fire Insights on the CSV file in DBFS
   
   To get detailed steps on how to create a dataset, read `Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/quick-start/3-create-datasets.html>`_

   Below is the creation of a Dataset on a CSV file.

   .. figure:: ../../_assets/databricks/data.PNG
      :alt: Databricks
      :width: 60%

**Step 2 : Utilize the Dataset in Workflow**
+++++++++++++

#. Create a workflow using the dataset created in the above step.

   **Note** : Navigate to the Node Repository on the left-hand side pane and click on the **Datasets** tab to access the list of previously created datasets.

   The workflow given below shows the usage of the Dataset created in step 1.

   .. figure:: ../../_assets/databricks/dataset.PNG
      :alt: Databricks
      :width: 60%   

**Step 3 : Save and Execute the Workflow**
+++++++++++++++++
#. Give a name to your workflow and click on the **Save** button.
#. Now, click on the **Execute** button to execute the workflow. 

   For more details, read `Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/quick-start/5-execute-workflow.html>`_ 


