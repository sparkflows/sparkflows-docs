Saving Data to HIVE
==================

As par of your data pipeline or workflow, you might want to save data to HIVE after it has been read from a data source, cleaned and transformed. After data is saved in HIVE it can be read from another workflow or accessed through BI tools such as Tableau.


Cluster vs Standalone Mode
--------------------------

In your workflow, drag and drop a "SaveAsHIVETable" processor. Confirgure this processor to save your data into HIVE as a table which can be read later. 

Note: Fire Insights can run in cluster mode or in the standalone mode. These settings are in Administration/Configuration.When connecting to HIVE, Sparkflows must be running in cluster mode on an edge node of a Hadoop cluster. HIVE settings have to be correctly set under Administration/Configuration-> app.runOnCluster.

The example workflow below, contains "SaveAsHIVETable" processor. It reads Housing dataset and saves it into the HIVE 'housing_table'.

.. figure:: ../../_assets/tutorials/dataset/24.PNG
   :alt: Dataset
   :align: center
   :width: 60%

When the example workflow is executed, data is written into HIVE table 'housing_table'.

.. figure:: ../../_assets/tutorials/dataset/25.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
The 'housing_table' gets created with the schema of the Housing Dataset.

.. figure:: ../../_assets/tutorials/dataset/26.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
   



