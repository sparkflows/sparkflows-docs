Executing workflow without Sparkflows
==================

The workflows created in Sparkflows can be executed on Databricks without having Sparkflows installation available.

Architecture diagram
----------

.. figure:: ..//_assets/databricks/WorkflowExecution.png
   :alt: databricks
   :width: 60%


Below are the high level steps for it:

  * Export the workflow from Sparkflows as JSON file.
  * Uplod the workflow JSON to DBFS.
  * Upload the Sparkflows libraries into the Databricks Cluster.
  * Create a Notebook and attach it to Databricks Cluster which have Sparkflows Library installed.
  * Execute the Notebook.
  


Export and Upload the workflow JSON to DBFS
----------

As the first step, export the workflow as JSON files and upload to a DBFS folder.

The workflow might be a spark/scala workflow or a pyspark workflow.

Running Scala Workflows
---------------

Upload the fire core jar
++++++++++++++++++++++


  * Upload ``fire-x.y.z/fire-core-lib/fire-spark_2_4-core-3.1.0-jar-with-dependencies.jar`` to Databricks. Upload it under Workspace as a Library on to Databricks.

Create a Notebook in Databricks
++++++++++++

Suppose the workflow json is available at ``dbfs:/workflows/test_csv_scala.json``

In order to execute it, create a Notebook with the below code::

    # Create Input Parameters
    
    dbutils.widgets.text("job-id", "100")
    dbutils.widgets.text("postback-url", "")
    dbutils.widgets.text("workflowJsonPath", "dbfs:/workflows/test_csv_scala.json")
    dbutils.widgets.text("programParameters", "")
    
::

    # Get the values of Input Parameters
    
    val jobId = dbutils.widgets.get("job-id")
    val webserverURL = dbutils.widgets.get("postback-url")
    val workflowJsonPath = dbutils.widgets.get("workflowJsonPath")
    var programParameters = dbutils.widgets.get("programParameters")
    val debug = "false"
    val username = ""

::

    # Adding the scope, user, password and url of secrets to parameter, if any.
    
    programParameters = programParameters.trim + " --var databricks_scope=db_secrets_scope --var sf_user_key=sfUser --var sf_password_key=sfPassword --var sf_url_key=sfUrl"
    
    
::

    # Read the workflow json.
    
    import org.apache.commons.lang3.StringEscapeUtils
    val workflowjson = spark.read.textFile(workflowJsonPath).take(1)(0)

::

    # Execute the workflow.
    
    import fire.execute.WorkflowExecuteDatabricks
    WorkflowExecuteDatabricks.execute(webserverURL, jobId, workflowjson, debug, username, programParameters.trim)
    

Create the Spark Job in Databricks
++++++++++++++++

Create the Spark Job by attaching the notebook template with input parameters like workflow-json-path etc.

Submit the Spark Job to Databricks Cluster
++++++++++++++++

Submit the Spark Job to Databricks Cluster by passing the required workflow json path.


Running Pyspark Workflows
----------

Upload fire wheel file to DBFS
++++++++++++++

  * Upload ``fire-x.y.z/dist/fire-3.1.0-py3-none-any.whl`` to Databricks. Upload it under Workspace as a Library on to Databricks under DBFS or even in S3 Bucket which is accessible from the Databricks Cluster.
    
Create a Notebook
++++++++++++

Suppose the workflow json is available at ``dbfs:/workflows/Join_Workflow.json``

In order to execute it, create a Notebook with the below code::

    # Create Input Parameters
    
    dbutils.widgets.text("job-id", "100")
    dbutils.widgets.text("postback-url", "")
    dbutils.widgets.text("workflowJsonPath", "dbfs:/workflows/Join_Workflow.json")
    dbutils.widgets.text("programParameters", "")
    
::

    # Get the values of Input Parameters
    
    jobId = dbutils.widgets.get("job-id")
    webserverURL = dbutils.widgets.get("postback-url")
    workflowJsonPath = dbutils.widgets.get("workflowJsonPath")
    programParameters = dbutils.widgets.get("programParameters")
    
::

    # Print the Input Parameters
    
    print("jobId: "+jobId)
    print("webserverURL: "+webserverURL)
    print("workflowJsonPath: "+workflowJsonPath)
    print("programParameters: "+programParameters)

::

    # Import the WorkflowExecuteDatabricks and call the execute method by passing parmaters.
    
    from fire.databricks.workflow_execute import WorkflowExecuteDatabricks
    debug = False
    username = ""
    WorkflowExecuteDatabricks.execute(webserverURL = webserverURL, jobId = jobId, 
                                      workflowJsonPath = workflowJsonPath, debug = debug, username = username,
                                      program_parameters = programParameters)
    
 
Create the Pyspark Job in Databricks
++++++++++++++++

Create the Pyspark Job by attaching the notebook template with input parameters like workflow-json-path etc.

Submit the Pyspark Job to Databricks Cluster
++++++++++++++++

Submit the Pyspark Job to Databricks Cluster by passing the required workflow json path.
 
 
.. note::  Make sure to verify if workflow json path in dbfs is accessible and above Notebook is attached to Databricks Cluster with required Sparkflows library
