Pipeline Nodes
====================================

Sparkflows supports Pipelines. In a Pipeline various workflows and other components can be executed in the provided order.

In Sparkflows, Pipelines can run with or without Airflow. The nodes available in the Pipeline depend on whether Airflow is integrated or not.


A Pipeline can have the following node types:


*	``Workflow`` node can be added to a Pipeline to execute a Workflow. A ``Workflow`` node can be connected to another ``Workflow`` node thus forming a series of workflows that can be executed one after another.

.. note:: Workflow node is available only when Airflow Server is not configured.

Below are list of nodes available when ''Airflow'' is enabled in Sparkflows by default.

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


Create EMR cluster
----------

Create EMR cluster node can be used to creates a new EMR cluster by using details in configuration and pass the emr_id to next step.

Below is an example JSON for a Create EMR cluster node.

```
JSON
```

::

    {
  "id": "6",
  "name": "Create EMR cluster",
  "description": "This node creates a new EMR cluster by using details in configuration and pass the emr_id to next step..",
  "type": "emr",
  "nodeClass": "fire.pipelineNodes.EMR",
  "fields" : [

    {"name": "notes", "value":"", "widget": "textfield", "title": "Notes", "description": "Notes"},


    {"name": "Name", "value":"", "required":true, "widget": "textfield", "title": "Task Name", "description": "Name of the task in airflow dag and it's should unique in the dag." },
	{"name": "ReleaseLabel", "value":"emr-6.2.0", "required":true, "widget": "textfield", "title": "Release Label", "description": "ReleaseLabel like emr-6.2.0 ,emr-6.2.1, emr-6.3.0 etc" },
    {"name": "LogUri", "value":"s3://aws-logs-us-east-1/elasticmapreduce/", "required":true, "widget": "textfield", "title": "Log Uri", "description": "LogUri Path" },
	{"name": "Applications", "value":"Spark", "required":true, "widget": "textfield", "title": "Applications", "description": "Applications Name is Spark" },
	{"name": "JobFlowRole", "value":"EMR_EC2_DefaultRole", "required":true, "widget": "textfield", "title": "JobFlow Role", "description": "The IAM role that was specified when the job flow was launched. The EC2 instances of the job flow assume this role." },
	{"name": "ServiceRole", "value":"EMR_DefaultRole", "required":true, "widget": "textfield", "title": "Service Role", "description": "The IAM role that is assumed by the Amazon EMR service to access Amazon Web Services resources on your behalf." },
	{"name": "KeepJobFlowAliveWhenNoSteps", "value":"False", "required":true, "widget": "array", "optionsArray": ["True","False"],"title": "Keep JobFlow Alive When No Steps", "description": "Specifies whether the cluster should remain available after completing all steps. Defaults to true." },
	{"name": "TerminationProtected", "value":"False", "required":true, "widget": "array", "optionsArray": ["True","False"], "title": "Termination Protected", "description": "Indicates whether Amazon EMR will lock the cluster to prevent the EC2 instances from being terminated by an API call or user intervention, or in the event of a cluster error." },
	{"name": "EmrManagedMasterSecurityGroup", "value":"", "required":true, "widget": "textfield", "title": "Emr Managed Master SecurityGroup", "description": "Parameter to specify a custom managed security group for the master instance." },
	{"name": "EmrManagedSlaveSecurityGroup", "value":"", "required":true, "widget": "textfield", "title": "Emr Managed Slave SecurityGroup", "description": "Parameter to specify a custom managed security group for core and task instances." },
	{"name": "InstanceGroups", "value":"[]", "required":true, "widget": "variablesList", "optionsArray": ["Name","InstanceRole","InstanceType","InstanceCount"], "title": "InstanceGroups", "description": "InstanceRole: Instance group role in the cluster, InstanceType: EC2 instance type, InstanceCount:Actual count of running instances.." }


  ]
  }





XMLParser
------------------------

XMLParser nodes can be added to Sparkflows by adding JSON files.

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
    {"name": "files", "value":"s3://fire-sample-data/health/log4j/log4j.properties", "widget": "textfield", "title": "Files", "description": "Comma-separated list of files to be placed in the working directory of each executor."},
    {"name": "conf", "value":"spark.dynamicAllocation.enabled=true", "widget": "textfield", "title": "Configuration", "description": "Arbitrary Spark configuration property in key=value format. Multiple configurations should be passed with comma separation. (e.g. <key>=<value>,<key2>=<value2>)"},
    {"name": "class", "value":"com.fire.ingestion.interop.pipeline.XmlReaderPipelineMain", "widget": "textfield", "title": "Class", "description": "The entry point for your application (e.g. org.apache.spark.examples.SparkPi)", "required": true},
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


