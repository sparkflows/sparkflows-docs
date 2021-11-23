Case When
=============

This tutorial will cover how to use the Case When processor using an example sales data. The data has been taken from Kaggle courtesy of the World Health Organization.  

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
We use the ``Execute In Loop`` processor to have the nodes that follow execute repeatedly on data corresponding to different product. The ``Execute In Loop`` processor creates a list of all the unique values in the selected column and filters all values except for one at a time. This allows us to create a model for each product without editting the workflow or using a row filter. In this case we are using this processor to calculate seperate summary statistics for each Product Line without filtering the data for each seperately. For the purposes of this tutorial, distinct values that will be used to loop the workflow have also been displayed using the ``Execute In Loop`` processor. 


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
   
   
