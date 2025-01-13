Databricks Terminate Cluster
=========
**Databricks Terminate Cluster** node can be used to terminate an existing Databricks Cluster. This action halts the cluster's compute resources, releasing them to help optimize costs by preventing charges for idle resources. This is particularly useful for managing costs when a cluster is no longer needed for ongoing workloads.

This guide explains the setup process for the Databricks Terminate Cluster node.

Configuration of Databricks Terminate Cluster Node
-------------------

#. **Databricks Terminate Cluster** node can be configured as shown below.

   .. figure:: ../../../_assets/user-guide/pipeline/db-terminatecluster.png
      :alt: Pipeline
      :width: 70%

#. Select the desired values in the above required fields as follows:
   
   * **Task Name:** Enter a unique name of the task in the Airflow DAG.
   * **Cluster ID:** Enter the ID of an existing Databricks cluster. If left blank, the Cluster ID created in the previous step will be used.
   * **Select Databricks Connection:** Select a Databricks Connection from the dropdown list. The list contains the connections defined in the Airflow and the selected connection will be used by the Airflow to communicate with Databricks.
