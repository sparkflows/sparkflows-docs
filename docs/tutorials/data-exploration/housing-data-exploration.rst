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
   :width: 60%
   
Reading Housing Dataset
---------------------

``DatasetStructured`` Processor creates a Dataframe of your dataset named ``Housing Training`` by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature.

Processor Output
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/2.PNG
   :alt: titanic-data-cleaning
   :width: 60%
   

Calculate Summary Statistics
----------------
``Summary Statistics`` Processor calculates summary statistics for the selected variables.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/3.PNG
   :alt: titanic-data-cleaning
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/4.PNG
   :alt: titanic-data-cleaning
   :width: 60%


Create Histogram Graph
----------------
``HistoGram`` Processor creates a histogram to show distribution by count of Sale Price.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/5.PNG
   :alt: titanic-data-cleaning
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/6.PNG
   :alt: titanic-data-cleaning
   :width: 60%
   
Graph Values
---------------------

``Graph Values`` Processor graphs the relationship between Sale Price and Basement Sqaure Footage.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/7.PNG
   :alt: titanic-data-cleaning
   :width: 60%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/8.PNG
   :alt: titanic-data-cleaning
   :width: 60%

Plot Correlation Matrix
---------------

``Correlation`` Processor creates a correlation matrix of selected variables and plots the results.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/9.PNG
   :alt: titanic-data-cleaning
   :width: 60%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/10.PNG
   :alt: titanic-data-cleaning
   :width: 60%



Flag Outliers and Create Graph
----------------
``Flag Outlier`` Processor creates a new flag column to mark outliers and ``Graph Group by Column`` Processor graphs the count in each category.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/11.PNG
   :alt: titanic-data-cleaning
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-exploration-housing-data/12.PNG
   :alt: titanic-data-cleaning
   :width: 60%
   
   
