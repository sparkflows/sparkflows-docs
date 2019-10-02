ParseJSONCol
=========== 

Parses JSON content in a given Col

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeParseJSONColumn

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - jsonColName
        - JSON Col Name
        - Column containing the JSON Content
      * - inputCol
        - Input Col
        - Input Columns
      * - jsonFieldNames
        - JSON Field names
        - JSON Field names
      * - jsonFieldTypes
        - JSON Field Type
        - Data Type of the JSON field


Examples
---------

Input
--------------

.. list-table:: 
   :widths: 60
   :header-rows: 2

   * - txt
   
   * - StringType
 
   * - {"name":"Michael"}
     
   * - {"name":"Andy", "age":30}
     
   * - {"name":"Justin", "age":19}
  
  
Parameters
----------


.. list-table:: 
   :widths: 30 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - JSON Col Name
     - txt
     
.. list-table:: 
   :widths: 30 30 30
   :header-rows: 1
   
   * - Input Col
     - JSON Field names
     - JSON Field Type
     
   * - txt
     - name
     - StringType
     
   * - txt
     - age
     - IntegerType
     
     
Output
--------------

.. list-table:: 
   :widths: 60 60 30 30
   :header-rows: 2

   * - txt
     - txt_parsed
     - name
     - age
   
   * - StringType
     - StructType(StructField(name,StringType,true)
     - StringType
     - IntegerType
 
   * - {"name":"Michael"}
     - [Michael,null]
     - Michael
     -
     
   * - {"name":"Andy", "age":30}
     - [Andy,30]
     - Andy
     - 30
     
   * - {"name":"Justin", "age":19}
     - [Justin,19]
     - Justin
     - 19


