Data Cleaning
=============

This workflow cleans the input data. 

It also:

* Handles null values.

* Replaces ``N/Y`` values etc. with ``0/1``.


Workflow
-------

The below workflow:

* Reads data from a dataset.
* Handles the null values by imputing the missing values with the constant value provided in the specified columns.
* Converts Strings to Integer Indexes.
* Converts Gender to Integer Values.
* Replaces Gender and Family with ``0/1``.


.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/1.PNG
   :alt: DataCleaning
   :width: 65%
   
Reading from Dataset
---------------------

``DatasetCSV`` reads in the input Dataset file and creates DataFrame from it.


Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/2.PNG
   :alt: DataCleaning
   :width: 65%   
   
   
Handling Null Values
------------

``ReplaceMissingValueWithConstant`` Processor handles the null values by imputing the missing values with the constant value provided in the specified columns.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/3.PNG
   :alt: DataCleaning
   :width: 65%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/4.PNG
   :width: 65%
  

Convert Strings to Integer Indexes
------------

``StringIndexer`` Processor encodes a string type column to a column of label indices.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/5.PNG
   :alt: DataCleaning
   :width: 65%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/6.PNG
   :width: 65%

   
Convert Gender to Integer Values
------------

``CaseWhen`` Processor sets values for the variables based on conditions, as shown below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/7.PNG
   :alt: DataCleaning
   :width: 65%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/8.PNG
   :alt: DataCleaning
   :width: 65%
   
Replace Gender and Family with 0/1
------------

``FindAndReplaceUsingRegexMultiple`` Processor sets values for the variables based on conditions as below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/9.PNG
   :alt: DataCleaning
   :width: 65%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/10.PNG
   :alt: DataCleaning
   :width: 65%
   
   
Prints the Results
------------------

It prints the first few records onto the screen.
