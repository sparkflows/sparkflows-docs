Titanic Data Cleaning/Wrangling
=========================

This workflow shows how to wrangle the Titanic Dataset with Sparkflows.

Workflow
--------
This workflow performs the following steps:

* Reads the Titanic dataset
* Drops Rows containing Null values
* Filters the Rows for whom Age has not been specified
* Changes the data type of the Age column to integer
* Filters rows for persons of age > 30 and who are female

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture1.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%
   
Reading Titanic dataset
---------------------

Processor Output
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture2.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%
   

Dropping the rows with null values
--------------

Processor Configuration
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture3.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%


Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture4.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%


Filter by string length
----------------
It filters the rows within the provided string length


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture5.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture6.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%
   
Convert Age to Integer
---------------------

It performs conversion of Age to integer type

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture7.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%   

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture8.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%   


Get Rows of Interest
---------------

Filters the data based on provided conditions


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture9.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%   

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/titanic-data-cleaning/Capture10.PNG
   :alt: titanic-data-cleaning
   :align: center
   :width: 60%   




Prints the results
-------------

It prints the first few records onto the screen.
