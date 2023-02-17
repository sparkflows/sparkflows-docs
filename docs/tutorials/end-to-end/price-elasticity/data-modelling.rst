Data Modelling - Price Elasticity
=================================

This tutorial will cover how to model price elasticity using an sample sales data. The aim of this tutorial is to calculate the price elasticity of each product separately using a Linear Regression. The data has been taken from Kaggle courtesy of Assert Solutions.  

.. contents::
   :depth: 2


Workflow Overview
-------------------
The below workflow: 

* Creates a loop to create models for each Product Code.
* Filters the data based on the number of records for each Product Code.
* Assembles features for modelling.
* Builds a linear regression model to find price elasticity.
* Filters model results to remove unecesary data.
* Saves the model results to CSV.

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Modelling_Overview.PNG
      :alt: titanic-data-cleaning
      :width: 70%
   
Creating Loop
----------------------------
We use the ``Execute In Loop`` processor to have the nodes that follow execute repeatedly on data corresponding to different product. The ``Execute In Loop`` processor creates a list of all the unique values in the selected column and filters all values except for one at a time. This allows us to create a model for each product without editing the workflow or using a row filter. 


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Loop_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Filter Product Code by Count
--------------------------------------------
We use the ``Decision`` processor to find the count of each unique values in the selected column and filter out unique values that do not meet the stated threshold. This is important when creating modelling workflows since different models will require a minimum number of data points to function correctly. 


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Decision_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Assembling Features for Modelling
-------------------
We use the ``Vector Assembler`` processor to assemble the feature columns for modelling. SparkML Regression processors require a vector for the features columns. 


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Vector_Assembler_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Building the Linear Regression Model
----------------------------------
We use the ``Linear Regression`` processor to create an OLS Regression model using SparkML. In this case we are modelling the quantity demanded to determine the relationship between price and quantity, otherwise known as elasticity. Since we are building multiple models, it is important that we are able to differentiate model results. We can use the Model Identifier option to name each model, here we are using the Product Code to label each model. 


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Regression_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Processor Output
^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Regression_Output.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Dropping Unnecessary Data for Export
--------------------------
We use the ``Row Filter`` processor to drop rows which are unnecessary from the model results before saving. In this case we are only interested in the Coefficient related to Price, so we drop all other rows.  


Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Row_Filter_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
   
Saving Data to CSV
---------------------

We use the ``Save CSV`` to save the dataset to the HDFS as a CSV file. An important option is the Save Mode, which tells the processor what to do if a file with the same name already exists in the specified location. This is especially important when a workflow is expected to be executed multiple times and for version control. In this case the workflow will be executing the ``Save CSV`` processor multiple times and we want to collect the results in a single file, so we use the Append option. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/price-elasticity/data-modelling/Save_CSV_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%


