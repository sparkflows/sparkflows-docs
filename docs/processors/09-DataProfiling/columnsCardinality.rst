Columns Cardinality
=========== 

Distribution of categorical data. Calculates the count of records for each unique value for the column specified.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeColumnsCardinality

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - maxValuesToDisplay
        - Max Values To Display
        - Maximum number of values to display in result.
      * - inputCols
        - Column Names
        - Name of columns for the cardinality data


Details
-------


This node displays distribution of categorical data. Calculates the count of records for each unique value for the column specified.

This node facilitates selection of multiple String columns. Distribution of each column is displayed separately.


Examples
-------


If ColumnsCardinality node is configured to display distribution on two columns i.e. [DEPT] and [SALARY_GRADE] from the incoming dataset 
then output would be created as below:

 Columns Unique Count 
+++++++++++++++
displaying count of unique values for each column


DEPT	: 3
SALARY_GRADE	: 3

 Distribution of first selected column [DEPT]
+++++++++++++++

HR : 3
SALES : 3
MANAGEMENT : 1

 Distribution of second selected column [SALARY_GRADE]
+++++++++++++++

HIGH : 3
MID : 2
LOW : 2
