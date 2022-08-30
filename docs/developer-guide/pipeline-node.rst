Pipeline Nodes
====================================

Fire Insights supports Pipelines. In a Pipeline various workflows and other components can be executed in the provided order.

In Fire Insights, Pipelines can run with or without Airflow. The nodes available in the Pipeline depend on whether Airflow is integrated or not.


A Pipeline can have the following node types:


*	``Workflow`` node can be added to a Pipeline to execute a Workflow. A ``Workflow`` node can be connected to another ``Workflow`` node thus forming a series of workflows that can be executed one after another.

.. note:: Workflow node is available only when Airflow Server is not configured.

Below are list of nodes available when ''Airflow'' is enabled.

*   ``Branch Python Operator`` node can be used to execute flow depends on return value from the previous task.
*   ``Bash Operator`` node can be used to executes the commands depends on selected trigger rule.
*   ``Python Operator`` node can be used to execute python code using python operator.
*   ``Add step to EMR cluster`` node can be used to add step to EMR cluster and execute the arguments as one command using command-runner.jar.
*   ``Create EMR cluster`` node can be used to creates a new EMR cluster by using details in configuration and pass the emr_id to next step.
*   ``Terminate EMR cluster`` node can be used to terminates previously started EMR cluster.
*   ``EMR Workflow`` node can be used to allow to user to add the workflow in project to emr step to execute.
*   ``Empty Operator`` node can be used to creates Empty Operator.
*   ``XMLMapping`` node can be used as Lego Block: Execute Mapping Language Pipeline (a wrapper around Mapping Language Engine).
*   ``XMLParser`` node can be used as Lego Block: Execute Generic XML Parser (a wrapper around Spark XML).
*   ``EMR Step Sensor operator`` node will periodically check if that last added steps in EMR is completed or skipped or terminated.
*   ``S3 sensor`` node supports airflow s3_key_sensor operations.
*   ``Trigger next dag run``  node can be used to trigger other pipeline dag.

spark-submit-with-parameters
------------------------

Multiple spark-submit-with-parameters nodes can be added to Fire Insights by adding multiple JSON files.

Below is an example JSON for a spark-submit-with-parameters node which parses XML files.

```
JSON
```

