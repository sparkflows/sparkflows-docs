Anamoly Detection for IOT Devices
=================================


Objective
---------
Anomaly detection issue for time arrangement can be planned as discovering exception information guides relative toward some norm or common sign. Our center will be from a machine persopective, for example, surprising spikes, level move highlighting disintegrating soundness of a machine.

Dataset
--------

Dataset contains 4 columns as follows:-

* Datetime - 10 mins time interval of accelerometer data
* 4-Bearings - Contains reading of devices


Anamoly Detection using Prophet Time Series Model Workflow
-----------------------------------------------------------

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends fit with yearly, weekly, daily, seasonality and holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Time-series anomaly detection is a feature used to identify unusual patterns that do not conform to expected behavior, called outliers.

.. figure:: ../../_assets/tutorials/time-series/IOT/Anamoly_workflow.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%
   
Data Preprocessing
------------------

* **Column Filter** convert multivariate data into univariate for prophet model

.. figure:: ../../_assets/tutorials/time-series/IOT/column_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%
   
* **Output** Univariate data

.. figure:: ../../_assets/tutorials/time-series/IOT/col_filt_out.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%
   
Data Modeling
-------------

* **Prophet** Model for anomaly detication using mean as threshold value


**General Section of Prophet Model**

* Set Datetime column in DS column field
* Y is the target variable. Set it to the reading of bearings
* Set Growth as linear or logistic
* We are using prophet model so that it is self-sufficient to select seasonality in auto mode
* Set mode of seasonality as additive or multiplicative
* Set confidence Interval (0 to 1) which gives a range of plausible values for the parameter of interest.

.. figure:: ../../_assets/tutorials/time-series/IOT/prophet_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


**Future Data section of Prophet model**

* FUTURE PERIOD block gives the number of steps we want to predict 
  
.. figure:: ../../_assets/tutorials/time-series/IOT/prophet_future.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
* **SQL** set mean column to set threshold

.. figure:: ../../_assets/tutorials/time-series/IOT/prophet_out.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Model prediction
----------------

* **Threshold** to compare anomaly

.. figure:: ../../_assets/tutorials/time-series/IOT/iot_final_out.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
