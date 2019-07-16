Saving Data to HIVE
==================

Workflows allow us to create data pipelines. In data pipelines, data is transformed, models can be generated etc. We might want to save the resulting data at some point to a HIVE table. It would also thus allow the data to be accessed through BI tools like Tableau.

Fire Insights has one node to saving data to HIVE:

- SaveAsTable : Saves the data into a HIVE table

Cluster vs Standalone Mode
--------------------------

- Fire Insights can be running in Cluster mode or in the Standalone mode. These settings are in Administration/Configuration. The specific parameter is app.runOnCluster.

- When connecting to HIVE, Sparkflows should be running in Cluster mode on an edge node of a Hadoop Cluster. The HIVE settings have to be correctly set under Administration/Configuration.

Below is a workflow containing SaveAsTable. It reads in the Housing Dataset and saves it into the HIVE table 'housing_table'.

.. figure:: ../../_assets/tutorials/dataset/24.PNG
   :alt: Dataset
   :align: center
   :width: 60%

When the workflow is executed, the data is written into the HIVE table 'housing_table'.

.. figure:: ../../_assets/tutorials/dataset/25.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
The 'housing_table' gets created with the schema of the Housing Dataset.

.. figure:: ../../_assets/tutorials/dataset/26.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
   



