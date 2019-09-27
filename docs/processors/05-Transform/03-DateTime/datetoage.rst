DateToAge
=========== 

This node converts a date-column into columns of age (both in years and in days).

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDateToAge

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColName
        - Input Column Name
        - Input Column Name
      * - yearsOutputColName
        - Years Output Column Name
        - Num Years Output Column Name
      * - daysOutputColName
        - Days Output Column Name
        - Num Days Output Column Name


Details
-------


Calculates age from the given date or timestamp column.
Age is calculated and displayed in years and days columns.


Examples
-------


Examples when date is 06-25-2019
+++++++++++++++

dd-MM-yyyy : 20-09-2018 , 0 year : 278 days
MM-dd-yyyy : 09-30-2018 , 0 year : 268 days
yyyy-MM-dd : 2012-01-31 , 7	year : 2702 days



Examples
---------

Input
--------------

.. list-table:: 
   :widths: 50 40 60 50 60 
   :header-rows: 1

   * - transactionId
     - cardNumber
     - tx_timestamp
     - amount
     - merchnatId
   
   * - 215667691-7
     - 0003
     - 2015-12-25 01:17:06
     - 14952.59
     - 43199-016
     
   * - 751006667-0
     - 0012
     - 2015-12-29 01:17:06
     - 16603.44
     - 63621-354
     
   * - 52339970-8
     - 0001
     - 2015-12-22 01:17:06
     - 29175.35
     - 64205-126
  
   * - 884800094-0
     - 0003
     - 2015-12-15 01:17:06
     - 30190.31
     - 50730-7993
    
Parameters
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - tx_timestamp
     
   * - Years Output Column Name
     - num_years
     
   * - Days Output Column Name
     - num_days
     

Output
--------------

.. list-table:: 
   :widths: 50 40 60 50 60 20 20
   :header-rows: 1

   * - transactionId
     - cardNumber
     - tx_timestamp
     - amount
     - merchnatId
     - num_years
     - num_days
   
   * - 215667691-7
     - 0003
     - 2015-12-25 01:17:06
     - 14952.59
     - 43199-016
     - 3
     - 1372
     
   * - 751006667-0
     - 0012
     - 2015-12-29 01:17:06
     - 16603.44
     - 63621-354
     - 3
     - 1368
     
   * - 52339970-8
     - 0001
     - 2015-12-22 01:17:06
     - 29175.35
     - 64205-126
     - 3
     - 1375
     
   * - 884800094-0
     - 0003
     - 2015-12-15 01:17:06
     - 30190.31
     - 50730-7993
     - 3
     - 1382
     
