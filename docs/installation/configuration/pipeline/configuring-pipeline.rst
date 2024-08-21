Configuring Pipelines
======================

Sparkflows uses Apache Airflow for executing Pipelines.

Below are the steps involved in configuring pipeline in Sparkflows:

Step 1 : Login to Sparkflows
-------------------------------

#. **Login** to **Sparkflows Web Server URL** using your credentials.

Step 2 : Enable Pipline Tabs
---------------------------------
#. Navigate to **Administrations -> Configurations** to enable the below property:

   ::

        module.enablePipeline	true

   .. figure:: ../../../_assets/aws/livy/administration.png
      :alt: livy
      :width: 60%

   .. figure:: ../../../_assets/user-guide/pipeline/pipeline_configurations.PNG
      :alt: Pipeline List
      :width: 60%
   
   Once the above configuration is enabled, you will see three tabs in project namely **Pipelines, Executions & Schedules**.

   .. figure:: ../../../_assets/user-guide/pipeline/pipeline-list-new.png
      :alt: Pipeline List
      :width: 60% 
