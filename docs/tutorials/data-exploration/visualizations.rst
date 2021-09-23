Data Visualizations
================

This tutorial will cover how to explore data using different types of graphs and charts that can capture different or more in-depth information than basic graphs. Specifically, this tutorial will cover how to create box-plots, bubble charts, and graph group by column. The data used in this tutorials is sales data provided by an online retailer. The original data can be found here: https://www.kaggle.com/kyanyoga/sample-sales-data

.. contents::
   :depth: 2



Visualizing Sales Data
-------------------------

The below workflow: 

* Creates a box-plot of sales revenue
* Creates a bubble chart labelled by order status
* Creates a graph of the count of different order status


.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Overview.PNG
   :alt: books-recommendations
   :width: 90%
   

Graphing Distribution of Sales Revenue
-----------------------------------

We use the ``Graph Group by Column`` processor to visually gauge the profile of our data. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Boxplot_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Boxplot_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Columns Cardinality
-----------------------

We use the ``Columns Cardinality`` node to find the number of unique values in a string variable. In this case we are using cardinality to gauge the relationship between publishers, authors, and books. We can see that publishers on average publish 14 books, while authors on average write 2.4 books. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Bubble_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Bubble_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%



Grouping Users by Age
------------------------

We use the ``Graph Group by Column`` processor to visually gauge the profile of our data. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Graph_Group_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/visualizations/Graph_Group_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%

  
