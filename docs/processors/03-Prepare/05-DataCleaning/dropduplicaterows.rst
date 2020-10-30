DropDuplicateRows
=========== 

1>When user don't select any column, returns a new Dataset that contains only the unique rows from this Dataset. 2> Returns a new Dataset with duplicate rows removed, considering only the subset of columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDropDuplicateRows

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - colNames
        - Columns
        - Columns to be used in determining if any two rows are duplication. No columns indicate to use all the available columns.




