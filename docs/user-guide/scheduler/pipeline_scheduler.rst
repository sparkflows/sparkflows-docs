Overview
========

It's very important to schedule Pipelines and Workflows for smooth execution of long-running jobs in parallel and asynchronous manner.
Sparkflows scales out the Data Processing and Machine Learning Use cases by offering seamless scheduling capabilities.

Steps
========

1. **Schedule Pipeline**

Sparkflows allows you to schedule Pipeline. It stores the metadata of periodic jobs and uses a built-in scheduler to queue user requests.
If Airflow is configured then Sparkflows submits the Job requests to Airflow as per the scheduling. 

.. figure:: ../../_assets/user-guide/scheduler/SCHEDULE_PIPELINE.png
   :alt: Schedule Pipeline 
   :width: 60%
   
2. **View Pipeline Schedules**

Once the Pipeline is scheduled, you can view the scheduling info.

.. figure:: ../../_assets/user-guide/scheduler/VIEW_PIPELINE_SCHEDULES.png
   :alt: Pipeline Schedules
   :width: 60%
   
3. **View the DAG Script generated from the Pipeline**

.. figure:: ../../_assets/user-guide/scheduler/VIEW_DAG_CODE.png
   :alt: View DAG Code 
   :width: 60%


4. **Test - Trigger Pipeline Execution in Airflow**

.. figure:: ../../_assets/user-guide/scheduler/DIRECTLY_EXECUTE_PIPELINE_IN_AIRFLOW.png
   :alt: Trigger Pipeline 
   :width: 60%


5. **Check the logs for Pipeline and Airflow Interaction**

.. figure:: ../../_assets/user-guide/scheduler/VIEW_LOGS_OF_PIPELINE_AIRFLOW_INTERACTION.png
   :alt: View logs in Pipeline 
   :width: 60%

6. **View the DAGs in Pipeline**

.. figure:: ../../_assets/user-guide/scheduler/VIEW_AIRFLOW_DAGS.png
   :alt: View DAGS in Pipeline Editor
   :width: 60%

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


Troubleshooting
========

1. **Pipeline is not running consistently in Airflow**

**Issue Description**

There could be different reasons for this issue.

* The Background Event Trigger Thread is stalled
* The Websocket doesn't receive events in timely manner
* Airflow DAG Execution requests are not trigerred in timely manner
  
**Resolution**

Check the Machine Configuration.

* Ensure minumum 8 cores and 16 GB RAM are used.
* Check if any additional processes (running in the same VM where Sparkflows is running) hogging the memory and processes.

  Examples of additional processes: 
    * Agent handling the traffic between Load Balancer and installed service, 
    * any Applications (e.g. Envoy) which scans the deployed App and logs (CPU, Mem)  

* Check DAGs in Airflow are not queued up
* Ensure Airflow Instance is configured with enough Memory and Processing Cores. 
