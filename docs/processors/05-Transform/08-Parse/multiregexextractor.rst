MultiRegexExtractor
=========== 

This node to extract pattren from input columns

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node extract pattren from input columns as specified

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMultiRegexExtractor

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColNames
        - InputColumnsName
        - Columns
      * - outputColNames
        - OuputColumnsName
        - name of the output column
      * - patterns
        - Patterns
        - patterns or regex to extract the input column name
      * - groups
        - Groups
        - An regular expression group number starting with 1, defining which portion of the matching string will be returned


Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 30 40
   :header-rows: 2

   * - id
     - name
     - datetime
   
   * - StringType
     - StringType
     - StringType
     
   * - 1
     - Robert ryl
     - 2018-10-11 12:10:22
     
   * - 2
     - Daniell Hammack
     - 2017-10-11 10:10:22
     
   * - 3
     - Versie Hillebrand
     - 2013-10-11 20:10:22
  
   * - 4
     - Markita Hansen
     - 2012-11-13 23:10:25
     
   * - 5
     - Kary Hendrixson
     - 2017-10-18 22:10:26
   
   
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
   
   
   


