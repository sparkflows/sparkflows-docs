WHO Life Expectancy Data Cleaning
=========================

This workflow shows how to clean the WHO Life Expectancy Dataset with Sparkflows.

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
   
Imputing Mean Values to Replace Remaining NULL Values
----------------
``Imputing with Mean Value`` Processor imputes the mean value of each column in place of NULL values in each column.


Processor Configuration
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/ImputeMean_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

Indexing String Values into Numeric Values
---------------

``String Indexer`` Processor creates an numeric index for string values and creates a new column with the created index values. 


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/StringIndex_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/StringIndex_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Creating a Flag for Potentially Inaccurate Data
---------------

``Case When`` Processor creates a new column and populates it with values based on user-set conditions. 


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/CaseWhen_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/CaseWhen_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%


Creating a Flag for Outliers in Output Column
---------------

``Flag Outlier`` Processor creates a new column to indicate whether values in the given column are outliers based on the box and whisker method. 


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/FlagOutlier_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/who-data-cleaning/FlagOutlier_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
