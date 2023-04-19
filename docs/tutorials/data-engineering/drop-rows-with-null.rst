
Drop Rows With Null
===================

This sample workflow drops or filters the rows containing any null values from the input dataset.


Workflow
--------

The below workflow:

* Reads data from a CSV File.
* Drops rows having any null values in any of the columns.

.. figure:: ../../_assets/tutorials/data-cleaning/drop-rows-with-null/dropnull-wf.png
   :alt: Drop Rows With Null
   :width: 70%
   
Reading from CSV File
---------------------

It reads data from a CSV File. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/drop-rows-with-null/read-config.png
   :alt: Drop Rows With Null
   :width: 80%
   

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/drop-rows-with-null/read-output.png
   :alt: Drop Rows With Null
   :width: 80% 
   
Dropping rows with null
----------------------

It drops the rows which contain any null value.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/drop-rows-with-null/dropnull-config.png
   :alt: Drop Rows With Null
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/drop-rows-with-null/dropnull-output.png
   :alt: Drop Rows With Null
   :width: 80%
   
   
