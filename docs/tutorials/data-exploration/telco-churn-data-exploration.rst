Telco Churn Data Exploration
============================


Data Profiling is extremely helpful in understanding the data. Fire Insights provides a number of processors for users to profile their data.


Workflow for Data Profiling
----------------------------


Below is a workflow which profiles the Telco Churn Dataset.


.. figure:: ../../_assets/tutorials/data-exploration/1.PNG
   :alt: Concat Columns
   :width: 90%
   
Input Telco Churn Data
---------------------

The input dataset looks like below:


.. figure:: ../../_assets/tutorials/data-exploration/2.PNG
   :alt: Concat Columns
   :width: 90%
   
Workflow Execution Result
-------------------------

When the above workflow is executed, it produces the below results. The good thing about Fire Insights is that the Data Profiling runs in a distributed fashion. So, whatever the number of records in the input dataset, it scales seamlessly.


Summary Statistics
-------------------

.. figure:: ../../_assets/tutorials/data-exploration/3.PNG
   :alt: Concat Columns
   :width: 90%
   
Counts by Churned Column
-------------------------

.. figure:: ../../_assets/tutorials/data-exploration/4.PNG
   :alt: Concat Columns
   :width: 90%
   
Graph of counts of various attributes for Churned and Not Churned customers
-----------------------------------------------------------------------------


.. figure:: ../../_assets/tutorials/data-exploration/churned-notchurned-customers.png
   :alt: Concat Columns
   :width: 70%
   
Correlation Matrix
--------------------


.. figure:: ../../_assets/tutorials/data-exploration/co-relation-matrix.png
   :alt: Concat Columns
   :width: 70%
 


   
   

