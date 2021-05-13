Farmer's Markets On Geo Maps
===========================

This workflow reads in a dataset. It then plots number of Farmer's Market by city and by state on a graph.

Workflow
-------

The below workflow:

* Reads data from a sample dataset.
* Executes SQL Query for state count.
* Prints the result after executing query for the state counts.
* Plots the graph for farmers with the state counts.
* Executes SQL Query for the city counts.
* Plots graph for farmers with the city counts.

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/1.png
   :alt: Farmers Markets On Geo Maps
   :width: 90%

Reading from Dataset
---------------------

It reads sample Dataset files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/2.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/2a.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
Execute SQL Query
-------------------

It Executes SQL Query for state count from the SQL node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/3.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/3a.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
   
Analyze using Graph
--------------------

It plots Graph for farmers with state counts using RegionGeoGraph Processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/5.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/5a.png
   :alt: Farmers Markets On Geo Maps
   :width: 80% 

Execute SQL Query
-------------------

It executes SQL Query for City count from the SQL node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/6.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/6a.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%

Analyze using Graph
--------------------

It plots Graph for farmers with City counts using RegionGeoGRaph Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/7.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/7a.png
   :alt: Farmers Markets On Geo Maps
   :width: 80%

