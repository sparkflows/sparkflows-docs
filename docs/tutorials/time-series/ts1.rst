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
----------------


* Read data from using Readcsv node by passing path

* click on browse HDFS and select store_item_stock_train dataset

* Select data type from COLUMN TYPES FOR THE CSV and click OK


.. figure:: ../../_assets/tutorials/time-series/read_csv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%



