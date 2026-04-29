Retry Pipeline with Airflow
============================

The **Retry** option allows you to re-run a failed pipeline execution that was orchestrated through Airflow without triggering a brand-new DAG run. Instead of starting from scratch, Sparkflows asks Airflow to clear the failed task instances in the existing DAG run, so Airflow re-executes only the failed tasks (and their downstream dependencies) while preserving the work already completed by successful upstream tasks.

When is the Retry Option Available
-----------------------------------

The **Retry** icon appears on a pipeline execution row in the Pipeline Executions grid only when **both** of the following conditions are met:

#. The execution status is **FAILED**.
#. The execution was launched on an **Airflow** connection (an Airflow DAG run exists for it).

If either condition is not met (for example, the pipeline ran on Spark/Livy, or the execution succeeded or is still running), the Retry option will not be shown.

Steps to Retry a Failed Pipeline
---------------------------------

Step 1 : Navigate to Pipeline Executions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open the **Pipelines → Executions** tab to view the list of pipeline executions.

#. Identify the failed pipeline execution that you want to re-run.

   .. figure:: ../../_assets/user-guide/pipeline/retry_pipeline/pipeline_airflow_before_retry.png
      :alt: Pipeline Execution Before Retry
      :width: 80%

Step 2 : Click the Retry Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Retry** icon in the **Actions** column of the failed execution row.

#. Confirm the action when prompted.

   .. figure:: ../../_assets/user-guide/pipeline/retry_pipeline/pipeline_retry.png
      :alt: Retry Pipeline Execution
      :width: 80%

   On clicking Retry, Sparkflows will:

   * Call the Airflow REST API to **clear the failed task instances** in the corresponding DAG run.
   * Update the pipeline execution status back to **RUNNING** and clear its end time.
   * Reset all failed pipeline execution items to **QUEUED** so that their progress is tracked again as Airflow re-runs them.

Step 3 : Monitor the Retried Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Once retried, the pipeline execution status will change from **RUNNING** to **SUCCEEDED** or **FAILED** based on the outcome of the retried tasks.

   .. figure:: ../../_assets/user-guide/pipeline/retry_pipeline/pipeline_airflow_after_retry.png
      :alt: Pipeline Execution After Retry
      :width: 80%

What Gets Re-run
-----------------

* Only **failed tasks** (and any downstream tasks that depend on them) are re-executed.
* Successfully completed upstream tasks are **not** re-run; their outputs are reused.
* Pipeline parameters, connection, and DAG configuration from the original run are preserved.

Permissions
------------

The user invoking **Retry** must have **execute permission** on the pipeline (the same permission required to run the pipeline initially).
