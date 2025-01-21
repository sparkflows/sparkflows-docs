Write To GCS
============

Fire Insights has processor to write data to GCS. This document explains detailed steps required to write data to GCS.

Follow the steps given below:

Step 1 : Create or Edit a Workflow
++++++++++++++++++++++++++++++++
Create a new workflow or edit an existing one:

#. Go to workflow editor.

Step 2 : Use any Save Data Node
++++++++++++++++++++++++++++++++
To find Save Data nodes:

#. In the data connectors, search for Save Nodes like **Save CSV**, **Save Parquet**, **Save JSON**, **Read Bigquery** etc. 
#. Drag and drop it to the workflow editor.

   .. figure:: ../../_assets/gcp/gs_save_workflow.png
      :alt: Write to GCS
      :width: 60%
   
Step 3 : Configure the Save Data Node
++++++++++++++++++++++++++++++++
To configure:

#. Double-click on the selected Save Data Node like **Save CSV**, **Save Parquet**, **Save JSON**, **Read Bigquery** etc. 
#. Configure the **Save CSV** node as below. Fields would vary based on the node selected.

   .. figure:: ../../_assets/gcp/gs_save_configuration.png
      :alt: Write to GCS
      :width: 60%

* **Path:** Click on the **Browse GCS** button to select a location to save data to.
* **Save Mode:** Select a value from the dropdown. Select **Append** to append data to the location or **Overwrite** to overwrite the data.
* **Header:** Select a value from the dropdown. Select **True** if Header is to be saved and **False** when header is not needed to be saved.

Step 4 : Run the Workflow on Dataproc Connection
++++++++++++++++++++++++++++++++

#. Execute the workflow on Dataproc to write data to GCS using Dataproc Connection. 

   .. figure:: ../../_assets/gcp/gs_savegcs_execution.png
      :alt: Write to GCS
      :width: 60%
