EMR Serverless Workflow Operator
====================================

This operator executes a Sparkflows workflow as a step inside an existing EMR Serverless application on Amazon Web Services(AWS). Adds a selected Sparkflows workflow as a job step to an EMR Serverless application and runs it. If no Application ID is provided in the node, it smartly inherits it from the previous **Create Application** node.

.. figure:: ../../../_assets/user-guide/pipeline/emr-serverless-nodes/execute-wf.png
   :alt: Pipeline
   :width: 60%

* **Task Name:** Enter a unique name of the task in the Airflow DAG.
* **Application ID:** Enter an Application ID.
* **Execution Role ARN:** The IAM role assumed by the job.
* **Spark Conf:** Add Spark Conf values in comma separated as key:value.
* **Jar:** Entry point for spark job.
* **Workflow ID:** Select a Workflow from the list to execute.
* **AWS Connection ID:** Enter AWS Connection ID to be used.
* **Parameters:** Enter Key and Values to be used in the workflow.
