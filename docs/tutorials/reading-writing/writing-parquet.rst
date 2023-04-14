Save as Parquet Files
================

Fire Insights enables the user to write in a Parquet file.

Workflow
--------

Below is the workflow. It does the following:

* Reads transaction dataset.
* Saves Parquet file to the specified location.

.. figure:: ../../_assets/user-guide/read-write/Save-Parquet/save-parquet-wf.png
   :alt: readwrite
   :width: 70%

Reads transaction dataset
---------------------

It reads the transaction dataset.

Processor configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/Save-Parquet/read-config.png
   :alt: readwrite
   :width: 70%
   
Processor output
^^^^^^

.. figure:: ../../_assets/user-guide/read-write/Save-Parquet/read-output.png
   :alt: readwrite
   :width: 70%

Save Parquet file
----------------

It saves the Parquet file in the specified location.

Processor configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/Save-Parquet/save-parquet-config.png
   :alt: readwrite
   :width: 70%
   
Once the workflow is executed successfully the Parquet file will be saved to the specified location.

.. figure:: ../../_assets/user-guide/read-write/Save-Parquet/save-parquet-execution.png
   :alt: readwrite
   :width: 70%
