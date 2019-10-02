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
   :widths: 30 30 60 10
   :header-rows: 1
   
   * - InputColumnsName
     - OuputColumnsName
     - Patterns
     - Groups
     
   * - name
     - (.*) (.*)
     - firstname
     - 1
     
   * - name
     - (.*) (.*)
     - lastname
     - 2 
   
   * - datetime
     - ([0-9]{4}-[0-9]{2}-[0-9]{2})
     - date
     - 1


