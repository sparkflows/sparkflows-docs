String Functions
=========== 

This node performs the specified string function on the selected input columns of the incoming DataFrame

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringFunctions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Column Name
        - input column name
      * - stringFunction
        - String Function
        - String Function Name to be applied to the selected columns
      * - replaceExistingCols
        - ReplaceExistingCols
        - Whether to replace the existing columns or create new ones


Details
-------


This node creates a new Dataframe after transforming data of selected columns using specified string function.

In the output DataFrame, the input columns can either be replaced with the new value, or new columns created.


Examples
-------


Incoming Dataframe has following rows:

PRD_CD    |    PRD_NAME          
---------------------------------
P01       |    DRILL MACHINE     
P02       |    WEIGHING MACHINE  
P03       |    HAMMER            

if StringFunctions node is configured to add a new column as [PRD_NAME_LOWER] by applying [lower] function on [PRD_NAME] to convert [PRD_NAME] values in Lower Case
then outgoing Dataframe would be created as below after case conversion:

PRD_CD    |    PRD_NAME          |    PRD_NAME_UPPER
----------------------------------------------------------
P01       |    DRILL MACHINE     |    drill machine
P02       |    WEIGHING MACHINE  |    weighing machine
P03       |    HAMMER            |    hammer
