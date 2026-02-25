Logs for Job Metrics
=======================================

This document outlines how to search for and view overall job metrics in the server logs after a Spark workflow execution in Sparkflows.

The job-level metrics are logged when a Spark workflow completes successfully.

The logs include execution identifiers such as:

- AnalysisFlowExecutionId
- AnalysisFlowId
- PipelineExecutionId
- Pipeline


View the Metrics in Logs
---------------------------
To view the metrics in logs, follow the steps below:

**Step 1:** Navigate to the **Administration** tab from the top menu and search for **View Server Logs** card and click on it.

.. figure:: ../../_assets/configuration/logs/view-server-logs-card.png
   :alt: Logs
   :width: 40%


**Step 2:** In the search bar at the top, search for ``[JobExecutionMetrics]``. This will display the overall metrics related to a particular workflow.


- If the workflow has been run through the pipeline, it will be shown as below.




- If the workflow has been run without a pipeline, the metrics will be shown as below.




.. note:: If the workflow fails, job metrics will not be available - neither in the UI nor in the logs.
