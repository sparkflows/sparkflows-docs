Jetrail Data Analysis
======================

This workflow reads in a dataset. It then calculates the monthly trend in the JetRail Dataset and performs further analysis using the charts.

Workflow
-------

The below workflow:

* Reads data from a sample dataset.
* Extracts the Datetime Field.
* Calculates the count per month.
* Executes the query for months.
* Prints the result.
* Makes Graphical analysis.

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/1.png
   :alt: Jetrail Data Annalysis
   :width: 100%

Reading from Dataset
---------------------

It reads from sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2a.png
   :alt: Jetrail Data Annalysis
   :width: 90%   

Extract date time field
-----------------------
It extracts year and month field from date time field of timestamp using date time field extract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3a.png
   :alt: Jetrail Data Annalysis
   :width: 90% 
   
Calculate count per month
--------------------------
It calculates count per month using query by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4a.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Calculate sum of counts per month
------------------------

It executes query for grouping and selecting required fields, calculates sum of counts by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5a.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Prints the Results
------------------

It prints the results after executing  SQL Query
   
Graphical analysis
---------------------

It will graphically represent month with count using GraphValue Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7.png
   :alt: Jetrail Data Annalysis
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7a.png
   :alt: Jetrail Data Annalysis
   :width: 90%
