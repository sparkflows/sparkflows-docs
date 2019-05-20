PySpark
=======

Fire Insights provides a PySpark processor for writing PySpark/Python code.

Interface
---------

It provides the following interface for writing the PySpark code:

def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame):

* spark : SparkSession object
* workflowContext : Can be used for outputting results to the user
* id : id of the current processor
* inDF : Input PySpark dataframe

