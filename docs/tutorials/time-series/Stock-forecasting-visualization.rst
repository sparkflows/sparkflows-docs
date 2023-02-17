Stock Forecasting Visualization
---------------------

Graphical representation is the best way to understand insights from data. It refers to the use of charts and graphs to visually display, analyze, clarify, and interpret numerical data, functions and other qualitative structures.

Below is the workflow for Visualizing it:

   .. figure:: ../../_assets/tutorials/time-series/stock_graph_workflow1.png
      :alt: Stock Forecasting
      :width: 75%

Node 1 - ReadCSV
++++++++++++++++

* Reads output CSV which we have saved from Stock Forecasting.


   .. figure:: ../../_assets/tutorials/time-series/graph_readcsv.png
      :alt: Stock Forecasting
      :width: 75%

   
Node 2 - RowFilter
++++++++++++++++++

* Filters DataFrame with categorical variables like store and item.

      .. figure:: ../../_assets/tutorials/time-series/Row_filter.png
         :alt: Stock Forecasting
         :width: 75%
   
Node 3 - SortBy
++++++++++++++++

* Gives options to sort our dataset based on columns in ascending and descending order. 
   
Node 4 - GraphValue
+++++++++++++++++++
* Defines labels for X-axis and Y-axis. 
* Sets columns for X-axis and Y-axis.

   .. figure:: ../../_assets/tutorials/time-series/Graphvalues.png
      :alt: Stock Forecasting
      :width: 75%
   
**Graph obtained**

* Sales_pred_mean - Blue line.
* Sales_pred_lower - Red line.
* Sales_pred_upper - Magenta line. 
* Sales - Yellow line.
* Now have a look into graph.

   .. figure:: ../../_assets/tutorials/time-series/Graph_output.png
      :alt: Stock Forecasting
      :width: 75%
