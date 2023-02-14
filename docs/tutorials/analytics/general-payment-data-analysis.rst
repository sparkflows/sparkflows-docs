General Payment Data Analysis
=============================

This workflow reads in a dataset and then performs the detailed analytics on the general payment dataset.

Workflow
-------

The below workflow:

* Reads data from a sample dataset.
* Calculates count transactions by speciality.
* Summary of transactions. 
* Number of transactions per state.
* Prints the results.

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/1.png
   :alt: General Payment Data Analysis
   :width: 65%

Reading from Dataset
---------------------

It reads from sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/2.png
   :alt: General Payment Data Analysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/2a.png
   :alt: General Payment Data Analysis
   :width: 75%
 
 
Summary of Transactions
-----------------------

It finds stats on the amount of each transaction using the Summary Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/4.PNG
   :alt: General Payment Data Analysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/4a.png
   :alt: General Payment Data Analysis
   :width: 75%
   
Number of Transaction per State
-------------------------------

It finds the number of transactions per State by using the SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/9.PNG
   :alt: General Payment Data Analysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/9a.PNG
   :alt: General Payment Data Analysis
   :width: 75%
   
Prints the Result
------------------
 It prints the result of output getting from SQL Node.
 
Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/8.PNG
   :alt: General Payment Data Analysis
   :width: 75%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/8a.PNG
   :alt: General Payment Data Analysis
   :width: 75% 



