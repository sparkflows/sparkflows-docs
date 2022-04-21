Math Expression
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMathExpression

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCols
        - OutPut Column
        - Output Column Name
      * - expressions
        - Math Expression
        - Define math expression.


Details
-------


This node creates a new DataFrame by adding new column to the incoming Dataframe as per the experssion computation.

New column can be computed using existing columns in the Dataframe.


Examples
-------


Incoming Dataframe has following rows:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT
--------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0
P03       |    HAMMER            |    100.0         |    10.0       |    5.0

if MathExpression node is configured to compute a new column [NET_AMT] based on expression [LIST_PRICE + TAX_AMT - DISCOUNT] 
then outgoing Dataframe would be created as below with new column added:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT    |    NET_AMT    
------------------------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0        |    1050.0
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0       |    1550.0
P03       |    HAMMER            |    100.0         |    10.0       |    5.0         |    105.0
