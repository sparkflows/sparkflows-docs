DateToString
=========== 

This node converts a date/time column to string with given format

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDateToString

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
      * - outputColFormat
        - Output Column Format
        - Output Column Format
      * - outputColName
        - Output Column Name
        - Output Column Name


Details
-------


This node converts date/time column to string type with given format.


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
--------

.. list-table:: 
   :widths: 10 50
   :header-rows: 2

   * - id
     - date
  
   * - IntegerType
     - DateType
     
   * - 0
     - 2011-01-01
   
   * - 1
     - 2012-01-14
     
   * - 2
     - 2013-12-10
     
Parameters1
-------------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - date_string1
     
   * - Output Column Format
     - MM/dd/yyyy
     
   * - Output Column Name
     - date_string
 
Output1
--------------

.. list-table:: 
   :widths: 10 30 30
   :header-rows: 2

   * - id
     - date
     - date_string
   
   * - IntegerType
     - DateType
     - StringType
     
   * - 0
     - 2011-01-01
     - 01/01/2011
   
   * - 1
     - 2012-01-14
     - 01/14/2012
     
   * - 2
     - 2013-12-10
     - 12/10/2013
