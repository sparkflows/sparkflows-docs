Drop Duplicate Rows
=========== 

Drops duplicate rows from the incoming DataFrame. Specific columns can be selected to be used when comparing two rows

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


Details
-------


Drops duplicate rows from the incoming DataFrame. Specific columns can be selected to be used when comparing two rows.


