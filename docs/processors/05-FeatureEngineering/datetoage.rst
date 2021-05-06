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
