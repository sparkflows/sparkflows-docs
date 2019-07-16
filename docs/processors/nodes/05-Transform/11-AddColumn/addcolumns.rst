AddColumns
=========== 

This node allows adding new columns with certain values

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node adds the user specified columns to the DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeAddColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - addCurrentDateCol
        - Add Current Date Column
        - Whether to add the current date as a new column
      * - currentDateColName
        - Current Date Column Name
        - Name of the new Current Date Column Created
      * - addCurrentTimeCol
        - Add Current Time Column
        - Whether to add the current time as a new column
      * - currentTimeColName
        - Current Time Column Name
        - Name of the new Current Time Column Created
      * - addConstantStringCol1
        - Add Constant String Column
        - Whether to add a new columns with constant string value
      * - constantStringColName1
        - Constant String Column Name
        - Constant String Name
      * - constantStringColValue1
        - Constant String Column Value
        - Constant String Value
      * - addConstantIntCol1
        - Add Constant Integer Column
        - Whether to add a new columns with constant integer value
      * - constantIntColName1
        - Constant Integer Column Name
        - Constant Integer Column Name
      * - constantIntColValue1
        - Constant Integer Column Value
        - Constant Integer Value




