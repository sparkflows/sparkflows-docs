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
        - Column Name
        - New Output Column Name
      * - outputColTypes
        - Column Type
        - Data Type of the Output Column
      * - outputColFormats
        - Column Format
        - Format of the Output Column


Details
-------


It reads in JSON files. Each JSON record has to be on a separate line for Spark to handle it correctly.

There cannot be line break within a record.


