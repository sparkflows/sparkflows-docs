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


This node drops duplicate rows from the incoming DataFrame. 

Specific columns can be selected to be used when comparing two rows.

One of the matching rows is included in the outgoing Dataframe.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E01       |    DAVID       |    HR         |    25
E05       |    DAVID       |    HR         |    25
E02       |    JOHN        |    SALES      |    35
E03       |    JOHN        |    MARKETING  |    40
E04       |    JOHN        |    MARKETING  |    45

 If DropDuplicateRows node is configured to drop duplicate rows having duplicate values in [EMP_NAME] and [DEPT] then outgoing dataframe would be created as below:
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E02       |    JOHN        |    SALES      |    35
E01       |    DAVID       |    HR         |    25
E03       |    JOHN        |    MARKETING  |    40

 If DropDuplicateRows node is configured to drop duplicate rows having duplicate values in [EMP_NAME], [DEPT] and [AGE] then outgoing dataframe would be created as below:
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E01       |    DAVID       |    HR         |    25
E02       |    JOHN        |    SALES      |    35
E03       |    JOHN        |    MARKETING  |    40
E04       |    JOHN        |    MARKETING  |    45
