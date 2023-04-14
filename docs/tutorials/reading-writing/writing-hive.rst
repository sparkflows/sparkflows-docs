Save data to HIVE
==================

Depending on your data pipeline or workflow, you might want to save data to HIVE after it has been read from a data source, cleaned and transformed. After data is saved in HIVE, it can be read from another workflow or accessed through BI tools such as Tableau.


Cluster vs Standalone Mode
--------------------------

In your workflow, drag and drop a ``SaveAsHIVETable`` processor. Configure the processor to save your data into HIVE as a table which can be read later. 

.. Note:: Fire Insights can run in cluster mode or in the standalone mode. These settings are in Administration/Configuration. When connecting to HIVE, Sparkflows must be running in cluster mode on an edge node of a Hadoop cluster. HIVE settings have to be correctly set under Administration/Configuration-> app.runOnCluster.

The sample workflow below, contains "SaveAsHIVETable" Processor. It reads Transaction Dataset and saves it into the HIVE 'sample_08' table.

.. figure:: ../../_assets/tutorials/dataset/save-hive-wf.png
   :alt: Dataset
   :width: 70%

Fill the required fields.

.. figure:: ../../_assets/tutorials/dataset/save-hive-config.png
   :alt: Dataset
   :width: 85%
   
When the sample workflow is executed, data is written into HIVE Table as 'sample_08'.   
The 'sample_08' gets created with the schema of the Transaction Dataset.
   
   



