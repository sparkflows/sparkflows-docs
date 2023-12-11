Read from GCS
============

Fire Insights has processor to read from GCS. This document explains detailed steps required to read data from GCS.

Follow the steps given below:

Step 1 : Create or Edit a Workflow
++++++++++++++++++++++++++++++++
Create a new workflow or edit an existing one:

#. Go to workflow editor.

Step 2 : Use any File Reader Node
++++++++++++++++++++++++++++++++
To find File Reader nodes:

#. In the data connectors, search for File Reader Nodes like **Read CSV**, **Read Parquet**, **Read JSON**, etc. 
#. Drag and drop it to the workflow editor.

   .. figure:: ../../_assets/gcp/gs_configuration.PNG
      :alt: Read Files from GCS
      :width: 60%
   
Step 3 : Configure the File Reader Node
++++++++++++++++++++++++++++++++
To configure:

#. Double-click on the selected File Reader Nodes like **Read CSV**, **Read Parquet**, **Read JSON**, etc.
#. Select the required file and specify the file specific properties. In **Read CSV** node, you have to specify how the csv data can be extracted.
#. Once you've configured, make sure to click on the **Refresh Schema** button to fetch the schema. 

   .. figure:: ../../_assets/gcp/gs_configuration.PNG
      :alt: Read Files from GCS
      :width: 60%

Step 4 : Run the Workflow on Dataproc Connection
++++++++++++++++++++++++++++++++

#. Execute the workflow on Dataproc to read the data from GCS using Dataproc Connection. 

   .. figure:: ../../_assets/gcp/gs_job1.PNG
      :alt: Read Files from GCS
      :width: 60%

   .. figure:: ../../_assets/gcp/gs_job2.PNG
      :alt: Read Files from GCS
      :width: 60%
   
   .. figure:: ../../_assets/gcp/gs_job3.PNG
      :alt: Read Files from GCS
      :width: 60%   
