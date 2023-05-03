
ClickStream Analysis
=====================

This workflow reads in the Omniture clickstream data, product and users data. It cleans and joins them to get the denormalized clean dataset. It then performs the following analysis:

- Finds number of users by state and displays them on a map.
- Finds number of users by age and displays them on a graph.
   
Workflow
-------

The below workflow:

.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/clickstream-wf.png
   :alt: ClickStream Analysis
   :width: 60%
   
Sample Data
---------------------

Omniture Clickstream Data
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/omniture-data.png
   :alt: ClickStream Analysis
   :width: 60%
   
Product Data
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/product-data.png
   :alt: ClickStream Analysis
   :width: 60%
   
Users Data
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/users-data.png
   :alt: ClickStream Analysis
   :width: 60%
 
 
Count number of users by ``state`` and displays it on map
---------------------------------------------------
Configuration 
^^^^^^^^^^^^^
.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/graphregiongeo-config.png
   :alt: ClickStream Analysis
   :width: 60%
  
   
Result
^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/graphregiongeo-output.png
   :alt: ClickStream Analysis
   :width: 60%


Count number of users by ``age`` and display it as a line chart
---------------------------------------------------

Caluclation 
^^^^^^^^^^^^^
.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/groupbyage-config.png
   :alt: ClickStream Analysis
   :width: 60%
   
   
Configuration
^^^^^^^^^^^^^
.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/graphbyage-config.png
   :alt: ClickStream Analysis
   :width: 60%
   
Result
^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/clickstream-analysis/graphbyage-output.png
   :alt: ClickStream Analysis
   :width: 60%
   
