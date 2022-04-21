Filter By Date Range
=========== 

This node filters Rows within the given date range

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFilterByDateRange

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Column
        - input column name
      * - fromDateCol
        - From Date
        - Takes Start Date in the form of yyyy-MM-dd
      * - toDateCol
        - To Date
        - Takes End Date in the form of yyyy-MM-dd


Details
-------


This node filters Rows within the given date range.

New outgoing Dataframe is created based on filtered rows and it is passed to next node.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    INV_NO    |    INV_DT      |    PRD_CD
----------------------------------------------------------
C01        |    INV1111   |    2021-10-01  |    PRD01
C01        |    INV1112   |    2021-10-03  |    PRD02
C01        |    INV1113   |    2021-10-05  |    PRD03
C01        |    INV1114   |    2021-10-07  |    PRD04
C01        |    INV1115   |    2021-10-09  |    PRD05
C01        |    INV1116   |    2021-10-10  |    PRD06

If FilterByDateRange node is configured as below:

COLUMN       :    INV_DT_VAL
FROM DATE    :    2021-10-01
TO DATE      :    2021-10-05

then outgoing Dataframe would be created as below with the rows falling in the given date range:

CUST_CD    |    INV_NO    |    INV_DT      |    PRD_CD
----------------------------------------------------------
C01        |    INV1111   |    2021-10-01  |    PRD01
C01        |    INV1112   |    2021-10-03  |    PRD02
C01        |    INV1113   |    2021-10-05  |    PRD03
