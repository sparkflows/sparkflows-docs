Jetrail Data Annalysis
======================

This workflow reads in a dataset. It then Calculates the monthly trend in JetRail Dataset and annalysing using graph.

Worklow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Extract date time field.
* Calculate count per months.
* Execute query for months.
* prints the results.
* Graphical annalysis.

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/1.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%

Reading from Dataset
---------------------

It reads from sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/2a.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%   

Extract date time field
-----------------------
It extract year and month field from date time field of timestamp using date time field extract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/3a.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60% 
   
Calculate count per months
--------------------------
It calculate count per months using query by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/4a.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Execute query for months
------------------------

It execute query for grouping and selecting required fields calculate sum of counts by SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/5a.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Prints the Results
------------------

It prints the results after executing  sql query for months.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/6.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/6a.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Graphical annalysis
---------------------

It will graphically represented month with count using GraphValue Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/jetrail-data-annalysis/7a.PNG
   :alt: Jetrail Data Annalysis
   :align: center
   :width: 60%
