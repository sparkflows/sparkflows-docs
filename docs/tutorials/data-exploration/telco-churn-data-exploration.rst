Telco Churn Data Exploration
============================


Data Profiling is extremely helpful in understanding the data. Fire Insights provides a number of processors for users to profile their data.


Workflow for Data Profiling
----------------------------


Below is a workflow which profiles the Telco Churn dataset.


.. figure:: ../../_assets/tutorials/data-exploration/Telco-WF.png
   :alt: Concat Columns
   :width: 65%
   
Input Telco Churn Data
---------------------

The input dataset looks like below:


.. figure:: ../../_assets/tutorials/data-exploration/input.png
   :alt: Concat Columns
   :width: 65%
   
Workflow Execution Result
-------------------------

When the above workflow is executed, it produces the below results. A good thing about Fire Insights is that the Data Profiling runs in a distributed fashion. So, whatever be the number of records in the input dataset, it scales seamlessly.


Summary Statistics
-------------------

.. figure:: ../../_assets/tutorials/data-exploration/summary-output.png
   :alt: Concat Columns
   :width: 65%
   
Counts by Churned Column
-------------------------

.. figure:: ../../_assets/tutorials/data-exploration/graph-grp-by-col-output.png
   :alt: Concat Columns
   :width: 65%
   
Graph of counts of various attributes for Churned and Not Churned customers
-----------------------------------------------------------------------------


.. figure:: ../../_assets/tutorials/data-exploration/graph-values-output.png
   :alt: Concat Columns
   :width: 65%
   
Percentage distribution of label values
---------

.. figure:: ../../_assets/tutorials/data-exploration/pie-chart.png
   :alt: Concat Columns
   :width: 35%
   

Correlation Matrix
--------------------


.. figure:: ../../_assets/tutorials/data-exploration/correlation-matrix.png
   :alt: Concat Columns
   :width: 50%
 


   
   

