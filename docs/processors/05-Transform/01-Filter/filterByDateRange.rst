FilterByDateRange
=========== 

This node filters Rows within the given date range

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFilterByDateRange

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Column
        - input column name
      * - fromDateCol
        - From Date
        - Takes Start Date in the form of yyyy-MM-dd
      * - toDateCol
        - To Date
        - Takes End Date in the form of yyyy-MM-dd

Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 30
   :header-rows: 1

   * - id
     - date_col
   
   * - 1
     - 2016-04-09
     
   * - 2
     - 2016-08-16
     
   * - 3
     - 2016-06-26
     
   * - 4
     - 2016-10-20
     
   * - 5
     - 2016-07-30
    
   * - 6
     - 2016-09-23
     
   * - 7
     - 2017-02-23  

Parameters
----------


.. list-table:: 
   :widths: 10 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Column
     - date_col
     
   * - From Date
     - 2016-07-28
     
   * - To Date
     - 2017-03-31


Output
------

.. list-table:: 
   :widths: 10 30
   :header-rows: 1

   * - name
     - date_col
   
   * - 2
     - 2016-08-16
     
   * - 4
     - 2016-10-20
     
   * - 5
     - 2016-07-30
    
   * - 6
     - 2016-09-23
