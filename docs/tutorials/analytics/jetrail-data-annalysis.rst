Jetrail Data Analysis
======================

This workflow reads in a dataset. It then calculates the monthly trend in the JetRail Dataset and performs further analysis using the charts.

Workflow
-------

The below workflow:

* Reads the data from a sample dataset.
* Extracts the Datetime Field.
* Calculates the count per month.
* Executes the query for months.
* Prints the result.
* Makes Graphical analysis.

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/1.png
   :alt: Jetrail Data Annalysis
   :width: 65%

Reading from Dataset
---------------------

It reads from the sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2a.png
   :alt: Jetrail Data Annalysis
   :width: 75%   

Extract Datetime Field
-----------------------
It extracts the year and the month field from the Datetime Field of timestamp using Datetime Field Extract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3a.png
   :alt: Jetrail Data Annalysis
   :width: 75% 
   
Calculate Count per Month
--------------------------
It calculates the count per month using the query by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4a.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Calculate Sum of Counts per Month
------------------------

It executes query for grouping and selecting the required fields, and calculates the sum of counts by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5a.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Prints the Result
------------------

Prints the result of the previous SQL node.

Processor Configuration
^^^^^^^^^^^^^^^^^^
.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/6.png
   :alt: Jetrail Data Annalysis
   :width: 75%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/6a.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Graphical Analysis
---------------------

It will graphically represent the month with the count using the GraphValue Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7.png
   :alt: Jetrail Data Annalysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7a.png
   :alt: Jetrail Data Annalysis
   :width: 75%
