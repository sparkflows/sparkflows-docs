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




