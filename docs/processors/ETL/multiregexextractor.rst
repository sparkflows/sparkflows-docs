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




