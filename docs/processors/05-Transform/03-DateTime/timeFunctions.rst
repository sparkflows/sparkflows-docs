TimeFunctions
=========== 



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

Input
--------------

.. list-table:: 
   :widths: 25 10
   :header-rows: 2

   * - Date
     - Temp
     
   * - DateType
     - IntegerType
   
   * - 1981-01-01
     - 20.7
   
   * - 1981-01-02
     - 17.9
   
   * - 1981-01-03
     - 18.8
     
   * - 1981-01-04
     - 14.6
     
   * - 1981-01-05
     - 15.8
   

Parameters
------------

.. list-table:: 
   :widths: 40 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - TimeStamp Column Name
     - date_string
     
   * - Time Functions
     - yyyy-MM-dd HH:mm:ss
      

Output
--------

.. list-table:: 
   :widths: 10 30 30 30 30 30 30 30 30
   :header-rows: 1

   * - Date
     - Temp
     - date_year
     - date_month
     - date_dayofmonth
     - date_dayofweek
     - date_dayofyear
     - date_weekofyear
     - date_season
   
   * - 1981-01-01
     - 20.7
     - 1981
     - 1
     - 1
     - 5
     - 1
     - 1
     - Winter
     
   * - 1981-01-02
     - 17.9
     - 1981
     - 1
     - 2 
     - 6 
     - 2 
     - 1 
     - Winter
     
   * - 1981-01-03 
     - 18.8
     - 1981
     - 1
     - 3
     - 7
     - 3
     - 1
     - Winter
     
   * - 1981-01-04
     - 14.6
     - 1981
     - 1
     - 4
     - 1
     - 4
     - 1
     - Winter
     
   * - 1981-01-05
     - 15.8
     - 1981
     - 1
     - 5
     - 2
     - 5
     - 2
     - Winter
     


