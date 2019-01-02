ReadJSON
=========== 

Dataset Node for reading JSON files

Type
--------- 

dataset

Class
--------- 

fire.nodes.dataset.NodeDatasetJSON

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
        - Path of the JSON file/directory
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


It reads in JSON files. Each JSON record has to be on a separate line for Spark to handle it correctly.

There cannot be line break within a record.


