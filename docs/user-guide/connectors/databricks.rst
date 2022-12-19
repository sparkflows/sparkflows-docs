Databrikcs
==========

Fire Insights has a processor that allows you to connect with databrikcs table and dbfs file system.

Read Databricks table in Workflow
---------------------------------

In the workflow use the processor 'ReadDatabricksTable'. It will allow you to read tables from Databricks.

Then use the other processors in Fire for processing the data read from the Databricks Table.

Workflow
++++++++

.. figure:: ../../_assets/configuration/workflow_databricks.PNG
   :alt: Databricks
   :width: 60%

Processor Configurations for ReadDatabricksTable
++++++++

* DATABRICKS DATABASE : Click on BROWSE STUDIO DB and select specified database.
* DATABRICKS TABLE : Click on BROWSE STUDIO TABLE and select specified Table.


.. figure:: ../../_assets/configuration/databricks-editor.PNG
   :alt: Databricks
   :width: 80%

Refresh schema for processor ReadDatabricksTable
++++++++
 
.. figure:: ../../_assets/configuration/databricks-refreshschema.PNG
   :alt: Databricks
   :width: 80% 

Processor executions for ReadDatabricksTable
++++++++

.. figure:: ../../_assets/configuration/databrcks-interactiveexecutions.PNG
   :alt: Databricks
   :width: 80%

Databricks Workflow execution
++++++++

Below is the output of executing the above workflow which reads data from a Databricks table.

.. figure:: ../../_assets/configuration/databricks-workflowexecutions.PNG
   :alt: Databricks
   :width: 80%



In the workflow use the processor `SaveDatabricksTable`. It will allow you to save data to Databricks tables.

Below is a workflow which writes data to the Databricks table ``default``.

Workflow
++++++++

.. figure:: ../_assets/configuration/savedatabricks_workflow.PNG
   :alt: Databricks
   :width: 60%

Processor Configurations for SaveDatabricksTable
++++++++

* DATABRICKS DATABASE : Click on BROWSE STUDIO DB and select specified database.
* DATABRICKS TABLE : Click on BROWSE STUDIO TABLE and select specified Table.
* FORMAT : The tables can be saved into CSV, JSON, Parquet and ORC file formats.
* SAVE MODE : Append, overwrites, ErrorifExists or Ignore

.. figure:: ../_assets/configuration/savedatabricks_configuration.PNG
   :alt: Databricks
   :width: 90%



Databricks Workflow execution
++++++++

Below is the output of executing the above workflow which saves the data to Databricks table.

.. figure:: ../_assets/configuration/savedatabricksworkflo_wexecution.PNG
   :alt: Databricks
   :width: 90%

* Verify the Table


.. figure:: ../_assets/configuration/databrickstable_saved.PNG
   :alt: Databricks
   :width: 90%
   
   
File Formats
++++++++++++

The tables can be saved into CSV, JSON, Parquet and ORC file formats.

If the file format is not specified, the data in tables is stored in Parquet format.

