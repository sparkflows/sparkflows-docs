Pipe Python2
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

fire.nodes.etl.NodePipePython2

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - codeHeader
        - Pipe Header Code
        - Header part of the Python code to be run. It receives each record as a string
      * - codeBody
        - Pipe Body Code
        - Body part of the Python code to be run.
      * - codeFooter
        - Pipe Footer Code
        - Footer part of the Python code to be run. It should write out each resulting record back as a string.
      * - outputColNames
        - Output Column Names
        - Output Schema of Pipe Python Processor
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns




