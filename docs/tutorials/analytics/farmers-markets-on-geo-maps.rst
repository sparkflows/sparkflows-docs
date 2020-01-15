Farmers Markets On Geo Maps
===========================

This workflow reads in a dataset. It then plots number of Farmers Market by City and by State on a Graph.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Executes SQL Query for state count.
* Prints the result after executing query for state counts.
* Plots Graph for farmers with state counts.
* Executes SQL Query for city counts.
* Plots Graph for farmers with city counts.

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/1.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%

Reading from Dataset
---------------------

It reads sample Dataset files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/2.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/2a.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Execute SQL Query
-------------------

It Executes SQL Query for state count from the SQL node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/3.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/3a.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Prints the Results
------------------

It prints the results after executing query for state counts by SQL Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/4.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/4a.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%   
   
Analyze using Graph
--------------------

It plots Graph for farmers with state counts using RegionGeoGraph Processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/5.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/5a.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60% 

Execute SQL Query
-------------------

It executes SQL Query for City count from the SQL node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/6.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/6a.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%

Analyze using Graph
--------------------

It plots Graph for farmers with City counts using RegionGeoGRaph Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/7.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/7a.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%

