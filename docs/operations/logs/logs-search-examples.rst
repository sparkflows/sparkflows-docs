Logs Search Examples
----------

This page documents ways to search for some common scenarios.

Logs for Workflow Execution
+++++++

Use the workflow execution Job ID to search for logs for a specific workflow execution.

You can also search the logs using the workflow execution Id.

::

    2024-10-14 09:05:23,238 [clientInboundChannel-10] "fire-1" INFO fireui.alert.AnalysisFlowExecutionStatusUtil [314] Changing Analysis Flow Execution Id: 314 Status : 3 : 
    new status : FAILED
    2024-10-14 09:05:23,244 [clientInboundChannel-10] "fire-1" INFO fireui.alert.AnalysisFlowExecutionStatusUtil [314] Start Time : 2024-10-14 03:35:21 UTC
    2024-10-14 09:05:23,252 [clientInboundChannel-10] "fire-1" INFO fireui.alert.AnalysisFlowExecutionStatusUtil [314] End Time : 2024-10-14 03:35:21 UTC
    2024-10-14 09:05:23,259 [clientInboundChannel-10] "fire-1" INFO fireui.workflowexecute.BrowserWorkflowContext [314] workflowExecutionId: 314
    2024-10-14 09:05:23,270 [clientInboundChannel-10] "fire-1" INFO fireui.alert.AnalysisFlowExecutionStatusUtil [314] Changing Analysis Flow Execution Id: 314 Status : 3 : 
    new status : FAILED
    2024-10-14 09:05:23,277 [clientInboundChannel-10] "fire-1" INFO fireui.alert.AnalysisFlowExecutionStatusUtil [314] Start Time : 2024-10-14 03:35:21 UTC
    2024-10-14 09:05:23,277 [clientInboundChannel-10] "fire-1" INFO fireui.alert.AnalysisFlowExecutionStatusUtil [314] End Time : 2024-10-14 03:35:21 UTC

Logs for Pipeline Execution
++++++

Use the pipeline execution ID in order to serach for log for a specific pipeline execution.



