StructuredStreamingCSV
=========== 

It monitors a specified directory for new files. It keeps reading in any new files created in the directory.

Input
--------------
It does not take any DataFrame as input

Output
--------------
It reads the new files and creates DataFrame from the content of the text files. This DataFrame is passed to the output Nodes.

Type
--------- 

sparkstreaming

Class
--------- 

fire.nodes.structuredstreaming.NodeStructuredStreamingCSV

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - path
        - Path
        - Path of the Text file/directory
      * - separator
        - Separator
        - CSV Separator
      * - outputColNames
        - Column Names for the CSV
        - Output Column Names
      * - outputColTypes
        - Column Types for the CSV
        - Output Column Types
      * - outputColFormats
        - Column Formats for the CSV
        - Output Column Formats




