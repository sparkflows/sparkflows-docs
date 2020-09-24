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

Below is the sample workflows which contains ``DateTimeFieldExtract`` processor in Fire Insights.

It reads the JetRail Train dataset & use DateTimeFieldExtract processor which create New DataFrame by extracting Date & Time field and print the result.

.. figure:: ..//_assets/ml_userguide/datetime_field.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%
   
DateTimeFieldExtract processor Configuration:

.. figure:: ..//_assets/ml_userguide/datetime_configuration.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Output result of ``DateTimeFieldExtract`` processor:

.. figure:: ..//_assets/ml_userguide/datetime_output_result.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Below is the sample workflows which contains ``MovingWindowingFunctions`` processor in Fire Insights.

It reads the ticker dataset, concatenate the input column, casting specified column to new data type, use MovingWindowingFunctions processor which calculates the moving value of selected function of input column and print the result. 

.. figure:: ..//_assets/ml_userguide/windowsfn.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

MovingWindowingFunctions processor Configuration:

.. figure:: ..//_assets/ml_userguide/windows_configuartion.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Output result of ``MovingWindowingFunctions`` processor:

.. figure:: ..//_assets/ml_userguide/output-result.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Time Series Visualizations
--------------------------

Fire Insights provides a number of Processors for the visualization of the time series data.

* Charts : LineChart

Below is the sample workflows which contains ``Time Series data`` and visualize using line chart in Fire Insights.

.. figure:: ..//_assets/ml_userguide/visualization.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Configurations for visualization processors in Fire Insight:

.. figure:: ..//_assets/ml_userguide/configurations_visualization.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Output result of ``Visualization`` processor:

.. figure:: ..//_assets/ml_userguide/outputresult_visualization.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Splitting
---------

Fire Insights provides processors for splitting the data by time for training, test and validation.

* Split By Time



