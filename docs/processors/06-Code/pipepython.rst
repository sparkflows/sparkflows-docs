PipePython
=========== 

This node runs any given Python code. It pipes the incoming DataFrame through pipe to the Python Script. Output back to Spark has to be written out using print.

Input
--------------
It pipes the incoming DataFrame through pipe to the Python Script. It also passes the Schema of the DataFrame to the Python script through the command line argument - argv[1]

Output
--------------
Output back to Spark has to be written out using print.

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




