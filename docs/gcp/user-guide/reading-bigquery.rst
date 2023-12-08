Read from BigQuery
============

Fire Insights has processor to read from BigQuery Tables. This document explains detailed steps required to read data from BigQuery.

Follow the steps given below:

Step 1 : Create or Edit a Workflow
++++++++++++++++++++++++++++++++
Create a new workflow or edit an existing one:

#. Go to workflow editor.

Step 2 : Create the Read BigQuery Node
++++++++++++++++++++++++++++++++
To create the node:

#. Search for the **Read BigQuery** Node in the Data Connectors section of Node Repository and drag and drop it to the workflow editor.

   .. figure:: ../../_assets/gcp/biguery_read.PNG
      :alt: Read BigQuery Node
      :width: 65%
   
Step 3 : Configure Read BigQuery Node
++++++++++++++++++++++++++++++++
To configure the Node:

#. Double click on the **Read BigQuery** Node, to configure the table connection. 

#. Once you've configured, make sure to click on the **Refresh Schema** button to fetch the schema. 

   .. figure:: ../../_assets/gcp/biguery_config.PNG
      :alt: Read BigQuery Node
      :width: 65%

#. Click on **Save** to save the workflow.

Step 4 : Submit Workflow on Dataproc Connection
++++++++++++++++++++++++++++++++
To submit the workflow on Dataproc Connection:

#. Click on the **connection** icon located on RHS of top-menu bar and select the **Dataproc Connection** from the dropdown list.
#. Click on **Execute** button to submit the workflow. 

   .. figure:: ../../_assets/gcp/dataproc_job1.PNG
      :alt: Read BigQuery Node
      :width: 65%

   .. figure:: ../../_assets/gcp/dataproc_job2.PNG
      :alt: Read BigQuery Node
      :width: 65%

   .. figure:: ../../_assets/gcp/dataproc_job3.PNG
      :alt: Read BigQuery Node
      :width: 65%
