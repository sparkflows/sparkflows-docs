Configuring Pipelines
========================

This document describes in detail the steps required to configure pipelines in Sparkflows.

  
To configure a pipeline in Sparkflows, follow these steps:

#. Login to Sparkflows:
     
   **Login** to the Sparkflows Web Server URL using your credentials, navigate to **Administrations -> Configurations**, and enable the following property:

   ::

      module.enablePipeline	true

   .. figure:: ../_assets/user-guide/pipeline/pipeline_administration.PNG
      :alt: Pipeline List
      :width: 60%

   .. figure:: ../_assets/user-guide/pipeline/pipeline_configurations.PNG
      :alt: Pipeline List
      :width: 60%
   
#. Enable Pipeline Tabs:

   After enabling the configuration, you will see three new tabs in your project: **Pipelines, Executions, and Schedules**.

   .. figure:: ../_assets/user-guide/pipeline/pipeline-list-new.png
      :alt: Pipeline List
      :width: 60% 

#. Airflow Configuration:

   If you are running Airflow on a remote server, set the following configurations in the **Airflow tab**: 
  

   .. list-table:: 
      :widths: 10 20 30
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Airflow Home
        - Airflow Home
        - Airflow Home Directory, if running on same machine.
      * - Airflow Endpoint URL
        - Airflow Endpoint URL
        - Airflow Endpoint URL where its running.
      * - Enable/Disable Airflow
        - Enable/Disable Airflow
        - Enable Airflow
      * - Airflow Dag
        - Airflow Dag
        - Airflow Dag location if you configured S3 Bucket.
      * - Airflow IAM Role
        - Airflow IAM Role
        - Airflow IAM Role used for accessing S3 Bucket for dags.
      * - Airflow dag max check
        - Maximum retry scheduler will do for checking availability of dag file in airflow dag directory
        - Depending on your requirements.
      * - Airflow dag Sync delay
        - Airflow dag Sync delay(seconds)
        - Depending on your requirements.
     
   .. figure:: ../_assets/user-guide/pipeline/pipeline_airflow.PNG
      :alt: Pipeline List     
      :width: 60%

   After saving these configurations, pipelines will be automatically submitted to the Airflow server for scheduling and execution.
  
   .. note:: Ensure that the Airflow path and other parameters are updated with their absolute paths.

#. Accessing the **Pipeline List**:

   The **Pipeline tab** under a Project displays a list of all pipelines created within that project. Pipelines can be grouped under various categories for better organization.

   .. figure:: ../_assets/user-guide/pipeline/pipeline-list-new.png
      :alt: Pipeline List
      :width: 60%
