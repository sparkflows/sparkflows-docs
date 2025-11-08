Databricks Create Cluster Pipeline Tutorials
=================================

This tutorial will guide you through using the Airflow Databricks Pipeline feature to create Databricks Cluster using the selected connection.

It will cover the following key aspects:

* Defining Databricks Workspace connection.
* Defining Airflow connection and synching the created Databricks connection.
* Pipeline creation to create Databricks Cluster, and add Steps to it.
* Configuring the Create Cluster node.
* Executing and monitoring the pipeline.

Defining Databricks Workspace connection
^^^^^^^^^^^^^^^^^^^^^^^^

#. Define a **Databricks Workspace Connection** as below. This is a pre-requisite step. It will be used in the **Airflow** connection and would be synched to Airflow.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-databricks-connection.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-databricks-connection1.png
      :alt: Pipeline Tutorials
      :width: 70%

Defining Airflow connection
^^^^^^^^^^^^^^^^^^^^^^^^

#. Define a **Airflow Connection** as below. This is a pre-requisite step. It will be used to conenct and communicate with the **Airflow** to execute jobs.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-airflow-connection.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-airflow-connection1.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-airflow-connection2.png
      :alt: Pipeline Tutorials
      :width: 70%

* Select the **Databricks Workspace Connection** created in the previous step.

* Click on the **Sync** Button to the synch the Databrick connection to the Airflow.
	  
Pipeline Set Up
^^^^^^^^^^^^^^^^^^^^^^^^

#. Select the **Airflow Connection** created in the previous step. It would be used to communicate with the **Airflow**.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-select-airflowconn.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Create a Pipeline as shown below. More nodes can be added based on the functionality.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-pipeline.png
      :alt: Pipeline Tutorials
      :width: 40%

Create Cluster Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **Create Cluster node** to the pipeline and configure it as shown below. This node will create a **Databricks cluster running on AWS** based on the provided configuration.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-node.png
      :alt: Pipeline Tutorials
      :width: 70%
	  
   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-node1.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Enter the desired values in the required fields as follows:

	*   **Task Name:** Enter Unique name of the task in the Airflow DAG i.e. **create_cluster**
	*   **Databricks Runtime Version:** Select a value from the drop which would be used for Cluster creation i.e. **10.4.x-scala2.12**
	*   **Worker Type:** Enter type of the Worker Node to be created i.e. **Standard_D4ds_v5**
	*   **Driver Type:** Enter type of the Worker Node to be created i.e. **Standard_D4ds_v5**
	*   **Number of Minimum Worker:** Enter a value for min number of Worker Nodes to be onboarded i.e. **1**.
	*   **Number of Maximum Worker:** Enter a value for max number of Worker Nodes to be onboarded i.e. **1**.
	*   **Spark Config:** Spark Config values would be used while executing spark jobs on the cluster. Enter a value in Key-Value pair i.e. **spark.sql.shuffle.partitions - 200**.
	*   **Custom Tags:** It is used to categorize and for better management of clusters. Enter a value in Key-Value pair i.e. **environment - production**
	*   **Init Scripts Path:** Add path of the script to perform initial setup tasks when cluster is started. Enter a value as appropriate.
	*   **Databricks Connection:** It would display the **Databricks Connection** used in the read only mode.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Pipeline to execute it. Upon execution, Databricks cluster would be created as below.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-plexec.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-plexec1.png
      :alt: Pipeline Tutorials
      :width: 70%

#. In **Airflow UI DAG** would be created and status would be updated appropriately as below.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-airflowuidag.png
      :alt: Pipeline Tutorials
      :width: 70%

#. **Job** in the **Airflow** would be created as below.

   .. figure:: ../../../_assets/tutorials/pipeline/dbpl-createcluster-airflowuijob.png
      :alt: Pipeline Tutorials
      :width: 70%
