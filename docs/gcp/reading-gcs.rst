Read from GCS
============

Fire Insights has processor to read from BigQuery Tables.

1. Create a new workflow to read data from GCS
++++++++++++++++++++++++++++++++

- Create a new workflow or edit an existing one in the workflow editor.

2. Use any File Reader Node
++++++++++++++++++++++++++++++++

- In the data connectors, search for File Reader Nodes like ``Read CSV``, ``Read Parquet``, ``Read JSON`` etc. 
- Drag and drop it to the workflow editor.

.. figure:: ../_assets/gcp/read-gcs.png
   :alt: Read Files from GCS
   :width: 40%
   
3. Configure the File Reader Node
++++++++++++++++++++++++++++++++

- For example, double click on the selected File Reader Nodes like ``Read CSV``, ``Read Parquet``, ``Read JSON`` etc.
- Configure the table connection. Once you've configured, make sure to click on the ``Refresh Schema`` button to fetch the schema. 


.. figure:: ../_assets/gcp/configure-gcs.png
   :alt: Configure GCS File Reader Node
   :width: 40%
