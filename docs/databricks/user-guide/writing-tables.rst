Writing to Databricks Tables
======================

Fire Insights enables you to write to Databricks tables.


In the workflow use the processor 'SaveDatabricksTable'. It will allow you to save data to tables to Databricks.

Below is a workflow which writes data to the Databricks table ``test_save``.

Workflow
++++++++

.. figure:: ../../_assets/configuration/savedatabricksworkflow.PNG
   :alt: Databricks
   :align: center
   :width: 60%

Processor Configurations for SaveDatabricksTable
++++++++

.. figure:: ../../_assets/configuration/savedatabricksconfiguration.PNG
   :alt: Databricks
   :align: center
   :width: 60%



Databricks Workflow execution
++++++++

Below is the output of executing the above workflow which saves the data to Databricks table.

.. figure:: ../../_assets/configuration/savedatabricksworkflowexecution.PNG
   :alt: Databricks
   :align: center
   :width: 60%

* Verify the Table


.. figure:: ../../_assets/configuration/databrickstablesaved.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   
   
File Formats
++++++++++++

The tables can be saved into CSV, JSON, Parquet and ORC file formats.

If the file format is not specified, the data in tables is stored in Parquet format.



