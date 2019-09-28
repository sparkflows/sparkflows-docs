MultiStringToDate
=========== 

This node converts a string column to date using the given date/time format

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMultiStringToDate

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColNames
        - Columns
        - Columns
      * - inputColFormats
        - Column Formats
        - Input Column Formats. eg: yyyy-MM-dd yyyy-MM-dd HH:mm:ss
      * - outputColNames
        - Output Column Names
        - Output Column Names
      * - outputColTypes
        - New Data Types
        - New data types (DATE, TIMESTAMP)


Details
-------


This node converts multiple string columns to date/time.


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


Input
--------------

.. list-table:: 
   :widths: 10 50 50
   :header-rows: 2

   * - id
     - date_string
     - date_string1
     
   * - IntegerType
     - StringType
     - StringType 
   
   * - 0
     - 2011-1-1 00:00:00.0
     - 05/26/2016 01:01:01
   
   * - 1
     - 2012-1-14 01:00:00.0
     - 06/22/2017 01:00:00
   
   * - 2
     - 2013-12-10 02:00:00.0
     - 01/12/2016 01:01:01
     

Parameters
-------------

.. list-table:: 
   :widths: 10 25 25 25 25
   :header-rows: 1

   * - Id
     - Columns
     - Column Formats
     - Output Column Names
     - New Data Types
   
   * - 1
     - date_string
     - yyyy-M-dd HH:mm:ss
     - date_string_date
     - DATE
     
   * - 2
     - date_string
     - yyyy-M-dd HH:mm:ss
     - date_string_timestamp
     - TIMESTAMP   
 
   * - 3
     - date_string1
     - MM/dd/yyyy HH:mm:ss
     - date_string1_date
     - DATE
     
   * - 4
     - date_string1
     - MM/dd/yyyy HH:mm:ss
     - date_string1_timestamp
     - TIMESTAMP
     
Output
---------
 
.. list-table:: 
   :widths: 10 50 50 50 50 50 50
   :header-rows: 2

   * - id
     - date_string
     - date_string1
     - date_string_date
     - date_string_timestamp
     - date_string1_date
     - date_string1_timestamp
     
   * - IntegerType
     - StringType
     - StringType
     - DateType
     - TimestampType
     - DateType
     - TimestampType
   
   * - 0
     - 2011-1-1 00:00:00.0
     - 05/26/2016 01:01:01
     - 2011-01-01	
     - 2011-01-01 00:00:00.0
     - 2016-05-26
     - 2016-05-26 01:01:01.0
   
   * - 1
     - 2012-1-14 01:00:00.0
     - 06/22/2017 01:00:00
     - 2012-01-14
     - 2012-01-14 01:00:00.0
     - 2017-06-22
     - 2017-06-22 01:00:00.0
   
   * - 2
     - 2013-12-10 02:00:00.0
     - 01/12/2016 01:01:01
     - 2013-12-10
     - 2013-12-10 02:00:00.0
     - 2016-01-12
     - 2016-01-12 01:01:01.0
     
     
