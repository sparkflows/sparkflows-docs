Case When
=============

This tutorial will cover how to use the Case When processor using aggregate health data. The data has been taken from Kaggle courtesy of the World Health Organization.  

.. contents::
   :depth: 2


Workflow Overview
-------------------
The below workflow: 

* Uses the Case When processor to create a new variable
* Creates a histogram to show the distribution of a variable

.. figure:: ../../_assets/tutorials/data-engineering/case-when/Overview.PNG
   :alt: titanic-data-cleaning
   :width: 70%
   
   
Using Case When
----------------------------
We use the ``Case When`` processor to create a new columns based on values from another column(or multiple other columns).  


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/case-when/CaseWhen_Config.PNG
   :alt: titanic-data-cleaning
   :width: 70%
   

Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/case-when/CaseWhen_Output.PNG
   :alt: titanic-data-cleaning
   :width: 70%
   

Creating a Histogram
-------------------------------
We use the ``Histogram`` processor to calculate basic summary statistics for numeric variables. In this case we are using it to calculate separate statistics for each Product Line. The output is showing a sample of the statistics that were generated, summary statistics were generated for every distinct Product Line. 


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/case-when/Histogram_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/case-when/Histogram_Output.PNG
   :alt: titanic-data-cleaning
   :width: 70%
   
   
