Pivot
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


.. figure:: ../../_assets/tutorials/data-exploration/pivot/Overview.PNG
   :alt: books-recommendations
   :width: 90%
   

Graphing Distribution of Sales Revenue
-----------------------------------

We use the ``BoxPlot`` processor to chart the distribution of a selected variable. This node also has the option to group by a different variable. In this case we are grouping sales by the ProductLine to show to distribution of sales in each category.  

Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/pivot/Print1_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Graphing Distribution of Sales Revenue
-----------------------------------

We use the ``BoxPlot`` processor to chart the distribution of a selected variable. This node also has the option to group by a different variable. In this case we are grouping sales by the ProductLine to show to distribution of sales in each category.  

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/pivot/Pivot1_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/pivot/Pivot2_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/pivot/Print2_output.PNG
   :alt: titanic-data-cleaning
   :width: 90%

