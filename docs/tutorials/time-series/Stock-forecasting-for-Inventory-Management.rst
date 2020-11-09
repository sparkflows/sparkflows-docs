Stock Forecasting
=================

Objective
---------
Stock forecasting helps production units to get an idea about raw material, pricing of goods, improvement in supply, chain management and proper control of sales.

Dataset
--------

Dataset contains 4 columns as follows:-

* Date - Date when product was sold
* Store - Store id from where product got sold
* Item - Item id
* Sales - Quantity of product sold

Predict future sales of items at particular store  

Prophet Time Series Modelling Workflow on Multivariate Data
-----------------------------------------------------------

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends fit with yearly, weekly, daily, seasonality and  holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

.. figure:: ../../_assets/tutorials/time-series/stock_workflow1.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%


Node 1 - ReadCSV
++++++++++++++++


* Reads the given CSV file : store_item_stock_train.csv


.. figure:: ../../_assets/tutorials/time-series/read_csv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%



* Below are the first 10 rows of data
* Columns contain data as datetype, store and item which are categorical variables and sales which is a continuous variable.


.. figure:: ../../_assets/tutorials/time-series/store_top_10.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 2 - RowFilter
++++++++++++++++++

* Filters data by row with respect to store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
   
Node 3 - Prophet
++++++++++++++++

Used Facebook Prophet to create the ML model.

**General Section of Prophet Model**

* Set Date column in DS column field
* Y is the target variable. Set it to the Sales column
* Set Growth as linear or logistic
* We are using prophet model so it is sufficient to select seasonality in auto mode
* Set mode of seasonality as additive or multiplicative
* Set confidence Interval (0 to 1) which gives a range of plausible values for the parameter of interest.

.. figure:: ../../_assets/tutorials/time-series/prophet_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


**Future Data section of Prophet model**

* FUTURE PERIOD block gives the number of steps we want to predict 
* FREQUENCY can be Monthly or Daily 
* Set INCLUDE HISTORY to true for testing the model and False for production
  
.. figure:: ../../_assets/tutorials/time-series/prophet_future.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 4 - SQL
++++++++++++++++

**General Section of SQL node**

* Renames columns forecasted by Prophet  

.. figure:: ../../_assets/tutorials/time-series/sql_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

**Schema Section of SQL node**

* Refreshes Schema and sets data type with respect to columns

.. figure:: ../../_assets/tutorials/time-series/sql_schema.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   

Node 5 - JoinUsingSQL
+++++++++++++++++++++

**General Section of JoinUsingSQL node**


* Joins Prediction (from SQL node) and Historical Data(from RowFilter node)

.. figure:: ../../_assets/tutorials/time-series/join_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

**Schema Section of JoinUsingSQL node**

* Follow the same steps as in Schema Section of SQL node

.. figure:: ../../_assets/tutorials/time-series/join_schema.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Node 6 - SaveCSV
++++++++++++++++


* Sets path where you want to save the final output


.. figure:: ../../_assets/tutorials/time-series/save_output_forecast.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Output Visualization
---------------------

Graphical representation is the best way to understand insights from data. It refers to the use of charts and graphs to visually display, analyze, clarify, and interpret numerical data, functions and other qualitative structures.

Below is the workflow for Visualizing it:

.. figure:: ../../_assets/tutorials/time-series/stock_graph_workflow1.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

Node 1 - ReadCSV
++++++++++++++++

* Reads output CSV which we have saved from Stock Forecasting.


.. figure:: ../../_assets/tutorials/time-series/graph_readcsv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

   
Node 2 - RowFilter
++++++++++++++++++

* Filters dataframe with categorical variables like store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Node 3 - SortBy
++++++++++++++++

* Gives options to sort our Dataset based on columns in ascending and descending order 
   
Node 4 - GraphValue
+++++++++++++++++++
* Defines labels for X-axis and Y-axis 
* Sets columns for X-axis and Y-axis

.. figure:: ../../_assets/tutorials/time-series/Graphvalues.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
**Graph obtained**

* Sales_pred_mean - Blue line
* Sales_pred_lower - Red line
* Sales_pred_upper - Magenta line 
* Sales - Yellow line
* Now have a look into graph

.. figure:: ../../_assets/tutorials/time-series/Graph_output.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
