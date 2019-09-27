StringToDate
=========== 

This node converts a string column to date using the given date/time format

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringToDate

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
      * - inputColFormat
        - Input Column Format
        - Input Column Format. eg: yyyy-MM-dd yyyy-MM-dd HH:mm:ss
      * - outputColName
        - Output Column Name
        - Output Column Name
      * - outputColType
        - Output Column Type
        - Output Column Type




Examples
-------


Format Examples
+++++++++++++++

dd-MM-yy : 31-01-12
dd-MM-yyyy : 31-01-2012
MM-dd-yyyy : 01-31-2012
yyyy-MM-dd : 2012-01-31
yyyy-MM-dd HH:mm:ss : 2012-01-31 23:59:59
yyyy-MM-dd HH:mm:ss.SSS : 2012-01-31 23:59:59.999
yyyy-MM-dd HH:mm:ss.SSSZ : 2012-01-31 23:59:59.999+0100
EEEEE MMMMM yyyy HH:mm:ss.SSSZ : Saturday November 2012 10:45:42.720+0100

OUTPUT COLUMN NAME: - If user inputs an existing column name, it overrides the column 
                      otherwise it will add a new column.



Input
--------------

.. list-table:: 
   :widths: 50 40 60 50 60 
   :header-rows: 1

   * - id
     - date_string
     - date_string1
   
   * - 0
     - 2011-1-1 00:00:00.0
     - 05/26/2016 01:01:01
   
   * - 1
     - 2012-1-14 01:00:00.0
     - 06/22/2017 01:00:00
   
   * - 2
     - 2013-12-10 02:00:00.0
     - 01/12/2016 01:01:01
     
