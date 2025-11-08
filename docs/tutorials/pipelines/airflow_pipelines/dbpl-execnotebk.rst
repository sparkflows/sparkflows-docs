Execute Notebook on Databricks Cluster
=================================

This tutorial will guide you through using the Airflow Databricks Pipeline feature to create a Databricks Cluster and execute a Databricks Notebook on it.

It will cover the following key aspects:

* Creating a Databricks Cluster.
* Executing a Databricks Notebook.
* Executing and monitoring the pipeline.

Pipeline Set Up
^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a Pipeline as shown below. More nodes can be added based on the functionality.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-execnotebk-pipeline.png
      :alt: Pipeline Tutorials
      :width: 70%

Create Databricks Cluster Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **Create Databricks Cluster** node to the pipeline and configure it as shown below. **Create Databricks Cluster** node creates a new **Databricks Cluster** by using the details in configuration and passes the Cluster id to the next step.

	.. figure:: ../../../_assets/user-guide/pipeline/create-db-cluster.png
	   :alt: Pipeline
	   :width: 70%
   
	.. figure:: ../../../_assets/user-guide/pipeline/create-db-cluster2.png
	   :alt: Pipeline
	   :width: 70%

	*   **Task Name:** Enter Unique name of the task in the Airflow DAG i.e. **create_cluster**
	*   **Databricks Runtime Version:** Select a value from the drop which would be used for Cluster creation i.e. **10.4.x-scala2.12**
	*   **Worker Type:** Enter type of the Worker Node to be created i.e. **Standard_D4plds_v6**
	*   **Driver Type:** Enter type of the Worker Node to be created i.e. **Standard_D4plds_v6**
	*   **Number of Minimum Worker:** Enter a value for min number of Worker Nodes to be onboarded i.e. **1**.
	*   **Number of Maximum Worker:** Enter a value for max number of Worker Nodes to be onboarded i.e. **1**.
	*   **Spark Config:** Spark Config values would be used while executing spark jobs on the cluster. Enter a value in Key-Value pair i.e. **spark.sql.shuffle.partitions - 200**.
	*   **Custom Tags:** It is used to categorize and for better management of clusters. Enter a value in Key-Value pair i.e. **environment - production**
	*   **Init Scripts Path:** Add path of the script to perform initial setup tasks when cluster is started. Enter a value as appropriate.

Run Databricks Notebook Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **Run Databricks Notebook** node to the pipeline and configure it as shown below. **Run Databricks Notebook** node can be used to execute a **Databricks Notebook** in a **Databricks Cluster** by using the details in configuration.

	.. figure:: ../../../_assets/user-guide/pipeline/create-db-runnotebook.png
	   :alt: Pipeline
	   :width: 70%
   
	*   **Task Name:** Enter Unique name of the task in the Airflow DAG i.e. **submit_job_task**
	*   **Cluster ID:** It can be left blank. It would use the Cluster created in the earllier step.
	*   **Notebook Path:** Enter path of the **Databricks Notebook** that needs to be executed.
	*   **Base Parameters:** These parameters are passed to the notebook and are used for processing. Enter values as per the notebook definition.
	*   **Select Databricks Connection:** Select the Databricks Connection from the dropdown.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Pipeline to execute it. Upon execution, Databricks cluster would be created and the selected Notebook would be executed.
