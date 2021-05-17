Saving Data to HIVE
==================

As part of your data pipeline or workflow, you might want to save data to HIVE after it has been read from a data source, cleaned, and transformed. After data is saved in HIVE it can be read from another workflow or accessed through BI tools such as Tableau.


Cluster vs Standalone Mode
--------------------------

In your workflow, drag and drop a "SaveAsHIVETable" processor. Configure the processor to save your data into HIVE as a table that can be read later. 

Note: Fire Insights can run in cluster mode or standalone mode. These settings are in Administration/Configuration. When connecting to HIVE, Sparkflows must be running in cluster mode on an edge node of a Hadoop cluster. HIVE settings have to be correctly set under Administration/Configuration-> app.runOnCluster.

The example workflow below contains the "SaveAsHIVETable" processor. It reads the Transaction dataset and saves it into the HIVE 'sample_08' table.

.. figure:: ../../_assets/tutorials/dataset/SaveHiveTableWorkflow.png
   :alt: Dataset
   :width: 90%

Fill the required fields.

.. figure:: ../../_assets/tutorials/dataset/HiveTableNodeConfiguration.png
   :alt: Dataset
   :width: 90%
   
When the example workflow is executed, data is written into the HIVE table as 'sample_08'.   
The 'sample_08' gets created with the schema of the Transaction Dataset.
   
   



