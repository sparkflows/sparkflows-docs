DateDifference
=========== 

This node finds difference between two dates

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDateDiff

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - fromDate
        - FromDate
        - From date column name
      * - toDate
        - Todate
        - To date column name
      * - useCurrentDateAsToDateCol
        - useCurrentDateAsToCol
        - Current Date As ToDate
      * - days
        - Days
        - Days difference
      * - hours
        - Hours
        - Hours difference
      * - minutes
        - Minutes
        - Minutes difference
      * - seconds
        - Seconds
        - Seconds difference


Details
-------


Calculates difference between 2 given dates.
Difference between dates is displayed in days, hours, minutes, and seconds columns.


Examples
-------

Format Examples
+++++++++++++++
dd-MM-yy : 30-11-95 to 19-02-18 diff- 8608 days : 206609 hours : 12396574 min :	743794461 : second
dd-MM-yyyy : 10-02-1996 to 20-09-2017 diff- 8536 days : 204881 hours : 12292884 min :	737573070 : second
MM-dd-yyyy : 19-10-1994 to 06-12-2017 diff- 9015 days : 216377 hours : 12982644 min :	778958670 : second
yyyy-MM-dd : 1994-12-25 to 2019-01-16 diff- 8948 days : 214769 hours : 12886164 min :	773169870 : second
yyyy-MM-dd HH:mm:ss : 2012-01-31 23:59:59 to 2010-12-30 22:59:59 diff-397 days: 1 hour: 0 minutes : 0 seconds
