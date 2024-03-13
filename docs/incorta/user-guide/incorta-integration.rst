Incorta Integration
====================
Sparkflows allows reading the data from an Incorta object store using a storage connection and do the data-cleaning, data transformation, data profiling, feature-engineering and model build with a no-code workflow designer. It allows users to submit the workflow to the Incorta Spark cluster with the Incorta Chidori compute connection and saves the results and model to the Incorta object-store.

This document outlines the steps for integrating Sparkflows with Incorta. 

Integration Components
---------------------

* Storage Connection i.e. Incorta Tables.
* Compute Connection i.e. Chidori.
* Incorta MV with Pyspark code.

Step 1: Setting-up Storage Connection to Incorta Object Store
------------------------------------------
#. Navigate to **Administration -> Configuration -> Global Connection**.
#. Create a connection to the Incorta Object Store.

   .. figure:: ../../_assets/incorta/Incorta-StorageConnection-General-II.png
      :alt: incorta_integration
      :width: 60%
    
   .. figure:: ../../_assets/incorta/Incorta-StorageConnection-Incorta-II.png
      :alt: incorta_integration
      :width: 60%


Step 2: Create the Workflow
-----------------------
#. Navigate to **workflow editor**.
#. Create the workflow by selecting the connection and Incorta table.

   .. figure:: ../../_assets/incorta/Workflow-I.png
      :alt: incorta_integration
      :width: 60%   

   **Note:** In the above example, the workflow reads from an Incorta object store, transforms the selected columns to doubletype, performs feature extraction and transformation and builds the randomforest classification model.

Step 3: Execute the Workflow and View Results 
---------------------------
#. Execute the workflow on **Incorta Spark Cluster** with selected **Chidori Connection**.

   .. figure:: ../../_assets/incorta/Workflow-II.png
      :alt: incorta_integration
      :width: 60%   
   
#. Access the **Execution Page** to review results.
   
   .. figure:: ../../_assets/incorta/Workflow-III.png
      :alt: incorta_integration
      :width: 60%   
   

Step 4: View Model Summary
-------------------------------
In the Model Registry hyperparameter, summary, metrics, feature importance and model path stored for the executed model. It allows users to **compare** the different models and **deploy** the model to **Kubeflow**. And also **register** the model to **MLflow**. (MLflow and Kubeflow configured in Configuration MLOps Page).

   .. figure:: ../../_assets/incorta/Model-I.png
      :alt: incorta_integration
      :width: 60%   
   
   

   .. figure:: ../../_assets/incorta/Model-II.png
      :alt: incorta_integration
      :width: 60%   
   

Step 5: Generate Pyspark Code
-----------------------------
PySpark Code can be generated for workflow and executed on any spark environment by following the below steps:

#. Expand the three-dots menu and click on **Generate Pyspark Code**.

   .. figure:: ../../_assets/incorta/Generate-Code.png
      :alt: incorta_integration
      :width: 60%   
#. Click on **Copy to Clipboard** button to copy the generated code to any Spark environment.

   .. figure:: ../../_assets/incorta/Copy-Code.png
      :alt: incorta_integration
      :width: 60%   








