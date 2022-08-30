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

XMLParser
------------------------

XMLParser nodes can be added to Fire Insights by adding JSON files.

Below is an example JSON for a XMLParser node which parses XML files.

```
JSON
```

::

    {
  "id": "3",
  "name": "XMLParser",
  "description": "Lego Block: Execute Generic XML Parser (a wrapper around Spark XML)",
  "type": "legoblock",
  "nodeClass": "fire.pipelineNodes.XMLParser",
  "fields" : [
    {"name": "notes", "value":"", "widget": "textfield", "title": "Notes", "description": "Notes"},
    {"name": "Name", "value":"", "required":true, "widget": "textfield", "title": "Task Name", "description": "Name of the task in airflow dag and it should be unique in the dag."},
    {"name": "ClusterId", "value":"", "required":false, "widget": "textfield", "title": "Cluster Id", "description": "If Cluster Id is empty, step try to pick the cluster id from previous create emr node(task)." },

    {"name": "ActionOnFailure", "value":"CONTINUE", "required":true, "widget": "array", "optionsArray": ["CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER"], "title": "ActionOnFailure", "description": "Action On Failure" },

    {"name": "deploy-mode", "value":"client", "widget": "array", "optionsArray": ["client","cluster"], "title": "Deploy Mode", "description": "Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client)", "required": true},
    {"name": "jars", "value":"s3://fire-sample-data/health/jar/spark-xml_2.12-0.12.0.jar", "widget": "textfield", "title": "Jars", "description": "Comma separted jars path location", "required": true},
    {"name": "files", "value":"s3://fire-sample-data/change-health/log4j/log4j.properties", "widget": "textfield", "title": "Files", "description": "Comma-separated list of files to be placed in the working directory of each executor."},
    {"name": "conf", "value":"spark.dynamicAllocation.enabled=true", "widget": "textfield", "title": "Configuration", "description": "Arbitrary Spark configuration property in key=value format. Multiple configurations should be passed with comma separation. (e.g. <key>=<value>,<key2>=<value2>)"},
    {"name": "class", "value":"com.changehealthcare.ingestion.interop.pipeline.XmlReaderPipelineMain", "widget": "textfield", "title": "Class", "description": "The entry point for your application (e.g. org.apache.spark.examples.SparkPi)", "required": true},
    {"name": "applicationJar", "value":"s3://fire-sample-data/health/jar/generic-xmlparser_2.12-EMR-6.2_3.0.0-SNAPSHOT-assembly.jar", "widget": "textfield", "title": "Application Jar", "description": "Path to a bundled jar including your application and all dependencies.", "required": true},
  
   {"name": "parameters", "value":"", "widget": "tab", "title": "Parameters"},
   
   {"name": "name", "value":"Ingestion-edi270", "widget": "textfield", "title": "Name", "description": ""},
   {"name": "inputBasePath", "value":"hdfs:///interoperability/valid/270", "widget": "textfield", "title": "InputBasePath", "description": ""},
   {"name": "sourceBasePath", "value":"s3://fire-sample-data/health/input ", "widget": "textfield", "title": "SourceBasePath", "description": ""},
   {"name": "inputPathOrder", "value":"version,year,month,day,hour", "widget": "textfield", "title": "InputPathOrder", "description": ""},
   {"name": "outputBasePath", "value":"s3://fire-sample-data/health/outputIngestion", "widget": "textfield", "title": "OutputBasePath", "description": ""},
   {"name": "validateXML", "value":"true", "widget": "textfield", "title": "ValidateXML", "description": ""},
   {"name": "processPartialInput", "value":"true", "widget": "textfield", "title": "ProcessPartialInput", "description": ""},
   {"name": "RootTag", "value":"X12", "widget": "textfield", "title": "RootTag", "description": ""},
   {"name": "RowTag", "value":"TS_270", "widget": "textfield", "title": "RowTag", "description": ""},
   {"name": "version", "value":"1-2", "widget": "textfield", "title": "Version", "description": ""},
   {"name": "year", "value":"2022", "widget": "textfield", "title": "Year", "description": ""},
   {"name": "month", "value":"03", "widget": "textfield", "title": "Month", "description": ""},
   {"name": "day", "value":"30", "widget": "textfield", "title": "Day", "description": ""},
   {"name": "hour", "value":"04", "widget": "textfield", "title": "Hour", "description": ""}
	
  ]
  }
