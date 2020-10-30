Stock Forecasting
=================
The auto_arima work fits the best ARIMA(Autoregressive Integrated Moving Average) model to a univariate time arrangement as indicated by either AIC, AICc, BIC or HQIC. The capacity plays out an inquiry (either stepwise or parallelized) over conceivable model requests inside the requirements given. 

The auto_arima capacity can be overwhelming. There are a ton of boundaries to tune, and the result is vigorously subject to various themes. In this segment, we spread out a few contemplations you'll need to make when you fit your ARIMA models.


Time Series Modelling Workflow on Univariate Data
-----------------------------------------------------------

.. figure:: ../../_assets/tutorials/time-series/ARIMA_workflow.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Node 1 - Readcsv
----------------


* Read data from using Readcsv node by passing path

* click on browse HDFS and select store_item_stock_train dataset

* Select data type from COLUMN TYPES FOR THE CSV and click OK


.. figure:: ../../_assets/tutorials/time-series/ARIMA_readcsv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
