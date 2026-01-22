Sparkflows Workflow Execution via Command Line
=============================================

The following commands explain how to execute a Sparkflows workflow JSON using the Java
command line.

Main Class
----------

``fire.execute.WorkflowExecuteInIncorta``

Execute Workflow and Retrieve a Single Output DataFrame
------------------------------------------------------

Use the method below to execute a Sparkflows workflow and retrieve the output DataFrame
from the last node in the workflow.

::

   WorkflowExecuteInIncorta.executeWF(
       String workflowJson,
       SparkSession spark,
       String parameters,
       String jwtConfig
   )

**Parameters**
+++++++++++++++

- ``workflowJson`` - Sparkflows workflow JSON string
- ``spark`` - SparkSession instance
- ``parameters`` - Runtime parameters passed using ``--var name=value`` format
- ``jwtConfig`` - JWT token used for Box integration in ReadExcelAdvanced and
  SaveExcelAdvanced nodes

**Example**
+++++++++++++++++

.. code-block:: scala

   val workflowJsonUI: String = "ADD THE WORKFLOW JSON"
   val parameters: String =
     "--var inputPath=Example.xlsx " +
     "--var sheetName=0.1 - H-Master " +
     "--var startDataImportRow=8 " +
     "--var customHeaderRow=7 " +
     "--var workflow_1_HeaderHandlingMode=CUSTOM_ROW"

   val token: String = ""
   val data =
     WorkflowExecuteInIncorta.executeWF(
       workflowJsonUI,
       spark,
       parameters,
       token
     )

Execute Workflow with Input and Output DataFrame Mapping
-------------------------------------------------------

Use this method to:

- Pass input DataFrames mapped to schema.table names used in ReadIncorta nodes
- Retrieve output DataFrames mapped to schema.table names defined in SaveIncorta nodes

::

   WorkflowExecuteInIncorta.executeWF(
       workflowJsonUI,
       spark,
       parameters,
       token,
       inputDataFrames
   )

**Parameters**
+++++++++++++++

- ``workflowJson`` – Sparkflows workflow JSON string
- ``spark`` – SparkSession instance
- ``parameters`` – Runtime parameters passed using ``--var name=value`` format
- ``jwtConfig`` – JWT token used for Box integration in ReadExcelAdvanced and
  SaveExcelAdvanced nodes
- ``inputDataFrames`` – Map of schema.table (key) to inputdataframes (value)

InputDataframe is used instead of ReadIncorta Node.  
It returns the Map of schema.table (key) to outputdataframes (value).  
Returns the dataframes instead of SaveIncorta.

**Example**
+++++++++++++++++

.. code-block:: scala

   import java.util.HashMap
   import org.apache.spark.sql.{Dataset, Row}

   val workflowJsonUI: String = "ADD THE WORKFLOW JSON"

   // Create input dataFrames
   val tempDF = spark.emptyDataFrame
   val inputDataFrames = new HashMap[String, Dataset[Row]]()
   inputDataFrames.put("TEST_SCHEMA.TEST_TABLE", tempDF)

   val parameters: String = ""
   val token: String = ""

   // Execute workflow
   val outputDataFrames =
     WorkflowExecuteInIncorta.executeWF(
       workflowJsonUI,
       spark,
       parameters,
       token,
       inputDataFrames
     )

   // Retrieve output DataFrames
   val output1DF = outputDataFrames.get("TEST_SCHEMA.OUTPUT1")
   val output2DF = outputDataFrames.get("TEST_SCHEMA.OUTPUT2")
