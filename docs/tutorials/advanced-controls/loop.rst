Loop
=============

This tutorial will cover how to use the loop processor using an example sales data. The data has been taken from Kaggle courtesy of Assert Solutions.  

.. contents::
   :depth: 2


Workflow Overview
-------------------
The below workflow: 

* Creates a loop to seperate the data by Product Line
* Calculates summary statistics of the sales values

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Modelling_Overview.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
Creating Loop
----------------------------
We use the ``Execute In Loop`` processor to have the nodes that follow execute repeatedly on data corresponding to different product. The ``Execute In Loop`` processor creates a list of all the unique values in the selected column and filters all values except for one at a time. This allows us to create a model for each product without editting the workflow or using a row filter. In this case we are using this processor to calculate seperate summary statistics for each Product Line without filtering the data for each seperately. For the purposes of this tutorial, distinct values that will be used to loop the workflow have also been displayed using the ``Execute In Loop`` processor. 


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Loop_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   

Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Regression_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   

Calculating Summary Statistics
-------------------------------
We use the ``Summary Statistics`` processor to drop rows which are unnecessary from the model results before saving. In this case we are only interested in the Coefficient related to Price, so we drop all other rows.  


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Row_Filter_Config.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Regression_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Regression_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Regression_Output.PNG
   :alt: titanic-data-cleaning
   :width: 90%
   
   
   
