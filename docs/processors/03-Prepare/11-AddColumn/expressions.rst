Expressions
=========== 

Expressions

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeExpressions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - description
        - Description
        - Description
      * - outputCols
        - New Columns Name
        - New Columns Name
      * - expressions
        - Expressions
        - Expressions


Details
-------


This node creates a new DataFrame by adding new columns to the incoming Dataframe as per the experssion computation.

New column can be computed using existing columns in the Dataframe.


Examples
-------


Incoming Dataframe has following rows:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT
--------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0
P03       |    HAMMER            |    100.0         |    10.0       |    5.0

if Expression node is configured to compute new columns as below:

NEW COLUMNS NAME         |    EXPRESSIONS 	
-----------------------------------------------------------------
NET_AMT                  |    LIST_PRICE + TAX_AMT - DISCOUNT
PRD_DETAILS              |    CONCAT(PRD_CD,':',PRD_NAME)

then outgoing Dataframe would be created as below with new columns added:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT    |    NET_AMT    |    PRD_DETAILS
--------------------------------------------------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0        |    1050.0     |    P01:DRILL MACHINE
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0       |    1550.0     |    P02:WEIGHING MACHINE
P03       |    HAMMER            |    100.0         |    10.0       |    5.0         |    105.0      |    P03:HAMMER
