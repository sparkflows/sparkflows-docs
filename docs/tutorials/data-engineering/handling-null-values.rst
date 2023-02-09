Handling Null Values
====================

This sample workflow removes null values from the input dataset.


Workflow
--------

The below workflow:

* Reads data from a CSV file.
* Replaces null values in certain columns with constant values.
* Converts certain columns to 0/1 based on their value. It does it in 3 different ways.

  * Using StringIndexer Processor.
  * Using CaseWhen Processor.
  * Using FindAndReplace using Regex Processor.

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/7.PNG
   :alt: Handling Null Values
   :width: 70%
   
Reading from CSV File
---------------------

It reads in the CSV file data with-nulls.csv.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/8.PNG
   :alt: Handling Null Values
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/9.PNG
   :alt: Handling Null Values
   :width: 80%   
   
Replacing null values
---------------------

It replaces null values in certain columns with user defined constant values.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/10.PNG
   :alt: Handling Null Values
   :width: 80%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/11.PNG
   :alt: Handling Null Values
   :width: 80%   
   
Converting to 0/1 using StringIndexer
---------------------

It converts strings like Y/N to 0/1 for the specified columns using the StringIndexer Processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/12.PNG
   :alt: Handling Null Values
   :width: 80%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/13.PNG
   :alt: Handling Null Values
   :width: 80%
   

Converting to 0/1 using CaseWhen
---------------------

It converts strings like Y/N to 0/1 for the specified columns using the CaseWhen Processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/14.PNG
   :alt: Handling Null Values
   :width: 80%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/15.PNG
   :alt: Handling Null Values
   :width: 80%
   

Converting to 0/1 using FindAndReplaceUsingRegex
---------------------

It converts strings like Y/N to 0/1 for the specified columns using the FindAndReplaceUsingRegex Processor.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/16.PNG
   :alt: Handling Null Values
   :width: 80%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/17.PNG
   :alt: Handling Null Values
   :width: 80%
   

