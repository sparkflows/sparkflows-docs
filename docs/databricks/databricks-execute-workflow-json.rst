Executing workflow without Fire Insights
==================

The workflows created in Fire Insights can be executed on Databricks without having Fire Insights installation available.

Below are the high level steps for it:

  * Export the workflow from Fire Insights as JSON file.
  * Uplod the workflow JSON to DBFS.
  * Upload the Fire Insights libraries into the Databricks Cluster.
  * Create a Notebook
  * Execute the Notebook.
  


Export and Upload the workflow JSON to DBFS
----------

As the first step, export the workflow as JSON files and upload to a DBFS folder.

The workflow might be a pyspark workflow or a scala workflow.

Running Scala Workflows
---------------

Upload the needed library:

  * Upload fire-x.y.z/fire-core-lib/fire-spark_2_4-core-3.1.0-jar-with-dependencies.jar to Databricks. Upload it under Workspace as a Library on to Databricks.

Run the workflow:

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
    val programParameters = dbutils.widgets.get("programParameters")
    
::

    # Import the WorkflowExecuteDatabricks, Create the array of input parametrs with postback-url, job-id, workflow-json-path, debug-mode. Exeute the workflow, by calling main function.
    
    import fire.execute.WorkflowExecuteDatabricks
    val args: Array[String] = Array(webserverURL, jobId, workflowJsonPath, "true")
    WorkflowExecuteDatabricks.main(args)

Running Pyspark Workflows
----------

Upload the needed files and libraries:

  * Upload fire-x.y.z/dist/fire-3.1.0-py3-none-any.whl to Databricks. Upload it under Workspace as a Library on to Databricks under DBFS or even in S3 Bucket which is accessible from the Databricks Cluster.
    
Run the workflow:

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
    
 
 
.. note::  Make sure to verify if workflow json path in dbfs is accessible and above Notebook is attached to Databricks Cluster with required library
