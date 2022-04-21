Sort By
=========== 

It sorts the incoming DataFrame on the fields specified.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSortBy

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - description
        - Description
        - Description
      * - sortByColNames
        - Columns
        - Columns on which to Sort By
      * - ascDesc
        - Sorting Order
        - Whether to sort in ascending or descending order


Details
-------


This node sorts the incoming DataFrame based on the values present in columns specified.

Multiple columns can be selected for sorting data. Data can be sorted in Ascending or Descending order.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY
-------------------------------------------------------------------------------------
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00

If SortBy node is configured to sort data in descending order of values present in [CUST_NAME] column then outgoing Dataframe would be created as below:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY
-------------------------------------------------------------------------------------
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00
