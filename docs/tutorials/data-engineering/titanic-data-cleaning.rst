Titanic Data Cleaning/Wrangling
=========================

This workflow shows how to wrangle the Titanic Dataset with Sparkflows.

Workflow
--------
The below workflow: 

* Reads the Titanic dataset
* Drops Rows containing Null values
* Filters the Rows for whom Age has not been specified
* Changes the data type of the Age column to integer
* Filters rows for persons of age > 30 and who are females

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/10.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Reading Titanic dataset
---------------------

``DatasetStructured`` Processor creates a Dataframe of your dataset named ``Titanic Data`` by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature.

Processor Configuration
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/11.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   

Dropping the rows with null values
--------------

``DropRowsWithNull`` Processor drops the rows with null values.

Processor Configuration
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/12.PNG
   :alt: titanic-data-cleaning
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/13.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
Filter by string length
----------------
``FilterByStringLength`` Processor filters the rows within the provided string length.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/14.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/15.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
Convert Age to Integer
---------------------

``CastColumnType`` Processor performs conversion of Age to integer type.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/16.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/17.PNG
   :alt: titanic-data-cleaning
   :width: 90%

Get Rows of Interest
---------------

``RowFilter`` Processor filters the data based on provided conditions as below:


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/18.PNG
   :alt: titanic-data-cleaning
   :width: 90%

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/19.PNG
   :alt: titanic-data-cleaning
   :width: 90%



Prints the result
-------------

It prints the first few records onto the screen.
