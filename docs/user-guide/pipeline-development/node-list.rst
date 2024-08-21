Nodes
=========
This document outlines the various nodes that can be added to a Pipeline in Sparkflows.

Various nodes can be added to a Pipeline. Some of them are listed below:

*	**Workflow** node can be added to a Pipeline to execute a Workflow. A Workflow node can be connected to another Workflow node thus forming a series of workflows that can be executed one after another.

.. note:: Workflow node is available only when Airflow Server is not configured.

Below is a list of nodes available when **Airflow** is enabled:

*   **Branch Python Operator** node can be used to execute flow depending on the return value from the previous task.
*   **Bash Operator** node can be used to execute the commands depending on the selected trigger rule.
*   **Python Operator** node can be used to execute python code using python operator.
*   **Add step to EMR cluster** node can be used to add step to EMR cluster and execute the arguments as one command using `command-runner.jar`.
*   **Create EMR cluster** node can be used to create a new EMR cluster by using details in configuration and to pass the emr_id to next step.
*   **Terminate EMR cluster** node can be used to terminate a previously started EMR cluster.
*   **EMR Workflow** node can be used to allow the user to add the workflow in a project to an EMR step to execute.
*   **Empty Operator** node can be used to create an Empty Operator.
*   **XMLMapping** node can be used as Lego Block: Execute Mapping Language Pipeline (a wrapper around Mapping Language Engine).
*   **XMLParser** node can be used as Lego Block: Execute Generic XML Parser (a wrapper around Spark XML).
*   **EMR Step Sensor operator** node will Periodically check if the last added steps in EMR are completed, skipped, or terminated.
*   **S3 sensor** node supports Airflow `s3_key_sensor` operations.
*   **Trigger next dag run**  node can be used to trigger the next pipeline DAG.


Below is an example of a Pipeline with multiple Workflows.

.. figure:: ../_assets/user-guide/pipeline/create-pipeline-new.png
   :alt: Pipeline
   :width: 60%
   
