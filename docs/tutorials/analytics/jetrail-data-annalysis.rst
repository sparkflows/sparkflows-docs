Jetrail Data Analysis
======================

This workflow reads in a dataset. It then calculates the monthly trend in JetRail Dataset and annalyses using graph.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Extracts date time field.
* Calculates count per month.
* Executes query for months.
* Print the results.
* Graphical analysis.

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/1.png
   :alt: Jetrail Data Annalysis
   :width: 60%

Reading from Dataset
---------------------

It reads from sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2a.png
   :alt: Jetrail Data Annalysis
   :width: 60%   

Extract date time field
-----------------------
It extracts year and month field from date time field of timestamp using date time field extract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3a.png
   :alt: Jetrail Data Annalysis
   :width: 60% 
   
Calculate count per month
--------------------------
It calculates count per month using query by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4a.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Execute query for months
------------------------

It executes query for grouping and selecting required fields, calculates sum of counts by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5a.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
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
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7a.png
   :alt: Jetrail Data Annalysis
   :width: 60%
