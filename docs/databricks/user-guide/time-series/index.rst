Time Series Analysis
=====================

Time series forecasting is one of the most important use case in real world in areas of sales forecasting,energy demand, price prediction among others. Time series data is data captured at particular time periods or intervals. There is an explicit order dependency between observations. There are many datasets which have a sequential time component captured in them. Analytics and Machine learning solutions build using these datasets can benefit from learning from the time dimension captured in the dataset.


Sparkflows provides rich set of features for Time Series Analysis. Using the features available, once can model time series use cases as one of the below approaches:

* Create enginereed features (like different time interval lags) to capture the time component and then build tree models on it. This can handle univariate as well and multivariate time series use cases.
* Use the traditional approaches like prophet, arima, sarimax, var techniques. This can also handle univariate as well and multivariate time series use cases.

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/time-series/time_series_feature_engineering`

    Provides a number of Processors for Feature Engineering of Time Series Data.

    ---

    :doc:`/user-guide/time-series/time_series_visualizations`

    Provides a number of Processors for Visualization of Time Series Data.

    ---

    :doc:`/user-guide/time-series/time_series_modeling`

    Provides a number of Processors for Time Series Modeling.


.. toctree::
   :hidden:

   time_series_feature_engineering.rst
   time_series_visualizations.rst
   time_series_modeling.rst
   
