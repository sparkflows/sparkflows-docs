Decision
=========== 

It computes expressions to determine if the condition is met or not. Accordingly proceeds to the next step or stops here.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDecision

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
      * - inputCols
        - Columns
        - Columns
      * - functions
        - Function
        - Function to apply
      * - symbols
        - Symbol
        - Symbol to apply
      * - values
        - Values
        - Values


Details
-------


It computes expressions to determine if the condition is met or not. Accordingly proceeds to the next step or stops here.

If expression evaluates to true then incoming Dataframe is sent to the output node and it is executed otherwise execution terminates in this node.


Examples
-------


If Decision node is configured as below:

COLUMNS    |      FUNCTION        |    SYMBOL    |    VALUES 	
---------------------------------------------------------------
PRD_CD     |      COUNT_RECORDS   |    <         |    10

then if count of entries in [PRD_CD] is less then 10 then only incoming Dataframe would be sent to the output node for execution
otherwise execution stops at Decision node itself.
