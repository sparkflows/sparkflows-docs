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
* SQL query to get the status.
* Visualize the status count.

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/Flights-wf.png
   :alt: Analyze Flights Delays
   :width: 60%
   
Reading from Dataset
---------------------

It reads the Dataset Files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/read-config.png
   :alt: Analyze Flights Delays
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/read-output.png
   :alt: Analyze Flights Delays
   :width: 60%
   

Cast Column to Double
---------------------------------

It casts for the new datatype double using the CastColumn Type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/castcolumn-config.png
   :alt: Analyze Flights Delays
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/castcolumn-output.png
   :alt: Analyze Flights Delays
   :width: 60%

Cast Column to String
---------------------------------

It casts for the new Datatype string using the CastColumn Type Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/castcolumnstring-config.png
   :alt: Analyze Flights Delays
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/castcolumnstring-output.png
   :alt: Analyze Flights Delays
   :width: 60%
 
   
Execute the SQL Queries   
-------------------------

It executes the SQL Queries with the given conditions.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/sql-config.png
   :alt: Analyze Flights Delays
   :width: 60%
   


Visualize the status count
------------------

It visualizes the status count using the GraphGroupByColumn Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/graphgrpbycol-config.png
   :alt: Analyze Flights Delays
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/analyze-flights-delays/graphgrpbycol-output.png
   :alt: Analyze Flights Delays
   :width: 60%

