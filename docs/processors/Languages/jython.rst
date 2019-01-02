Jython
=========== 

This node runs any given Jython code. The input dataframe is passed in the variable inDF. The output dataframe should be placed in the variable outDF

Input
--------------
The input dataframe is passed in the variable in DF

Output
--------------
The output dataframe should be placed in the variable outDF

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeJython

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - tempTable
        - Temp Table
        - Temp Table Name to be used
      * - code
        - Jython
        - Python code to be run. Input dataframe is in inDF. Output dataframe is in outDF.
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
======


This node runs any given Jython code.

Below is an example jython code. It takes the input dataframe 'inDF', and returns the new dataframe 'outDF'


outDF = inDF.groupBy("c2").count()


