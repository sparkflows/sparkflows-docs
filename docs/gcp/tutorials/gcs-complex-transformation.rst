GCS Complex Data Transformation Tutorial
=================================

This tutorial will guide you through using the Sparkflows Nodes to perform complex data transformation using **GCS Read/Write** and **BigQuery Read/Write** processors.

It will cover the following key aspects:

* Configuring GCP and adding Dataproc connection
* Reading and Writing data to BigQuery.
* Reading and Writing data to GCS.
* Joining data read from BigQuery with the data read from GCS.
* Data transformation using various processors.
* Configuring the Read/Write processors.

Configuring GCP Details
^^^^^^^^^^^^^^^^^^^^^^^^

#. Configure **GCP** details under **Administration > Configurations** as below.

   .. figure:: ../../_assets/gcp/cdt-tutorials-gcp-config.png
      :alt: GCS Tutorials
      :width: 70%

#. Enable **Dataproc** connection under **Administration > Configurations** as below.

   .. figure:: ../../_assets/gcp/cdt-tutorials-enable-dataproc.png
      :alt: GCS Tutorials
      :width: 70%

Defining Dataproc connection
^^^^^^^^^^^^^^^^^^^^^^^^

#. Define a **Dataproc Connection** as below. This is a pre-requisite step. It will be used for job submission.

   .. figure:: ../../_assets/gcp/cdt-tutorials-dataproc-conn.png
      :alt: GCS Tutorials
      :width: 70%
	  
   .. figure:: ../../_assets/gcp/cdt-tutorials-dataproc-conn1.png
      :alt: GCS Tutorials
      :width: 70%

	  
Workflow Creation
^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a workflow as below using various Sparkflows Processors. Other processors can be added based on the use case implementation.

   .. figure:: ../../_assets/gcp/cdt-tutorials-workflow.png
      :alt: GCS Tutorials
      :width: 70%

Read BigQuery Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a **Read BigQuery Node** to the workflow and configure it as shown below. This node will read data from the selected table.

   .. figure:: ../../_assets/gcp/cdt-tutorials-bigquery-read.png
      :alt: GCS Tutorials
      :width: 70%
	  
#. Enter the desired values in the required fields as follows:

	*   **BigQuery Dataset:** Browse and select a dataset.
	*   **BigQuery Table:** Browse and select a table.
	*   Click on **Refresh Schema** button to fetch the schema details of the selected table.

Read GCS Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a **Read CSV Node** to the workflow and configure it as shown below to read data from **GCS**. This node will read data from the selected **GCS Location**.

   .. figure:: ../../_assets/gcp/cdt-tutorials-gcs-read.png
      :alt: GCS Tutorials
      :width: 70%
	  
#. Enter the desired values in the required fields as follows:

	*   **Path:** Browse and select path to the dataset.
	*   Select other values as appropriate.
	*   In the **Schema** tab click on **Refresh Schema** button to fetch the schema details of the selected dataset.

Join Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a **JOin Node** to the workflow and configure it as shown below to join two datasets.

   .. figure:: ../../_assets/gcp/cdt-tutorials-join.png
      :alt: GCS Tutorials
      :width: 70%
	  
Save GCS Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a **Save CSV Node** to the workflow and configure it as shown below to write data to **GCS**. This node will write data to the selected **GCS Location**.

   .. figure:: ../../_assets/gcp/cdt-tutorials-gcs-write.png
      :alt: GCS Tutorials
      :width: 70%
	  
#. Enter the desired values in the required fields as follows:

	*   **Path:** Browse and select path to save the data.
	*   Select other values as appropriate.
	  
Save BigQuery Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a **save BigQuery Node** to the workflow and configure it as shown below. This node will write data to the selected table.

   .. figure:: ../../_assets/gcp/cdt-tutorials-bigquery-write.png
      :alt: GCS Tutorials
      :width: 70%
	  
#. Enter the desired values in the required fields as follows:

	*   **BigQuery Dataset:** Browse and select a dataset.
	*   **BigQuery Table:** Browse and select a table.
	*   **Temporary Bucket:** Enter temporary Cloud Storage Bucket which would be used to save intermediate results.
	  
Workflow Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Workflow to execute it. Upon execution, Workflow would be executed in the Dataproc cluster as below.

   .. figure:: ../../_assets/gcp/cdt-tutorials-workflow-execute.png
      :alt: GCS Tutorials
      :width: 50%

#. It would be submitted to the dataproc cluster as below.

   .. figure:: ../../_assets/gcp/cdt-tutorials-dataproc-submit.png
      :alt: GCS Tutorials
      :width: 70%
	  
#. Upon successful execution data would be written to the GCS and BigQuery as below.

   .. figure:: ../../_assets/gcp/cdt-tutorials-gcs-save-exec.png
      :alt: GCS Tutorials
      :width: 50%
	  
   .. figure:: ../../_assets/gcp/cdt-tutorials-bigquey-save-exec.png
      :alt: GCS Tutorials
      :width: 70%
