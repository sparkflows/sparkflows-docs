Data Exploration of Housing Data
=========================

This workflow shows how to explore the Housing Dataset from Kaggle with Sparkflows.

Workflow
--------
The below workflow: 

* Reads the Housing dataset
* Calculates summary statistics for important variables
* Creates a histogram to show the distribution of the Sale Price variable
* Creates a graph to show the relationship between Sale Price and Basement Square Footage
* Creates a matrix to show the correlation between important variables
* Flags outliers in Ground Living Area and graphs the results

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/1.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Reading Housing Dataset
---------------------

``DatasetStructured`` Processor creates a Dataframe of your dataset named ``Housing Training`` by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature.

Processor Output
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/DatasetStructured_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   

Calculate Summary Statistics
----------------
``Summary Statistics`` Processor calculates summary statistics for the selected variables.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/SummaryStats_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/SummaryStats_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Create Histogram Graph
----------------
``HistoGram`` Processor creates a histogram to show distribution by count of Sale Price.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/HistoGram_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/HistoGram_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Graph Values
---------------------

``Graph Values`` Processor graphs the relationship between Sale Price and Basement Sqaure Footage.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/GraphValues_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/GraphValues_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%

Plot Correlation Matrix
---------------

``Correlation`` Processor creates a correlation matrix of selected variables and plots the results.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/Correlation_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/Correlation_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%



Flag Outliers and Create Graph
----------------
``Flag Outlier`` Processor creates a new flag column to mark outliers and ``Graph Group by Column`` Processor graphs the count in each category.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/FlagOutlier_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/GraphOutlier_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
