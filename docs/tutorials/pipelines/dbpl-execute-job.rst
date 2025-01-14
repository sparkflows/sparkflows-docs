Databricks Execute Existing Job Pipeline
=================================

This tutorial will guide you through using the Airflow Databricks Pipeline feature to execute an existing **Databricks Job** on a Databricks Cluster using either a **Job ID** or a **Job Name**.

It will cover the following key aspects:

* Defining Databricks Workspace connection.
* Defining Airflow connection and synching the created Databricks connection.
* Pipeline creation to execute existing Databricks Job, and add Steps to it.
* Configuring the Databricks Run Now node.
* Executing and monitoring the pipeline.

Defining Databricks Workspace connection
^^^^^^^^^^^^^^^^^^^^^^^^

#. Define a **Databricks Workspace Connection** as below. This is a pre-requisite step. It will be used in the **Airflow** connection and would be synched to Airflow.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-databricks-connection.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-databricks-connection1.png
      :alt: Pipeline Tutorials
      :width: 70%

Defining Airflow connection
^^^^^^^^^^^^^^^^^^^^^^^^

#. Define a **Airflow Connection** as below. This is a pre-requisite step. It will be used to conenct and communicate with the **Airflow** to execute jobs.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-airflow-connection.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-airflow-connection1.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-airflow-connection2.png
      :alt: Pipeline Tutorials
      :width: 70%

* Select the **Databricks Workspace Connection** created in the previous step.
* Click on the **Sync** Button to the synch the Databrick connection to the Airflow.
	  
Pipeline Set Up
^^^^^^^^^^^^^^^^^^^^^^^^

#. Select the **Airflow Connection** created in the previous step. It would be used to communicate with the **Airflow**.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-select-airflowconn.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Create a Pipeline as shown below. More nodes can be added based on the functionality.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-executejob-pipeline.png
      :alt: Pipeline Tutorials
      :width: 40%

Databricks Run Now Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add two **Databricks Run Now nodes** to the pipeline and configure them as shown below. These nodes will execute existing **Databricks Jobs** in a **Databricks Cluster** based on the provided configuration.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-execjob-node.png
      :alt: Pipeline Tutorials
      :width: 70%
	  
   .. figure:: ../../_assets/tutorials/pipeline/dbpl-execjob-node1.png
      :alt: Pipeline Tutorials
      :width: 70%

  * One node configuration uses **Job ID** and other uses **Job Name**. It is advisable not to enter values to both the fields at the same time.	

#. Enter the desired values in the required fields as follows:

	*   **Task Name:** Enter Unique name of the task in the Airflow DAG i.e. **create_cluster**
	*   **Job ID:** Enter an existing **Job ID**.
	*   **Job Name:** Select an existing **Job Name** from the dropdown.
	*   **Databricks Connection:** It would display the **Databricks Connection** used in the read only mode.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Pipeline to execute it. Upon execution, Databricks Jobs would be executed in the cluster as below.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-execjob-plexec.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-execjob-plexec1.png
      :alt: Pipeline Tutorials
      :width: 70%

#. In **Airflow UI DAG** would be created and status would be updated appropriately as below.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-execjob-airflowuidag.png
      :alt: Pipeline Tutorials
      :width: 70%

#. **Jobs** in the **Airflow** would be created as below.

   .. figure:: ../../_assets/tutorials/pipeline/dbpl-execjob-airflowuijob.png
      :alt: Pipeline Tutorials
      :width: 70%
