Stock Forecasting
=================

Periodically, we need to order products to replenish our inventory. When we do this, we have in mind a future period for which we are attempting to address demand along with an estimate of the demand in that period.
When actual demand exceeds our forecasts, we run the risk of a stockout (out of stock) situation with its associated potential loss of sales and reduced customer satisfaction. To avoid this, we often include additional units of stock, above the forecasted demand, in our replenishment orders. The amount of this safety stock depends on our estimates of variability in the demand for this upcoming period and the percentage of time we are willing to risk an out of stock situation.


Prophet Time Series Modelling Workflow on Multivariate Data
-----------------------------------------------------------

.. figure:: ../../_assets/tutorials/time-series/STOCK_WORKFLOW.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Node 1 - Readcsv
=================


* Read data from using Readcsv node by passing path

* click on browse HDFS and select store_item_stock_train dataset

* Select data type from COLUMN TYPES FOR THE CSV and click OK


.. figure:: ../../_assets/tutorials/time-series/read_csv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%



* Top 10 Rows of data
* Columns contains date as datetype, Store and Item are categorical variable and Sales as continuous variable


.. figure:: ../../_assets/tutorials/time-series/store_top_10.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 2 - RowFilter
=================

* Filter data by row with respect to store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Node 3 - Prophet
=================

General Section of Prophet model
----------------------------------

* Select Date column in DS column section
* Select Y as target here sales column is our target
* select Growth as linear or Logistic
* We are using prophet model so that is self-sufficient to select seasonality in auto mode
* Select mode of seasonality as additive or multiplicative
* At last but not the least Provide Interval for the Forecast between 0 to 1

.. figure:: ../../_assets/tutorials/time-series/prophet_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Future Data section of Prophet model
--------------------------------------

* In FUTURE PERIOD block give number of steps you want to predict 
* Give FREQUENCY as Monthely or Daily 
* INCLUDE HISTORY will true for testing our model and False for production
  
.. figure:: ../../_assets/tutorials/time-series/prophet_future.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 4 - SQL
=============


General Section of SQL node
----------------------------
* Write SQL query to select required columns from temp table

Schema Section of SQL node
----------------------------

* Refresh Schema and select give data type in OUTPUT COLUMN TYPES
* Click on OK to save changes
