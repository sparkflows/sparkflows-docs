Air Passengers Forecasting
==========================

Objective
---------

The objective is to develop a time series model to predict future demand of air passengers which helps Airline company to take decision on aircraft fleet management.

Data-set
--------

Data set contains 2 columns as follows:-

Month - Month of the years

Passengers - Total number of passengers travelled on that particular month.

Time Series Modelling Workflow on Univariate Data
--------------------------------------------------

The auto_arima work to fit the best ARIMA(Autoregressive Integrated Moving Average) model to a univariate time arrangement as indicated by either AIC, AICc, BIC or HQIC. The capacity plays out an inquiry (either stepwise or parallelized) over conceivable model requests inside the requirements given. 

The auto_arima capacity can be overwhelming. There are a ton of boundaries to tune, and the result is vigorously subject to various themes. In this segment, we spread out a few contemplations you'll need to make when you fit your ARIMA models.

.. figure:: ../../_assets/tutorials/time-series/air_flow.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 1 - Readcsv
----------------

* Read data from using Readcsv node by passing path

* click on browse HDFS and select AirPassengers dataset

* Select data type from COLUMN TYPES FOR THE CSV and click OK

.. figure:: ../../_assets/tutorials/time-series/ARIMA_readcsv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 2 - ARIMA
----------------

* p - The number of lag observations included in the model, also called the lag order.
* d - The number of times that the raw observations are different, also called the degree of differencing.
* q - The size of the moving average window, also called the order of moving average.

Don't worry about p,d,q in this case because we have something interesting model called  - AUTO-ARIMA(Able to select automatically optimal value)

* Y - Target Variable(Passengers Per Month)
* SEASONAL - automatically True but you can change as false if you want as non-seasonal
* STEPWISE - If you want to use flexibility of auto-arima so keep it true
* TRACE - Print parameters used in auto-arima
* SUPPRESS WARNINGS - Ignore warnings
* ERROR ACTION - You can also ignore errors it get automatically handled 
* SCORING - How you want to evaluate your model performance like - MSE, MAE
* FORECAST - Number of steps you want to get forecasted

.. figure:: ../../_assets/tutorials/time-series/ARIMA_model.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Summary
-------
 
* It provide to analyse what are different conditions used by trained model 
   
.. figure:: ../../_assets/tutorials/time-series/ARIMA_summary.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 3 - ZipWithIndex
---------------------

* Identify column which you want to make as index

Node 4 - PrintNRows
-------------------

* How many rows you want to print to see final predicted result

.. figure:: ../../_assets/tutorials/time-series/arima_printnrows.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Final Result
------------
 
Lets check few rows of our final forecasted result of ARIMA Model
 
.. figure:: ../../_assets/tutorials/time-series/arima_predicted_result.png
  :alt: Stock Forecasting
  :align: center
  :width: 60%
