Remove Duplicate Rows
=========== 

This node take an array of fields and compare the rows on those fields. From the matches it would randomly take one row and drop the rest.

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
The output Dataframe is the same as the input Dataframe with the duplicate rows removed

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRemoveDuplicateRows

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - order
        - Order
        - Whether to take the first or last matching record when removing duplicates
      * - inputCols
        - Columns
        - The columns to be selected for match


Details
-------


This node drops duplicate rows from the incoming DataFrame. 

Specific columns can be selected to be used when comparing two rows.

One of the matching rows either first or last one is included in the outgoing Dataframe based on selection .


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

 If RemoveDuplicateRows node is configured to retain first matching row and drop other duplicate rows having duplicate values in [EMP_NAME] and [DEPT]  
+++++++++++++++
then outgoing dataframe would be created as below:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E01       |    DAVID       |    HR         |    25
E02       |    JOHN        |    SALES      |    35
E03       |    JOHN        |    MARKETING  |    40

 If RemoveDuplicateRows node is configured to retain last matching row and drop other duplicate rows having duplicate values in [EMP_NAME] and [DEPT]  
+++++++++++++++
then outgoing dataframe would be created as below:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E05       |    DAVID       |    HR         |    25
E02       |    JOHN        |    SALES      |    35
E04       |    JOHN        |    MARKETING  |    45

 If RemoveDuplicateRows node is configured to retain first matching row and drop other duplicate rows having duplicate values in [EMP_NAME], [DEPT] and [AGE]  
+++++++++++++++
then outgoing dataframe would be created as below:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E01       |    DAVID       |    HR         |    25
E02       |    JOHN        |    SALES      |    35
E03       |    JOHN        |    MARKETING  |    40
E04       |    JOHN        |    MARKETING  |    45
