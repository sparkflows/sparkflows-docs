Date Time Field Extract
=========== 

It creates a new DataFrame by extracting Date and Time fields.

Input
--------------
It takes in a DataFrame as Input

Output
--------------
The output DataFrame has year/month/dayofmonth/hour/minute/second values extracted from the specified TimeStamp column into new columns

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDateTimeFieldExtract

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
        - The input column name
      * - extractYear
        - Extract Year
        - Extract Year
      * - extractMonth
        - Extract Month
        - Extract Month
      * - extractDayOfMonth
        - Extract Day of Month
        - Extract Day of Month
      * - extractHour
        - Extract Hour
        - Extract Hour
      * - extractMinute
        - Extract Minute
        - Extract Minute
      * - extractSecond
        - Extract Second
        - Extract Second
      * - extractWeekOfYear
        - Extract WeekOfYear
        - Extract WeekOfYear


Details
-------


It creates a new DataFrame by extracting Date and Time fields.

The output DataFrame has year/month/dayofmonth/hour/minute/second values extracted from the specified TimeStamp column into new columns


Examples
-------


If incoming Dataframe has Date value as 2018-01-01 14:30:45 in YYYY-MM-DD HH:mm:ss format then using datetimeextract node would result in followings 
added as new columns to the Dataframe:


*  YEAR : 2018 
*  MONTH : 01
*  DAY OF MONTH : 01 
*  HOUR : 14
*  MINUTE : 30
*  SECOND : 45
*  WEEKOFYEAR : 1 
