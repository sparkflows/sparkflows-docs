Time Series Analysis
====================

Time series analysis is a statistical technique that deals with time series data, or trend analysis.  Time series data means that data is in a series of  particular time periods or intervals.  

https://www.statisticssolutions.com/time-series-analysis/

Fire Insights provides a number of features for Time Series Analysis.

Time Series Modeling
--------------------

Fire Insights provides a number of Processors for Time Series Modeling. These include:

* H2OXGBoost
* Prophet : https://facebook.github.io/prophet/
* Arima

Time Series Feature Engineering
------------------------------

Fire Insights provides a number of Processors for Feature Engineering of Time Series Data. These include:

* DateTimeFieldExtract : Extracts year, month, day of month, hour, minute, second and week of year from timestamp/date columns.
* MovingWindowingFunctions : Calculates the moving values using the given function.
* WindowingAnalytics : Window Analytics Functions

Below is the workflows which contains ``MovingWindowingFunctions`` processor in Fire Insights.

.. figure:: ..//_assets/ml_userguide/windowsfn.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%
   
   
Time Series Visualizations
--------------------------

Fire Insights provides a number of Processors for the visualization of the time series data.

* Charts : LineChart

Splitting
---------

Fire Insights provides processors for splitting the data by time for training, test and validation.

* SplitByTime



