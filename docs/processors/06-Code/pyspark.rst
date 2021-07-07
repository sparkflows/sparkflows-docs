PySpark
=========== 

This node runs any given PySpark code. The input dataframe is passed in the variable inDF. The output dataframe is passed back by registering it as a temporary table.

Input
--------------
The input dataframe is passed in the variable inDF.

Output
--------------
The output dataframe is passed back by registering it as a temporary table

Type
--------- 

pyspark

Class
--------- 

fire.nodes.etl.NodePySpark

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - code
        - PySpark
        - PySpark code to be run. Input dataframe : "inDF", SparkContext : "sc", SQLContext : "sqlContext",  Output/Result dataframe should be registered as a temporary table - df.registerTempTable("outDF")
      * - schema
        - Schema
      * - outputColNames
        - Column Names for the CSV
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the CSV
        - Data Type of the Output Columns
      * - outputColFormats
        - Column Formats for the CSV
        - Format of the Output Columns


Details
-------


This node receives receives an input pyspark dataframe in function called myfn.

Finally the pyspark/python code returns the pyspark daframe.


Examples
-------


Format Examples
+++++++++++++++

Input Schema: id, price, lotsize, bedrooms, bathrms, stories, driveway, recroom, fullbase, gashw, airco, garagepl, prefarea

 add the house_type column
```````````````

from pyspark.sql.types import StringType
from pyspark.sql.functions import *
from pyspark.sql import *
from fire.workflowcontext import *

def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
house_type_udf = udf(lambda bedrooms: "big house" if int(bedrooms) >2 else "small house", StringType())
filetr_df = inDF.select("id", "price", "lotsize", "bedrooms")
outDF = filetr_df.withColumn("house_type", house_type_udf(filetr_df.bedrooms))
return outDF

 using pandas dataframe
```````````````

from pyspark.sql.types import StringType
from pyspark.sql.functions import *
from pyspark.sql import *

from fire.workflowcontext import *

def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
# Convert the Spark DataFrame to a Pandas DataFrame
pdf = inDF.select("*").toPandas()

workflowContext.outStr(id, "Outputting Pandas Dataframe")
workflowContext.outPandasDataframe(id, "Pandas DataFrame", pdf, 10)

# Create a Spark DataFrame from a Pandas DataFrame
df = spark.createDataFrame(pdf)

return df

 numpy 2d array to pandas dataframe & pandas dataframe to spark dataframe
```````````````

from pyspark.sql.types import StringType
from pyspark.sql.functions import *
from pyspark.sql import *
import numpy as np
import pandas as pd

from fire.workflowcontext import *
def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
# Create the numpy 2d array
example_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Convert to Pandas Dataframe
pandas_dataframe = pd.DataFrame(example_array, columns=['a', 'b', 'c', 'd'])
# Convert Pandas Dataframe to Spark Dataframe
spark_dataframe = spark.createDataFrame(pandas_dataframe)
return spark_dataframe
