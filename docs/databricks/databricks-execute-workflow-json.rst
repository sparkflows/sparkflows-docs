Executing from workflow JSON
==================

The workflow in Fire Insights can be exported as JSON files.

These JSON files can be executed on the Databricks clusters directly. Fire Insights does not have to be necessarily available.

The below defines the steps for it.

Export and Upload the workflow JSON to DBFS
----------

As the first step, export the workflow as JSON files and upload to a DBFS folder.

The workflow might be a pyspark workflow or a scala workflow.

Running Scala Workflows
---------------

Upload the needed library:

  * Upload fire-x.y.z/fire-core-lib/fire-spark_2_3-core-3.1.0-jar-with-dependencies.jar to Databricks. Upload it under Workspace as a Library on to Databricks.

Suppose the workflow json is available at dbfs://FileStore/wf/wf_spark.json

In order to execute it, create a Notebook with the below code::

    ...

Running Pyspark Workflows
----------

Upload the needed files and libraries:

  * Upload fire-x.y.z/dist/fire-3.1.0-py3-none-any.whl to Databricks. Upload it under Workspace as a Library on to Databricks under DBFS or even in S3 Bucket which is accessible from the Databricks Cluster.
  * Upload fire-x.y.z/dist/workflowexecutedatabricks.py, file to DBFS.
  
Run the workflow:

Suppose the workflow json is available at dbfs://FileStore/wf/wf_pyspark.json

In order to execute it, create a Notebook with the below code::

    ...
    
    
    
