Farmers Markets On Geo Maps
===========================

This workflow reads in a dataset. It then Plots number of Farmers Market by City and by State on a Graph.

Worklow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Eexecute SQL query for state count.
* Print the result after executing query for state counts.
* Plot Graph for farmers with state counts.
* Eexecute SQL query for city counts.
* Plot Graph for farmers with city counts.

.. figure:: ../../_assets/tutorials/analytics/farmers-markets-on-geo-maps/1.PNG
   :alt: Farmers Markets On Geo Maps
   :align: center
   :width: 60%

Reading from Dataset
---------------------

It reads sample Dataset file.

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
   
Eexecute SQL query
-------------------

It Eexecute SQL query for state count from the SQL node.

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

It Print the result after executing query for state counts by SQL Node.


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

It Plot Graph for farmers with state counts using RegionGeoGRaph Node.

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

Eexecute SQL query
-------------------

It Eexecute SQL query for City count from the SQL node.

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

It Plot Graph for farmers with City counts using RegionGeoGRaph Node.

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

