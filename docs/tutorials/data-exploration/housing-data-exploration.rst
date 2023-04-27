Data Exploration of Housing Data
=========================

This workflow shows how to explore the Housing Dataset from Kaggle with Sparkflows.

Workflow
--------
The below workflow: 

* Reads the Housing dataset.
* Calculates summary statistics for important variables.
* Creates a histogram to show the distribution of the Sale Price variable.
* Creates a graph to show the relationship between Sale Price and Basement Square Footage.
* Creates a matrix to show the correlation between important variables.
* Flags outliers in Ground Living Area and graphs the results.

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/housing-data-explore-WF.png
   :alt: housing-data-exploration
   :width: 65%
   
Reading Housing Dataset
---------------------

``DatasetStructured`` Processor creates a Dataframe of your dataset named ``Housing Training`` by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature.

Processor Output
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/housing-input.png
   :alt: housing-data-exploration
   :width: 65%
   

Calculate Summary Statistics
----------------
``Summary Statistics`` Processor calculates summary statistics for the selected variables.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/summary-config.png
   :alt: housing-data-exploration
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/summary-output.png
   :alt: housing-data-exploration
   :width: 65%


Create Histogram Graph
----------------
``HistoGram`` Processor creates a histogram to show distribution by count of Sale Price.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/histogram-config.png
   :alt: housing-data-exploration
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/histogram-output.png
   :alt: housing-data-exploration
   :width: 65%
   
Graph Values
---------------------

``Graph Values`` Processor graphs the relationship between Sale Price and Basement Sqaure Footage.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/graphvalues-config.png
   :alt: housing-data-exploration
   :width: 65%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/graphvalues-output.png
   :alt: housing-data-exploration
   :width: 65%

Plot Correlation Matrix
---------------

``Correlation`` Processor creates a correlation matrix of selected variables and plots the results.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/correlation-config.png
   :alt: housing-data-exploration
   :width: 65%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/correlation-output.png
   :alt: housing-data-exploration
   :width: 65%



Flag Outliers and Create Graph
----------------
``Flag Outlier`` Processor creates a new flag column to mark outliers and ``Graph Group by Column`` Processor graphs the count in each category.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/flag-outlier-config.png
   :alt: housing-data-exploration
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/graphgroup-output.png
   :alt: housing-data-exploration
   :width: 65%
   
   
