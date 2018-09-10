SaveAsHIVETable
=========== 

Saves the DataFrame into a HIVE Table

Type
--------- 

transform

Class
--------- 

fire.nodes.save.NodeSaveAsTable

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      :stub-columns: 1

      * - Name
        - Title
        - Description
      * - database
        - HIVE Database
        - Name of the HIVE Database
      * - table
        - HIVE Table
        - Name of the HIVE table
      * - partitionBy
        - Partition By
        - List of columns to partition by - separated by space
      * - format
        - Format
        - File format when saving to HIVE Table
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the path Exists




