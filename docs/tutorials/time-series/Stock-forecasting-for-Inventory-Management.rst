Stock Forecasting
=================

Objective
---------
Stock forecasting helps production units to get an idea about raw material, pricing of goods, improvement in supply-chain management and proper control of sales.

Dataset
--------

Data set contains 4 columns as follows:-

* Date - Product sold date
* Store - Store id from where product got sold
* Item - Item id
* Sales - Quantity of product sold


Prophet Time Series Modelling Workflow on Multivariate Data
-----------------------------------------------------------

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

.. figure:: ../../_assets/tutorials/time-series/stock_workflow1.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%


Node 1 - ReadCSV
++++++++++++++++


* Browse HDFS to set data path


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
++++++++++++++++++

* Filter data by row with respect to store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Node 3 - Prophet
++++++++++++++++

**General Section of Prophet model**

* Set Date column in DS column field
* Set Y as target here sales column is our target
* Set Growth as linear or Logistic
* We are using prophet model so that is self-sufficient to select seasonality in auto mode
* Set mode of seasonality as additive or multiplicative
* At last but not the least set confidance Interval(0 to 1) which gives a range of plausible values for the parameter of interest.

.. figure:: ../../_assets/tutorials/time-series/prophet_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


**Future Data section of Prophet model**

* In FUTURE PERIOD block give number of steps you want to predict 
* Give FREQUENCY as Monthly or Daily 
* INCLUDE HISTORY will true for testing our model and False for production
  
.. figure:: ../../_assets/tutorials/time-series/prophet_future.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

Node 4 - SQL
++++++++++++++++

**General Section of SQL node**

* Rename columns forecasted by prophet  

.. figure:: ../../_assets/tutorials/time-series/sql_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

**Schema Section of SQL node**

* Refresh Schema and set data type with respect to columns

.. figure:: ../../_assets/tutorials/time-series/sql_schema.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   

Node 5 - JoinUsingSQL
+++++++++++++++++++++

**General Section of JoinUsingSQL node**


* Join predicted(from SQL node) and Historical Data(from RowFilter node)

.. figure:: ../../_assets/tutorials/time-series/join_general.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

**Schema Section of JoinUsingSQL node**

* Follow same step as in Schema Section of SQL node

.. figure:: ../../_assets/tutorials/time-series/join_schema.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Node 6 - SaveCSV
++++++++++++++++


* Set path where you want to save final output


.. figure:: ../../_assets/tutorials/time-series/save_output_forecast.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%


Output Visualization
---------------------

Graphical representation is best way to understand insights from data. It refers to the use of charts and graphs to visually display, analyze, clarify, and interpret numerical data, functions, and other qualitative structures.

Below is the workflow for Visualizing it:

.. figure:: ../../_assets/tutorials/time-series/stock_graph_workflow1.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

Node 1 - ReadCSV
++++++++++++++++

* Read output csv which we have saved from Stock forecasting by passing path


.. figure:: ../../_assets/tutorials/time-series/graph_readcsv.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%

   
Node 2 - RowFilter
++++++++++++++++++

* Filter dataframe with categorical variable like store and item

.. figure:: ../../_assets/tutorials/time-series/Row_filter.png
   :alt: Stock Forecasting
   :align: center
   :width: 60%
   
Node 3 - Sortby
++++++++++++++++

* Gives options to sort our data set based on columns as ascending and descending order 
   
Node 4 - GraphValue
+++++++++++++++++++
* Define labels for X-axis and Y-axis 
* Set columns for X-axis and Y-axis

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
