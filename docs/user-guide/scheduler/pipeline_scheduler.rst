Overview
========

It's very important to schedule Pipelines and Workflows for smooth execution of long-running jobs in parallel and asynchronous manner.
Sparkflows scales out the Data Processing and Machine Learning Use cases by offering seamless scheduling capabilities.

Steps
========

1. **Schedule Pipeline**

Sparkflows allows you to schedule Pipeline. It stores the metadata of periodic jobs and uses a built-in scheduler to queue user requests.
If Airflow is configured then Sparkflows submits the Job requests to Airflow as per the scheduling 

.. figure:: ../../_assets/user-guide/scheduler/SCHEDULE_PIPELINE.png
   :alt: Schedule Pipeline 
   :width: 60%
   
2. **View Pipeline Schedules**

Once the Pipeline is scheduled, you can view the scheduling info.

.. figure:: ../../_assets/user-guide/scheduler/VIEW_PIPELINE_SCHEDULES.png
   :alt: Pipeline Schedules
   :width: 60%
   
3. **View the DAG Script generated from the Pipeline**

4. **Test - Trigger Pipeline Execution in Airflow**

.. figure:: ../../_assets/user-guide/scheduler/DIRECTLY_EXECUTE_PIPELINE_IN_AIRFLOW.png
   :alt: Schedule Pipeline 
   :width: 60%


5. **Check the logs for Pipeline and Airflow Interaction**

.. figure:: ../../_assets/user-guide/scheduler/VIEW_LOGS_OF_PIPELINE_AIRFLOW_INTERACTION.png
   :alt: View logs in Pipeline 
   :width: 60%

6. **View the DAGs in Pipeline**

7. **View the DAGs in Airflow**

.. figure:: ../../_assets/user-guide/scheduler/VIEW_JOBS_IN_AIRFLOW.png
   :alt: Airflow DAGs
   :width: 60%

   
8. **Check the status of Pipelines**

.. figure:: ../../_assets/user-guide/scheduler/VIEW_STATUS_OF_PIPELINE_EXECUTIONS.png
   :alt: Airflow DAGs
   :width: 60%

9. **Verify if DAGs are trigeered as per Schedules**

.. figure:: ../../_assets/user-guide/scheduler/TEST_SCHEDULED.png
   :alt: Airflow DAGs
   :width: 60%

Additional Notes
========

