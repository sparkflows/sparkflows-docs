Zip With Index
=========== 

This node Generates a new column with unique Index/Value for each row in the Dataset

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeZipWithIndex

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - indexColName
        - Index Column Name
        - Index column name


Details
-------


This node Generates a new column with unique Index/Value for each row in the Dataset.

This column is added to the outgoing Dataframe. It can be used to access a row within the Dataframe.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY
-------------------------------------------------------------------------------------
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00

If ZipWithIndex node is configured to create an index column as [INDEX_COL]
then outgoing Dataframe would be created as below containing the index column:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY         |    INDEX_COL    
-------------------------------------------------------------------------------------------------------
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00  |    0
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00  |    1
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00   |    2
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00  |    3
