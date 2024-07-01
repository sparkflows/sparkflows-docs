Delta Merge
=========== 

Merge the input data into the target delta location with merge, insert and update conditions.

Type
--------- 

join2inputs

Class
--------- 

fire.nodes.delta.NodeDeltaMerge

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - deltaTargetPath
        - Path
        - Merge Target Path
      * - tempDeltaTargetName
        - TempDeltaTargetName
        - temp table name for target path and the name is used in merge, update & insert stmt.
      * - tempSourceName
        - TempSourceName
        - temp table name for target path and the name is used in merge, update & insert stmt.
      * - mergeStmt
        - MergeStmt
        - merge stmt
      * - updateStmt
        - UpdateStmt
        - update stmt
      * - insertStmt
        - InsertStmt
        - insert stmt




