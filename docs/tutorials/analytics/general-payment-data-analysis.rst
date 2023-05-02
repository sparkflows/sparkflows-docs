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

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/WF.png
   :alt: General Payment Data Analysis
   :width: 60%

Reading from Dataset
---------------------

It reads from sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/read-config.png
   :alt: General Payment Data Analysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/read-output.png
   :alt: General Payment Data Analysis
   :width: 60%
 
 
Summary of Transactions
-----------------------

It finds stats on the amount of each transaction using the Summary Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/summary-config.png
   :alt: General Payment Data Analysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/summary-output.png
   :alt: General Payment Data Analysis
   :width: 60%
   
Number of Transaction per State
-------------------------------

It finds the number of transactions per State by using the SQL Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/sql-config.png
   :alt: General Payment Data Analysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/sql-output.png
   :alt: General Payment Data Analysis
   :width: 60%
   
Prints the Result
------------------
 It prints the result of output getting from SQL Node.
 
Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/print-config.png
   :alt: General Payment Data Analysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/general-payment-data-analysis/print-output.png
   :alt: General Payment Data Analysis
   :width: 60% 



