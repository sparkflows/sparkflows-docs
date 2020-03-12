Reading / Writing
======================

Fire Insights enables you to read from and write to Databricks tables.

Below is a workflow which read data from the Databricks table xyz. It then processes the data and finally writes out the result to the Databricks table abc.


Read Databricks table in Workflow
------------------------------------------

In the workflow use the processor 'ReadDatabricksTable'. It will allow you to read tables from Databricks.

Then use the other processors in Fire for processing the data read from the Databricks Table.

Workflow
++++++++

.. figure:: ../_assets/configuration/workflow-databricks.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Processor Configurations for ReadDatabricksTable
++++++++

.. figure:: ../_assets/configuration/databricks_editor.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Refresh schema for processor ReadDatabricksTable
++++++++
 
.. figure:: ../_assets/configuration/databricks_refreshschema.PNG
   :alt: Databricks
   :align: center
   :width: 60% 

Processor executions for ReadDatabricksTable
++++++++

.. figure:: ../_assets/configuration/databrcks_interactiveexecutions.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Databricks Workflow execution
++++++++

Below is the output of executing the above workflow which reads data from a Databricks table.

.. figure:: ../_assets/configuration/databricks_workflowexecutions.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   
   
Write to Databricks Table in a Workflow
---------------------------------------



Browse Databricks Databases and Tables
--------------------------------------

Fire Insights allows you to Browse your Databricks Schema.

Go to ``DATABROWSERS/Connections``. It will display the various Databricks Connections in your Applications.


.. figure:: ../_assets/configuration/databricks_browse_connection.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Select the relevant ``connection`` to use it for browing the Databricks Schema.

.. figure:: ../_assets/configuration/databricks_database.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   
Select ``CLUSTER`` tab to see detail informations of databrick cluster 

.. figure:: ../_assets/configuration/databricks_cluster_details.PNG
   :alt: Databricks
   :align: center
   :width: 60%

