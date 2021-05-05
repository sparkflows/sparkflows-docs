NYC Taxidata Analysis
======================

This workflow reads in a sample dataset. It then analyses average speed of taxis at each hour with sample data and prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a dataset.
* Extracts hour from pickup time.
* Calculates the speed per hour.
* Calculates the average speed per hour.
* Prints the results.
* Sort data by column.
* Displays average speed per hour on chart.

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/1.png
   :alt: NYC Taxidata Annalysis
   :width: 90%

Reading from Dataset
---------------------

It reads sample Dataset files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/2.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/2a.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Extract hour from pickup time
-----------------------------

It extracts hour from pickup time using datetimefieldextract Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/3.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/3a.png
   :alt: NYC Taxidata Annalysis
   :width: 60%

Calculate the speed per hour
-----------------------------

It calculates the speed per hour using SQL Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/4.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/4a.png
   :alt: NYC Taxidata Annalysis
   :width: 60%

Calculate the average speed per hour
-----------------------------

It calculates the average speed per hour using GroupBy Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/5.png
   :alt: NYC Taxidata Annalysis
   :width: 60%

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/5b.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/5a.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Prints the results
------------------

It will print the result with the output of GroupBy Node.

Sort data by column
------------------

It will sort the result by selected column and it's specified order ASC/DESC using SortBy Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/6.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/6a.png
   :alt: NYC Taxidata Annalysis
   :width: 60%

Analyze using Chart Graph
-------------------------

It displays average speed per hour on chart using Graphvalue Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/7.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/7a.png
   :alt: NYC Taxidata Annalysis
   :width: 60%
