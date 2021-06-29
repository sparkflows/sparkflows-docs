Time Functions
=========== 

This node extracts year, dayofmonth, dayofyear, weekofyear, dayofweek, quarter, hour, minute, second & season.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeTimeFunctions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - timeStampCol
        - TimeStamp Column Name
        - input column name
      * - timeFunctions
        - Time Functions
        - Time Functions Name


Details
-------


This node extracts year, dayofmonth, dayofyear, weekofyear, dayofweek, quarter, hour, minute, second & season from the selected timestamp/date column.

These values are extracted into new columns of the DataFrame.


