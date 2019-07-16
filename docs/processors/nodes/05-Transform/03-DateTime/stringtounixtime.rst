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
