Database Clean up
================

Sparkflows provides methods to cleanup the database tables used to store the metadata about the workflow-execution, pipeline-execution and their results.

Manual Cleanup
--------------

**To Access Database Cleanup Data**

Login to ``Sparkflows`` application -> ``Administration`` -> ``Cleanup Data``

Past workflow and pipeline executions can be cleaned up manually on demand.

Clean up workflow executions:

By selecting the ``Older than 90 days`` button, the user can delete workflow executions from the database that are older than the specified number of days

  .. figure:: ../../_assets/DB_cleanup/workflow_execution_cleanup.png
     :alt: workflow execution cleanup
     :width: 60%

