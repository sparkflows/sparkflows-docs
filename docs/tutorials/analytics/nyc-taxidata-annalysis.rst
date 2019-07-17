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
* Displays average speed per hour on chart.

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/1.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%

Reading from Dataset
---------------------

It reads sample Dataset files.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/2.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/2a.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Extract hour from pickup time
-----------------------------

It extracts hour from pickup time using datetimefieldextract Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/3.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/3a.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%

Calculate the speed per hour
-----------------------------

It calculates the speed per hour using SQL Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/4.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/4a.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%

Calculate the average speed per hour
-----------------------------

It calculates the average speed per hour using GroupBy Node.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/5.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/5a.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Prints the results
------------------

It will print the result with the output of GroupBy Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/6.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/6a.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%

Analyze using Chart Graph
-------------------------

It displays average speed per hour on chart using Graphvalue Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/7.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/nyc-taxidata-annalysis/7a.PNG
   :alt: NYC Taxidata Annalysis
   :align: center
   :width: 60%
