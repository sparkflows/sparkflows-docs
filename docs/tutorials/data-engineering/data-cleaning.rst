Data Cleaning
=============

This workflow cleans the input data. It does the following:

* Handles null values
* Replaces N/Y values etc. with 0/1


Workflow
-------

Below is the workflow. It does the following:

* Reads data from a dataset
* Handles the null values by imputing the missing values with the constant value provided in the specified columns
* Convert Strings to Integer Indexes
* Convert Gender to Integer Values
* Replace Gender and Family with 0/1


.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture1.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%
   
Reading from Dataset
---------------------

``DatasetCSV`` reads in the input Dataset file and creates DataFrame from it.


Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture2.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%   
   
   
Handling Null Values
------------

``ReplaceMissingValueWithConstant`` processor handles the null values by imputing the missing values with the constant value provided in the specified columns.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture3.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture4.PNG
   :align: center
   :width: 60%
  

Convert Strings to Integer Indexes
------------

``StringIndexer`` processor encodes a string type column to a column of label indices.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture5.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture6.PNG
   :align: center
   :width: 60%

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture7.PNG
   :align: center
   :width: 60%

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture8.PNG
   :align: center
   :width: 60%
   
Convert Gender to Integer Values
------------

``CaseWhen`` processor sets values for the variables based on conditions, as shown below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture9.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture10.PNG
   :align: center
   :width: 60%
   
Replace Gender and Family with 0/1
------------

``FindAndReplaceUsingRegexMultiple`` processor sets values for the variables based on conditions, as shown below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture11.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-cleaning/Capture12.PNG
   :alt: DataCleaning
   :align: center
   :width: 60%
   
   
Prints the Results
------------------

It prints the first few records onto the screen.
