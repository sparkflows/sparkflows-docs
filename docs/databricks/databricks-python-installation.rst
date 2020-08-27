Databricks Python Integration Steps
======================

Fire Insights integrates with Databricks with python package. It submits jobs to the Databricks clusters using the REST API of Databricks and have the results displayed back in Fire Insights.

Below are the steps for Integrating Fire Insights with your Databricks Clusters using python package.

NOTE: The Machine should have python with version 3.7.0 or above.


Install Fire Insights
-----------

Install Fire Insights on any machine. The machine has to be reachable from the Databricks cluster.

Upload Fire wheel file to Databricks
----------------------------------

Fire Insights wheel file has to be uploaded to Databricks. Fire Insights jobs running on Databricks make use of this wheel file, as it contains all python package needed.

Upload ``fire-x.y.z/dist/fire-3.1.0-py3-none-any.whl`` to Databricks. Upload it under Workspace as a Library on to Databricks under DBFS.


.. figure:: ../_assets/configuration/wheelfile.PNG
   :alt: Databricks
   :align: center
   :width: 40%

1. Login to ``Databricks Cluster``
++++++++++++++++++++++++++++++++

2. Click on ``workspace`` in the left side pane
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/azure_workspace.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
3. Create a new Library
++++++++++++++++++++++++++++++++

