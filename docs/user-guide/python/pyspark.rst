PySpark
=======

Fire Insights provides a PySpark processor for writing PySpark/Python code.

Interface
---------

In the PySpark Processor, we have to implement the myfn function which gets invoked::

  def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame):

  * spark : SparkSession object
  * workflowContext : Can be used for outputting results to the user
  * id : id of the current processor
  * inDF : Input PySpark dataframe


WorkflowContext
---------------

WorkflowContext provides the following methods for outputting data to the user::

  * def outStr(self, text: str)
  * def outNameValue(self, nm: str, val: str)
  * def outSchema(self, id: int, title: str, df: DataFrame)
  * def outDataFrame(self, id: int, title: str, df: DataFrame)
  * def outPandasDataframe(self, id: int, title: str, df: pd.DataFrame)
  * def outndarray(self, id: int, title: str, df: np.ndarray)

Example
-------

Below is an example code for the PySpark Node.

.. code-block:: python
    :linenos:
   
    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *
    from workflowcontext import *

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame):
      house_type_udf = udf(lambda bedrooms: "big house" if int(bedrooms) >2 else "small house", StringType())
      filetr_df = inDF.select("id", "price", "lotsize", "bedrooms")
      outDF = filetr_df.withColumn("house_type", house_type_udf(filetr_df.bedrooms))
      return outDF
      
      
  
