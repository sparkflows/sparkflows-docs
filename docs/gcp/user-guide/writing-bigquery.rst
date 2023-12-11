Write to Big Query
============

Fire Insights has processor to write to Big Query Tables. This document explains detailed steps required to write to BigQuery Tables.

Follow the steps given below:


Step 1 : Create or Edit a Workflow
+++++++++++++++++++
Create a new workflow or edit an existing one:

#. Go to workflow editor.


Step 2 : Create the Write To BigQuery Node
++++++++++++++++++++++++++++++++
To create the node:

#. Search for the **Write To BigQuery** Node in the Data Connectors section of Node Repository and drag and drop it to the workflow editor.

   .. figure:: ../../_assets/gcp/biguery_write.PNG
      :alt: Read BigQuery Node
      :width: 60%
   
Step 3 : Configure the Write To BigQuery Node
++++++++++++++++++++++++++++++++
To configure the Node:

#. Double click on the **Write To BigQuery** Node to configure the table connection. Once you've configured, press **ok**.

   .. figure:: ../../_assets/gcp/write_bigquery.PNG
      :alt: Read BigQuery Node
      :width: 60%

#. Click on **Save** to save the workflow.

Step 4 : Submit the Workflow on Dataproc Connection
++++++++++++++++++++++++++++++++
To submit the workflow on Dataproc Connection:

#. Click on the **connection icon** located on RHS of top-menu bar and select the **Dataproc Connection** from the dropdown list.
#. Click on **Execute** button to submit the workflow on Dataproc connection.


