Analyze Flights Delays
=====================

This workflow reads in a dataset. It then analyzes flights delay with sample datasets and prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Prints the sample datasets results.
* Column to be cast for new datatype double.
* Column to be cast for new datatype string.
* Updates the column name of datatype string.
* Prints the result of data updating after stringindexer Node.
* Executes the SQL queries with the given conditions.
* Prints the results.

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/1.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Reading from Dataset
---------------------

It reads Dataset files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/2.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/2a.png
   :alt: Analyze Flights Delays
   :width: 90%
   

Column to be cast for new datatype double
---------------------------------

It casts for new datatype double using castcolumn type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/4.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/4a.png
   :alt: Analyze Flights Delays
   :width: 90%

Column to be cast for new datatype string
---------------------------------

It casts for new datatype string using castcolumn type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/5.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/5a.png
   :alt: Analyze Flights Delays
   :width: 90%

Updates the column name of datatype string
----------------------------------------

It updates the column name of datatype string using stringindexer type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/6.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/6a.png
   :alt: Analyze Flights Delays
   :width: 90%
 
   
Executes the SQL queries   
-------------------------

It executes the SQL queries with the given conditions.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/8.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/8a.png
   :alt: Analyze Flights Delays
   :width: 90%

Prints the Results
------------------

It prints the results after satisfied condition by   sql   queries.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/9.png
   :alt: Analyze Flights Delays
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/9a.png
   :alt: Analyze Flights Delays
   :width: 90%

