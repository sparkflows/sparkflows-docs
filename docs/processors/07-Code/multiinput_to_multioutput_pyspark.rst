MultiInputToMultiOutputPySpark
=========== 

This node runs any given PySpark code. The input dataframes is passed in the variable inDFs. The output array of dataframe is passed back by registering each dataframe as a temporary table.

Input
--------------
The input dataframes is passed in the variable inDFs.

Output
--------------
The output array of dataframes is passed back by registering each dataframe as a temporary table

Type
--------- 

pyspark2inputs

Class
--------- 

fire.nodes.code.NodeMultiInputToMultiOutputPySpark

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




