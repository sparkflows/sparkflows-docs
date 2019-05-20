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


WorkflowContext
---------------

WorkflowContext provides the following methods for outputting data to the user:

* def outStr(self, text: str):
* def outNameValue(self, nm: str, val: str):
* def outSchema(self, id: int, title: str, df: DataFrame):
* def outDataFrame(self, id: int, title: str, df: DataFrame):
* def outPandasDataframe(self, id: int, title: str, df: pd.DataFrame):
* def outndarray(self, id: int, title: str, df: np.ndarray):

