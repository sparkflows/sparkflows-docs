Reading Databricks Tables
======================

Fire Insights enables you to read from and write to Databricks tables.

Below is a workflow which reads data from the Databricks table ``xyz``. It then processes the data and finally writes out the result to the Databricks table abc.


Read Databricks table in Workflow
------------------------------------------

In the workflow use the processor 'ReadDatabricksTable'. It will allow you to read tables from Databricks.

Then use the other processors in Fire for processing the data read from the Databricks Table.

Workflow
++++++++

.. figure:: ../../_assets/configuration/workflow-databricks.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Processor Configurations for ReadDatabricksTable
++++++++

.. figure:: ../../_assets/configuration/databricks_editor.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Refresh schema for processor ReadDatabricksTable
++++++++
 
.. figure:: ../../_assets/configuration/databricks_refreshschema.PNG
   :alt: Databricks
   :align: center
   :width: 60% 

Processor executions for ReadDatabricksTable
++++++++

.. figure:: ../../_assets/configuration/databrcks_interactiveexecutions.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Databricks Workflow execution
++++++++

Below is the output of executing the above workflow which reads data from a Databricks table.

.. figure:: ../../_assets/configuration/databricks_workflowexecutions.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   
   
