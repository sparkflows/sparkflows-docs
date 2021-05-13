Analyze Flights Delays
=====================

This workflow reads in a flights dataset. It then analyzes the flights delay and prints the result.

Workflow
-------

The below workflow:

* Reads in the input data.
* Prints the sample datasets result.
* Casts required columns to double.
* Casts required columns to string.
* Creates index columns.
* Executes the SQL Query to find the flights which are delayed.
* Prints the result.

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/1.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Reading from Dataset
---------------------

It reads the Dataset Files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/2.png
   :alt: Analyze Flights Delays
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/2a.png
   :alt: Analyze Flights Delays
   :width: 80%
   

Cast Column to Double
---------------------------------

It casts for the new datatype double using the CastColumn Type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/4.png
   :alt: Analyze Flights Delays
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/4a.png
   :alt: Analyze Flights Delays
   :width: 80%

Cast Column to String
---------------------------------

It casts for the new datatype string using the CastColumn Type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/5.png
   :alt: Analyze Flights Delays
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/5a.png
   :alt: Analyze Flights Delays
   :width: 80%

Create Index Columns from String Columns
----------------------------------------

Create new columns with the index values from the string columns.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/6.png
   :alt: Analyze Flights Delays
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/6a.png
   :alt: Analyze Flights Delays
   :width: 80%
 
   
Execute the SQL Queries   
-------------------------

It executes the SQL Queries with the given conditions.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/8.png
   :alt: Analyze Flights Delays
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/8a.png
   :alt: Analyze Flights Delays
   :width: 80%

Print the Result
------------------

It prints the final result.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/9.png
   :alt: Analyze Flights Delays
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/9a.png
   :alt: Analyze Flights Delays
   :width: 80%

