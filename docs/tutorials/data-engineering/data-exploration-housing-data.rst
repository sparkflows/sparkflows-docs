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

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/1.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Reading Housing Dataset
---------------------

``DatasetStructured`` Processor creates a Dataframe of your dataset named ``Housing Training`` by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature.

Processor Output
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/2.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   

Dropping the rows with null values
--------------

``DropRowsWithNull`` Processor drops the rows with null values.

Processor Configuration
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/3.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Filter by string length
----------------
``FilterByStringLength`` Processor filters the rows within the provided string length.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/4.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/5.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Convert Age to Integer
---------------------

``CastColumnType`` Processor performs conversion of Age to integer type.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/6.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/7.PNG
   :alt: titanic-data-cleaning
   :width: 90%

Get Rows of Interest
---------------

``RowFilter`` Processor filters the data based on provided conditions as below:


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/8.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/9.PNG
   :alt: titanic-data-cleaning
   :width: 90%



Prints the result
-------------

It prints the first few records onto the screen.
