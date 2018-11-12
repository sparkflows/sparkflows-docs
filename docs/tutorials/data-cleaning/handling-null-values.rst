Handling Null Values
====================

This example removes null values from the input dataset.


Workflow
--------

Below is the workflow. It does the following:

* Reads data from a CSV file.
* Replaces null values from certain columns with Constant Values.
* Converts certain columns to 0/1 based on their value. It does it in 3 different ways.

  * Using StringIndexer
  * Using CaseWhen
  * Using FindAndReplaceUsingRegex

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/1.png
   :alt: Handling Null Values
   :align: center
   :width: 60%
   
Reading from CSV File
---------------------

Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/2.png
   :alt: Handling Null Values
   :align: center
   :width: 60%
   
Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/2a.png
   :alt: Handling Null Values
   :align: center
   :width: 60%   
   
Replacing null values
---------------------

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/3.png
   :alt: Handling Null Values
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/3a.png
   :alt: Handling Null Values
   :align: center
   :width: 60%   
   
Converting to 0/1 using StringIndexer
---------------------

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/4.png
   :alt: Handling Null Values
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/4a.png
   :alt: Handling Null Values
   :align: center
   :width: 60%
   

Converting to 0/1 using CaseWhen
---------------------

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/5.png
   :alt: Handling Null Values
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/5a.png
   :alt: Handling Null Values
   :align: center
   :width: 60%
   

Converting to 0/1 using FindAndReplaceUsingRegex
---------------------

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/6.png
   :alt: Handling Null Values
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/handling-null-values/6a.png
   :alt: Handling Null Values
   :align: center
   :width: 60%
   

