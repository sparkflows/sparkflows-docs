Configuring Pipelines
======================

Sparkflows uses Apache Airflow for executing Pipelines. This document outlines the steps to configure pipeline in Sparkflows.

Follow the steps below:

Step 1 : Login to Sparkflows
-------------------------------

* Login to Sparkflows using your **credentials**.

Step 2 : Enable Pipeline Tabs
---------------------------------

* From the Dashboard page, navigate to **Administrations -> Configurations**, as shown below.

  .. figure:: ../../../_assets/aws/livy/fire_administration.png
      :alt: livy
      :width: 60%

* From the Configurations page, search the below configuration in the **Module** and enable it by setting its value to **true**. Then click on **Save Configurations** button to save the configuration.
  ::

      module.enablePipeline = true

   

  .. figure:: ../../../_assets/user-guide/pipeline/enable-pipeline.png
      :alt: Pipeline List
      :width: 60%
   
   
* Once the above configuration is enabled, you will see the three sub-tabs in project : **Pipelines, Executions & Schedules**, as shown below.

  .. figure:: ../../../_assets/user-guide/pipeline/pipeline-tabs.png
      :alt: Pipeline List
      :width: 60% 
