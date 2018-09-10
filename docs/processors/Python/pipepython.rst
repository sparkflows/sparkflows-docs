Pipe Python
=========== 

This node runs any given Python code. The input dataframe is passed in the variable inDF. The output dataframe should be placed in the variable outDF

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

fire.nodes.etl.NodePipePython

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - code
        - Pipe Python
        - Python code to be run. It receives each record as a string and outputs records back as a string.
      * - outputColNames
        - Output Column Names
        - Output Schema of Pipe Python Processor
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns




