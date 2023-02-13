Profiling and Correlation
=============

This workflow reads in a dataset. It then creates the correlation analysis and summary statistics.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a dataset.
* Perform correlation analysis of the required columns.
* Provide summary statistics of the dataset.

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/9.PNG
   :alt: ProfilingCorrelation
   :width: 70%
   
Performing Correlation analysis
---------------------

``Correlation`` processor performs correlation analysis on the selected columns as shown below. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/2.PNG
   :alt: ProfilingCorrelation
   :width: 70%
   
Processor Output - Correlation matrix
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/3.PNG
   :alt: ProfilingCorrelation
   :width: 70%   

Processor Output - Correlation Matrix Heat Map
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/4.PNG
   :alt: ProfilingCorrelation
   :width: 70%   

Processor Output - Sample Rows of Input Dataset
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/5.PNG
   :alt: ProfilingCorrelation
   :width: 70%   

   
Summary Statistics
------------

``Summary`` processor provides summary statistics of the input dataset.

Summary statistics provides useful information about sample data. For e.g. measures of spread.

It provides a table with number of non-null entries (count), mean, standard deviation, and minimum and maximum value for each numerical column.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/6.PNG
   :alt: ProfilingCorrelation
   :width: 70%   

Processor Output: Summary Statistics
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/7.PNG
   :alt: ProfilingCorrelation
   :width: 70%   
  
Processor Output: Sample Rows of Input Dataset
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/8.PNG
   :alt: ProfilingCorrelation
   :width: 70%    







