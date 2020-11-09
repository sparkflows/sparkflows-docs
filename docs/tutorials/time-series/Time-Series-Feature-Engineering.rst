Time Series Feature Engineering
===============================

Objective
---------
It is a process of extracting new features from raw data via data mining techniques. These features can be used to improve the performance of models. 

Dataset
--------

Dataset contains 4 columns as below:

* Date - Date when product was sold
* Store - Store id from where product got sold
* Item - Item id
* Sales - Quantity of product sold

Create new feature from existing table to improve performance of models

Feature Engineering Workflow
-----------------------------
Each column is a feature. But all features may not produce the best results from models, so feature engineering plays an important role in choosing the right features. A model will not entirely improve its prescient force, yet will offer the adaptability to utilize less unpredictable models that are quicker to run and more handily.

.. figure:: ../../_assets/tutorials/time-series/ts_features/tsf_workflow.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

Moving average
--------------
**One step moving average**

* Moving average is commonly used to streamline short-period fluctuations in time series data and feature long-term patterns.
* For one step, window size will be from -1 to 1 for sales data

 .. figure:: ../../_assets/tutorials/time-series/ts_features/ma1.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

**Seven step moving average** 
 
* For seven step, window size will be from -7 to 7 for sales data
* Moving average output
 
 .. figure:: ../../_assets/tutorials/time-series/ts_features/moving_output.png
   :alt: Stock Forecasting
   :align: center
   :width: 100% 


Extract Date Time Features
--------------------------

* Break date and get the year, month, week of year, day of the month, hour, minute, second, etc.

 .. figure:: ../../_assets/tutorials/time-series/ts_features/date_field_extraction.png
   :alt: Stock Forecasting
   :align: center
   :width: 100% 

* Output of Date Time Features

 .. figure:: ../../_assets/tutorials/time-series/ts_features/date_extrected_output.png
   :alt: Stock Forecasting
   :align: center
   :width: 100% 

Lags Feature
------------

* Lag is used to make non-stationary data into stationary data
* Outliers are easily discernible on a lag plot
* acf and pacf plot is used to calcluate best lags

**Lag one**

* The most commonly used lag is 1, called a first-order lag
* Window shift is one

 .. figure:: ../../_assets/tutorials/time-series/ts_features/lag1.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

**Lag seven** 
 
* Window shift is seven
 
 .. figure:: ../../_assets/tutorials/time-series/ts_features/all_lags.png
   :alt: Stock Forecasting
   :align: center
   :width: 100% 

New feature data
----------------

 .. figure:: ../../_assets/tutorials/time-series/ts_features/featuredoutput.png
   :alt: Stock Forecasting
   :align: center
   :width: 100% 
