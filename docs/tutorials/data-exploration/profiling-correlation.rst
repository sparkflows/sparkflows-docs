Profiling and Correlation
=============

This workflow reads in a dataset. It then creates the correlation analysis and summary statistics.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a dataset.
* Perform correlation analysis of the required columns.
* Provide summary statistics of the dataset.

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/9.png
   :alt: ProfilingCorrelation
   :width: 60%
   
Performing Correlation analysis
---------------------

``Correlation`` processor performs correlation analysis on the selected columns as shown below. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/correlation-config.png
   :alt: ProfilingCorrelation
   :width: 60%
   
Processor Output - Correlation matrix
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/correlation-table.png
   :alt: ProfilingCorrelation
   :width: 60%   

Processor Output - Correlation Matrix Heat Map
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/correlation-matrix.png
   :alt: ProfilingCorrelation
   :width: 60%   

Processor Output - Sample Rows of Input Dataset
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/input.png
   :alt: ProfilingCorrelation
   :width: 60%   

   
Summary Statistics
------------

``Summary`` processor provides summary statistics of the input dataset.

Summary statistics provides useful information about sample data. For e.g. measures of spread.

It provides a table with number of non-null entries (count), mean, standard deviation, and minimum and maximum value for each numerical column.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/summary-config.png
   :alt: ProfilingCorrelation
   :width: 60%   

Processor Output: Summary Statistics
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/summary-output.png
   :alt: ProfilingCorrelation
   :width: 60%   
  
Processor Output: Sample Rows of Input Dataset
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/profiling-correlation/input.png
   :alt: ProfilingCorrelation
   :width: 60%    







