Summary Statistics
=========== 

Summary statistics provide useful information about sample data. eg: measures of spread.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeSummary

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - title
        - Title
      * - colNames
        - Column Names
        - Column Names for Summary


Details
-------


Summary statistics provides useful information about sample data. eg: measures of spread.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/mllib-statistics.html#summary-statistics

Summary Node provides a table consist of informations such as number of non-null entries (count), mean, standard deviation, and minimum and maximum value for each numerical column.


Examples
-------


A set of columns can be selected to display Summary on.

If SummaryStatistics node is configured to compute Statistical Summary for [Salary]

then outgoing Dataframe would be created as below displaying Statistical Summary values:


*  count	:	8
*  mean	:	11500
*  min	:	10000
*  25_percentile	:	10000
*  50_percentile	:	11000
*  75_percentile	:	12000
*  max	:	13000
*  stdev	:	1195.229
*  variance	:	1428571.429
