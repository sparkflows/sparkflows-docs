Data Cleaning
=============

This workflow cleans the input data. 

It also:

* Handles null values

* Replaces ``N/Y`` values etc. with ``0/1``


Workflow
-------

The below workflow:

* Reads data from a dataset
* Handles the null values by imputing the missing values with the constant value provided in the specified columns
* Converts Strings to Integer Indexes
* Converts Gender to Integer Values
* Replaces Gender and Family with ``0/1``


.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture1.PNG
   :alt: DataCleaning
   :width: 90%
   
Reading from Dataset
---------------------

``DatasetCSV`` reads in the input Dataset file and creates DataFrame from it.


Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture2.PNG
   :alt: DataCleaning
   :width: 90%   
   
   
Handling Null Values
------------

``ReplaceMissingValueWithConstant`` Processor handles the null values by imputing the missing values with the constant value provided in the specified columns.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture3.PNG
   :alt: DataCleaning
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture4.PNG
   :width: 90%
  

Convert Strings to Integer Indexes
------------

``StringIndexer`` Processor encodes a string type column to a column of label indices.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture5.PNG
   :alt: DataCleaning
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture6.PNG
   :width: 90%

   
Convert Gender to Integer Values
------------

``CaseWhen`` Processor sets values for the variables based on conditions, as shown below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture7.PNG
   :alt: DataCleaning
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture8.PNG
   :width: 90%
   
Replace Gender and Family with 0/1
------------

``FindAndReplaceUsingRegexMultiple`` processor sets values for the variables based on conditions, as shown below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture9.PNG
   :alt: DataCleaning
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture10.PNG
   :alt: DataCleaning
   :width: 90%
   
   
Prints the Results
------------------

It prints the first few records onto the screen.
