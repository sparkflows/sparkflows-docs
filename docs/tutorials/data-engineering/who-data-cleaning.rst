WHO Life Expectancy Data Cleaning/Wrangling
=========================

This workflow shows how to wrangle the WHO Life Expectancy Dataset with Sparkflows.

Workflow
--------
The below workflow: 

* Reads the WHO Life Expectancy dataset
* Finds the number of NULL values in each column
* Drops columns with an unacceptable proportion of NULL values
* Imputes mean values in the place of remaining NULL values
* Indexes string type variables into numeric values for use in modelling
* Flags rows with potentially inaccurate data
* Flags outliers in the output column (Life Expectancy)

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/Overview.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Reading WHO Life Expectancy Dataset
---------------------

``DatasetStructured`` Processor creates a Dataframe of your dataset named ``WHO Life Expectancy`` by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature.

Processor Output
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/DatasetStructured_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   

Counting Number of NULL Values in Columns
--------------

``Null Values in Column`` Processor counts the number and percentage of NULL values in the selected columns.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/NullValues_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/NullValues_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Dropping Columns With Too Many NULL Values
----------------
``Drop Columns`` Processor creates a new dataframe, excluding the columns selected.


Processor Configuration
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/DropColumns_Config.PNG
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
