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



* Top 10 Rows of data
* Columns contains date as datetype, Store and Item are categorical variable and Sales as continuous variable


.. figure:: ../../_assets/tutorials/time-series/store_top_10.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 2 - RowFilter
------------------

* Filter data by row with respect to store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Node 3 - Prophet
------------------

General Section of Prophet model

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
* Give FREQUENCY as Monthly or Daily 
* INCLUDE HISTORY will true for testing our model and False for production
  
.. figure:: ../../_assets/tutorials/time-series/prophet_future.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 4 - SQL
--------------


General Section of SQL node

* Write SQL query to select required columns from temp table

.. figure:: ../../_assets/tutorials/time-series/sql_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Schema Section of SQL node
----------------------------

* Refresh Schema and select give data type in OUTPUT COLUMN TYPES
* Click OK to save changes

.. figure:: ../../_assets/tutorials/time-series/sql_schema.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   

Node 5 - JoinUsingSQL
------------------------

General Section of JoinUsingSQL node


* Write SQL query to join predicted(Data from SQL node) and History data(Data from RowFilter node)

.. figure:: ../../_assets/tutorials/time-series/join_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Schema Section of JoinUsingSQL node
-----------------------------------

* Follow same step as in Schema Section of SQL node

.. figure:: ../../_assets/tutorials/time-series/join_schema.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Node 6 - SaveCSV
-----------------


* click on browse HDFS select folder path where you want to save final output
* SAVE MODE block gives you flexibility of append, overwrite etc
* Select your header preference as true or false
* PARTITION section gives you flexibility to select columns which you want to save


.. figure:: ../../_assets/tutorials/time-series/save_output_forecast.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Output Visualization
---------------------

We now have access to forecasted and actual demand store-item(1-1) combinations. Let's quickly visualize forecasted and actual demand for the combination of item 1 in store 1. We will limit the visualization to data in calendar year 2013 for ease of interpretation:

* The forecast is not expected to perfectly predict demand. Instead, it provides a mean estimate around which actual demand varies.




Visualization workflow
-----------------------

.. figure:: ../../_assets/tutorials/time-series/stock_graph_workflow.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 1 - ReadCSV
----------------

* Read output csv which we have saved from Stock forecasting for Inventory Management
* click on browse HDFS and select output_forecast dataset
* Select data type from COLUMN TYPES FOR THE CSV and click OK


.. figure:: ../../_assets/tutorials/time-series/graph_readcsv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

   
Node 2 - RowFilter
------------------

* Filter dataframe with categorical variable like store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Node 3 - Sortby
---------------

* Gives options to sort our data set based on columns as ascending and descending order 
   
Node 4 - GraphValue
-------------------

* TITLE - Give title to Graph
* LABELS - Define labels for X-axis and Y-axis 
* MAX VALUES TO DISPLAY - Maximum number of values want to plot into graph
* CHART TYPE - accourding to your requirement select chart type like line for continous variable, histogram for count of categorical variable etc.
* IS STREAMING - Define is your data is live streming or not as true or false 
* X COLUMN - Select column for X-axis which you want to represent as here Forecasted date on X-axis
* Y COLUMN - Select columns for Y-axis which you want to represent as here we represented sales_pred_mean, sales_pred_lower, sales_pred_upper, sales.

.. figure:: ../../_assets/tutorials/time-series/Graphvalues.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Now we reach on intresting part
-------------------------------

* sales_pred_mean - Blue line
* sales_pred_lower - Red line
* sales_pred_upper - Magenta line 
* sales - Yellow line
* In last you can also check what data we ploted on this graph 

.. figure:: ../../_assets/tutorials/time-series/Graph_output.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
