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

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/WF.png
   :alt: Jetrail Data Annalysis
   :width: 60%

Reading from Dataset
---------------------

It reads from the sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/read-config.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/read-output.png
   :alt: Jetrail Data Annalysis
   :width: 60%   

Extract Datetime Field
-----------------------
It extracts the year and the month field from the Datetime Field of timestamp using Datetime Field Extract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/extract-datetime-config.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/extract-datetime-output.png
   :alt: Jetrail Data Annalysis
   :width: 60% 
   
Calculate Count per Month
--------------------------
It calculates the count per month using the query by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/sql-config.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/sql-output.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Calculate Sum of Counts per Month
------------------------

It executes query for grouping and selecting the required fields, and calculates the sum of counts by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/count-config.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/count-output.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Prints the Result
------------------

Prints the result of the previous SQL node.

Processor Configuration
^^^^^^^^^^^^^^^^^^
.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/print-config.png
   :alt: Jetrail Data Annalysis
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/print-output.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Graphical Analysis
---------------------

It will graphically represent the month with the count using the GraphValues Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/graph-values-config.png
   :alt: Jetrail Data Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/graph-values-output.png
   :alt: Jetrail Data Annalysis
   :width: 60%
