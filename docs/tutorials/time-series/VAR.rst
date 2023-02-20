Multivariate time series forecasting – Vector Auto Regression (VAR)
===================================================================

VAR model is a stochastic process that represents a group of time-dependent variables as a linear function of their own past values and 
the past values of all the other variables in the group.
For instance, we can consider a bivariate time series analysis that describes a relationship between hourly temperature and wind speed as a function of 
past values [2]:

- temp(t) = a1 + w11* temp(t-1) + w12* wind(t-1) + e1(t-1)
- wind(t) = a2 + w21* temp(t-1) + w22*wind(t-1) +e2(t-1)
where a1 and a2 are constants; w11, w12, w21, and w22 are the coefficients; e1 and e2 are the error terms.

Time Series Modelling Workflow
------------------------------

The below workflow:

- Reads the input CSV data.
- Drops the unwnamted columns.
- Builds the VAR model on input data.

VARForecast:
   
- Validate the model.(isValidation is true & pass the validation dat).
- Forest (isValidation is false).
   
   .. figure:: ../../_assets/tutorials/time-series/var/TimeSeriesMulti-WF.png
      :alt: VAR
      :width: 70%   
   
Read CSV
---------
 In Read CSV, select the input path and refresh the schema.

   .. figure:: ../../_assets/tutorials/time-series/var/2.png
      :alt: VAR
      :width: 75% 
   
Input Data
---------- 

   .. figure:: ../../_assets/tutorials/time-series/var/3.png
      :alt: VAR
      :width: 75% 
   
Drop Column
-----------
Drop the unwanted column.

   .. figure:: ../../_assets/tutorials/time-series/var/4.png
      :alt: VAR
      :width: 75% 
   

VAR
-----------
Configure the VAR stats model.

   .. figure:: ../../_assets/tutorials/time-series/var/5.png
      :alt: VAR
      :width: 75% 
   
Summary:
--------

   .. figure:: ../../_assets/tutorials/time-series/var/summary.png
      :alt: VAR
      :width: 65% 


Validation:
--------
For Validation, select isValidation as true and pass the validation data.

   .. figure:: ../../_assets/tutorials/time-series/var/6.png
      :alt: VAR
      :width: 75% 
   
Validation Metrics
------------------
   .. figure:: ../../_assets/tutorials/time-series/var/validation-metrics.png
      :alt: VAR
      :width: 65%  
   
Forecast
-----------
Select the steps for number of forecast.

   .. figure:: ../../_assets/tutorials/time-series/var/7.png
      :alt: VAR
      :width: 75%  
 
Forecast output
---------------
   .. figure:: ../../_assets/tutorials/time-series/var/result.png
      :alt: VAR
      :width: 75%     

   
