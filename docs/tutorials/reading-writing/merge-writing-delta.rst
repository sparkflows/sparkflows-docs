Using Merge Write Option to Write to Delta Lake
===============================================

Fire Insights also provides the option to write to Delta Lake using the Merge write operation. This approach enables users to handle incremental data and make updates or insertions to the Delta table based on specified conditions.

Workflow
--------

The following workflow demonstrates how to use the Merge write option. The steps involved are:

* Reads the Incremental Sales dataset.
* Displays the incremental records.
* Merges the incremental data into the Delta table based on matching conditions.

.. figure:: ../../_assets/user-guide/read-write/merge-delta/merge-write-wf.png
   :alt: merge-write-wf
   :width: 60%

Reads Incremental Sales Dataset
---------------------

This step reads the incremental sales data from a source file.

Processor configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/merge-delta/read-incremental-dataset.png
   :alt: read-incremental-dataset
   :width: 60%
   
Processor output
^^^^^^

.. figure:: ../../_assets/user-guide/read-write/merge-delta/display-incremental-output.png
   :alt: display-incremental-output
   :width: 60%

Merge Data into Delta Table
----------------

This step merges the incremental data into the Delta table using the merge operation, applying conditions for updates, deletions, or insertions.

Processor configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/merge-delta/merge-delta-general.png
   :alt: merge-delta-general
   :width: 60%

.. figure:: ../../_assets/user-guide/read-write/merge-delta/merge-delta-update.png
   :alt: merge-delta-update
   :width: 60%

.. figure:: ../../_assets/user-guide/read-write/merge-delta/merge-delta-insert.png
   :alt: merge-delta-insert
   :width: 60%

|

Once the workflow is executed successfully, the incremental data will be merged into the Delta table based on the defined conditions.

.. figure:: ../../_assets/user-guide/read-write/merge-delta/merge-delta-success.png
   :alt: merge-delta-success
   :width: 60%
