Pivot
================

This tutorial will cover how to pivot a data table and aggregate data to focus on a particular subset of a larger dataset. Pivot can also be used to feed into data visualization nodes and provides additional dimensions that would not otherwise be available. This tutorial will use the widely available Titanic dataset. 

.. contents::
   :depth: 2



Visualizing Sales Data
-------------------------

The below workflow: 

* Prints the raw data for comparison
* Pivots the dataset and generate aggregate statistics
* Prints the final result of the pivot


.. figure:: ../../_assets/tutorials/data-exploration/pivot/Overview.PNG
   :alt: books-recommendations
   :width: 90%
   

Printing the Raw Dataset
-----------------------------------

We use the ``Print N Rows`` processor to print out a sample of the given dataset. In this case it is being used to compare the dataset before being pivoted.   

Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/pivot/Print1_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Pivoting the Dataset
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

   
Printing the Pivoted Dataset
-----------------------------------

We use the ``Print N Rows`` processor to print out a sample of the given dataset. In this case it is being used to compare the dataset after being pivoted.   

Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-exploration/pivot/Print2_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
