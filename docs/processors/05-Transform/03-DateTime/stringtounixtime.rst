StringToUnixTime
=========== 

This nodes converts a string to Unix Time

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringToUnixTime

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
        - Input Column Format (eg: yyyy-MM-dd HH:mm:ss)
      * - outputColName
        - Output Column Name
        - Output Column Name


Details
-------


This node converts a string column to unix time (seconds).


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

Example: 
Date (string), Format , Unix time (seconds)
 2003-07-25 , yyy-MM-dd , 1059091200
 

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
------------

.. list-table:: 
   :widths: 40 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - date_string
     
   * - Input Column Format
     - yyyy-MM-dd HH:mm:ss
     
   * - Output Column Name
     - unix_time
 

Output
--------

.. list-table:: 
   :widths: 10 50 50 30
   :header-rows: 1

   * - id
     - date_string
     - date_string1
     - unix_time
   
   * - 0
     - 2011-1-1 00:00:00.0
     - 05/26/2016 01:01:01
     - 1293840000
   
   * - 1
     - 2012-1-14 01:00:00.0
     - 06/22/2017 01:00:00
     - 1326502800
   
   * - 2
     - 2013-12-10 02:00:00.0
     - 01/12/2016 01:01:01
     - 1386640800
     
