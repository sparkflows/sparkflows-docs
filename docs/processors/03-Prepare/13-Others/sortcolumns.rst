Sort Columns
=========== 

It sort the columns selection.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSortColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - sortColumnNames
        - Columns
        - Sort the Column Name


Details
-------


This node reorders columns present in the incoming DataFrame as specified.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY
-------------------------------------------------------------------------------------
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00

If SortColumns node is configured to reorder columns as [CUST_NAME], [AGE], [DATE_OF_JOINING], [CUST_CD] and [SALARY]
then outgoing Dataframe would be created as below:

CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    CUST_CD    |    SALARY
-------------------------------------------------------------------------------------
MATT         |    50     |    12-02-2002         |    C01        |    USD 200000.00
LISA         |    45     |    15-11-2020         |    C02        |    GBP 100000.00
ROBIN        |    30     |    10-10-2015         |    C03        |    EUR 15000.00
MARCUS       |    35     |    01-01-2021         |    C04        |    AUD 350000.00
