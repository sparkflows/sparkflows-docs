Write to Databricks Tables
======================

Fire Insights enables you to write to Databricks tables with the use of Save Databricks Table processor.

In the workflow, use the processor **SaveDatabricksTable**. It will allow you to save data to Databricks tables.

This document explains the detailed steps required to write data to Databricks Tables.

Step 1 : Create Workflow
-----------

#. Create a workflow with following processors:

   * **Read Databricks Table:** Use this processor to read tables from Databricks.
   * **Save Databricks Table:** Use this processor to save data to Databricks table.

   **Example Workflow:**

   * Below is a workflow which writes data to the Databricks table **default**.

     .. figure:: ../../_assets/configuration/savedatabricks_workflow.PNG
        :alt: Databricks
        :width: 60%

Step 2 : Configure Processor
----------------

 #. Configure the Save Databricks Table processor as below:

    * DATABRICKS DATABASE : Click on **BROWSE STUDIO DB** and select specified database.
    * DATABRICKS TABLE : Click on **BROWSE STUDIO TABLE** and select specified Table.
    * FORMAT : The tables can be saved into CSV, JSON, Parquet and ORC file formats.
    * SAVE MODE : Append, overwrites, ErrorifExists or Ignore.

      .. figure:: ../../_assets/configuration/savedatabricks_configuration.PNG
         :alt: Databricks
         :width: 60%


Step 3 : Execute Workflow
--------------
#. To save the table, click on the **Execute** button.

   * Below is the output of executing the above workflow which saves the data to Databricks table.

     .. figure:: ../../_assets/configuration/savedatabricksworkflo_wexecution.PNG
        :alt: Databricks
        :width: 60%

#. Table Verification.

   * Verify the table:

     .. figure:: ../../_assets/configuration/databrickstable_saved.PNG
        :alt: Databricks
        :width: 90%
   

.. Note:: File Formats:

* The tables can be saved into CSV, JSON, Parquet and ORC file formats.
* If the file format is not specified, the data in tables is stored in Parquet format.