XMLMapping
-----

XMLMapping node can be used as Lego Block: Execute Mapping Language Pipeline (a wrapper around Mapping Language Engine).

Below is an example JSON for a XMLMapping node which XML Mapping files.

```
JSON
```

::

    {
  "id": "3",
  "name": "XMLMapping",
  "description": "Lego Block: Execute Mapping Language Pipeline (a wrapper around Mapping Language Engine)",
  "type": "legoblock",
  "nodeClass": "fire.pipelineNodes.Mapping",
  "fields" : [ 
    {"name": "notes", "value":"", "widget": "textfield", "title": "Notes", "description": "Notes"},
    {"name": "Name", "value":"", "required":true, "widget": "textfield", "title": "Task Name", "description": "Name of the task in airflow dag and it should be unique in the dag."},
    {"name": "ClusterId", "value":"", "required":false, "widget": "textfield", "title": "Cluster Id", "description": "If Cluster Id is empty, step try to pick the cluster id from previous create emr node(task)." },

    {"name": "ActionOnFailure", "value":"CONTINUE", "required":true, "widget": "array", "optionsArray": ["CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER"], "title": "ActionOnFailure", "description": "Action On Failure" },

    {"name": "deploy-mode", "value":"client", "widget": "array", "optionsArray": ["client","cluster"], "title": "Deploy Mode", "description": "Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client)", "required": true},
    {"name": "files", "value":"s3://fire-sample-data/health/log4j/log4j.properties", "widget": "textfield", "title": "Files", "description": "Comma-separated list of files to be placed in the working directory of each executor."},
    {"name": "conf", "value":"spark.dynamicAllocation.enabled=true", "widget": "textfield", "title": "Configuration", "description": "Arbitrary Spark configuration property in key=value format. Multiple configurations should be passed with comma separation. (e.g. <key>=<value>,<key2>=<value2>)"},
    {"name": "class", "value":"com.fire.ingestion.mappinglanguage.pipeline.pipeline.PipelineMain", "widget": "textfield", "title": "Class", "description": "The entry point for your application (e.g. org.apache.spark.examples.SparkPi)", "required": true},
    {"name": "applicationJar", "value":"s3://fire-sample-data/health/jar/ihdp-mapping-language-pipeline_2.12-EMR-6.2_3.7.0-SNAPSHOT-assembly.jar", "widget": "textfield", "title": "Application Jar", "description": "Path to a bundled jar including your application and all dependencies.", "required": true},
  
   {"name": "parameters", "value":"", "widget": "tab", "title": "Parameters"},
   
   {"name": "name", "value":"270ToNDM", "widget": "textfield", "title": "Name", "description": ""},
   {"name": "spark.transform", "value":"270", "widget": "textfield", "title": "SparkTransform", "description": ""},
   {"name": "dataSource.type", "value":"system ", "widget": "textfield", "title": "DataSourceType", "description": ""},
   {"name": "inputBasePath", "value":"s3://fire-sample-data/health/outputIngestion", "widget": "textfield", "title": "InputBasePath", "description": ""},
   {"name": "inputPathOrder", "value":"version,year,month,day,hour", "widget": "textfield", "title": "InputPathOrder", "description": ""},
   {"name": "outputBasePath", "value":"s3://fire-sample-data/health/outputEngine", "widget": "textfield", "title": "OutputBasePath", "description": ""},
   {"name": "outputPathOrder", "value":"version,year,month,day,hour", "widget": "textfield", "title": "OutputPathOrder", "description": ""},
   {"name": "version", "value":"1-2", "widget": "textfield", "title": "Version", "description": ""},
   {"name": "year", "value":"2022", "widget": "textfield", "title": "Year", "description": ""},
   {"name": "month", "value":"03", "widget": "textfield", "title": "Month", "description": ""},
   {"name": "day", "value":"30", "widget": "textfield", "title": "Day", "description": ""},
   {"name": "hour", "value":"04", "widget": "textfield", "title": "Hour", "description": ""},
    {"name": "enableTransformPipelineFeature", "value":"true", "widget": "textfield", "title": "Enable Transform Pipeline Feature", "description": ""}
    
  ]
  }
