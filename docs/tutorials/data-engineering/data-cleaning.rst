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


.. figure:: ../../_assets/tutorials/data-engineering/
   :alt: DataCleaning
   :align: center
   :width: 60%
   
Reading from Dataset
---------------------

It reads in the input Dataset File.


Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :alt: DataCleaning
   :align: center
   :width: 60%   
   
   
Handling Null Values
------------

It handles the null values by imputing the missing values with the constant value provided in the specified columns.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :align: center
   :width: 60%
  

Convert Strings to Integer Indexes
------------

``  StringIndexer  `` encodes a string type columns to a column of label indices

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :align: center
   :width: 60%

.. figure:: ../../_assets/tutorials/data-engineering/
   :align: center
   :width: 60%

.. figure:: ../../_assets/tutorials/data-engineering/
   :align: center
   :width: 60%
   
Convert Gender to Integer Values
------------

``  CaseWhen  `` sets values based on conditions as shown below

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :align: center
   :width: 60%
   
Replace Gender and Family with 0/1
------------

``  FindAndReplaceUsingRegexMultiple  `` sets values based on conditions as shown below

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :alt: DataCleaning
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/
   :align: center
   :width: 60%
   
   
Prints the Results
------------------

It prints the first few records onto the screen.
