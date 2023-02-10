Scheduler
=========

Scheduling pipelines refer to the process of automating the execution of tasks, such as data processing, building machine learning models, triggering airflow jobs at a specific time or interval. It's important to consider factors such as scalability, reliability, and cost when scheduling pipelines. This can be useful in a variety of situations, such as:

* Running every X minutes/hourly/daily/weekly/monthly data processing jobs.
* Automatically triggering the airflow pipelines.

In Sparkflows, there are two ways to schedule pipelines:

* Using Cron in the Scheduler 
* Using Scheduler with choosing options from the UI


Steps to Schedule and view the Scheduled jobs
---------------------------------------------

1. **Schedule Jobs**

      Sparkflows allows you to schedule Jobs. These jobs can be either comprise of running Workflows or Pipelines. The Scheduler takes in the below fields as input as seen in the images below. The first one corresponds to Scheduling pipeline and the next one is for Scheduling workflow:

      .. figure:: ../../_assets/user-guide/scheduler/SCHEDULE_PIPELINE.png
         :alt: Schedule Pipeline 
         :width: 75%
      
      
      .. figure:: ../../_assets/user-guide/scheduler/ SCHEDULE_WORKFLOW.png
         :alt: Schedule Pipeline 
         :width: 75%
       
       
      Each of the above fields is described below:
         1. ``Project``: From the dropdown, one has to choose the Project in which the workflow or pipeline which user wants to Schedule resided.
         2. ``Workflow``: One has to choose the workflow or the pipeline which user wants to Schedule.
         3. ``Spark submit options``: This field can be made use of to specify the runtime options while submitting Workflows which will be run as Apache Spark jobs. If not, it can be left empty.
         4. ``Program parameters``: If the Workflow taken in any parameters, it can be specified here. If not, it can be left empty.
         5. ``Email on Success``: Email address of people who should be notified on success of the scheduled job can be specified in this field.
         6. ``Email on Failure``: Email address of people who should be notified on failure of the scheduled job can be specified in this field.
         7. ``Start date``: This can be used to specify when should the scheduled job start. One can specify date and time and the scheduled job will start executing only after the start date has elapsed. Eg: One can schedule a job to run hourly starting three days later using this feature.
         8. ``End date``: This can be used to specify when should the job should stop getting scheduled. One can specify date and time and the scheduled job will stop getting scheduled after the stop date has elapsed. Eg: One can schedule a job to run hourly but stop getting scheduled three days later using this feature.
         9. ``Schedule frequency``: One can choose the frequency of the job by choosing from the options below along with the time zone:
               a. ``Minute`` : Will schedule the Job every X minutes.
               b. ``Hourly`` : Will schedule the Job every X hours.
               c. ``Daily`` : Will schedule the Job daily at X hour and Y minutes.
               d. ``Weekly``  : Will schedule the Job weekly on X day, Y hour and Z minutes.
               e. ``Monthly`` : Will schedule the Job monthly at X day, Y hour and Z minutes.
               f. ``Cron Expression``: Cron expression of the form can be used to schedule job in Sparkflows ``0 0/15 * * * ? *`` This Cron will schedule the job every 15 minutes.
   
2. **View Pipeline Schedules**

   Once the Pipeline is scheduled, you can view the list of scheduled jobs by clicking on the Schedules tab. One can also view other meta data of the scheduled jobs as seen in the image below.

      .. figure:: ../../_assets/user-guide/scheduler/VIEW_PIPELINE_SCHEDULES.png
         :alt: Pipeline Schedules
         :width: 75%
   

Notes  
========

* One can use the scheduler in Sparkflows to trigger Airflow pipelines.

* Redeployment of the Sparkflows application will not remove the already scheduled workflows and pipelines. The jobs will start to get scheduled once the application in restarted.

* The scheduler will continue to trigger the workflow even if the compute cluster is not reachable.

* The scheduler will continue to trigger the airlfow pipelines even if the airflow cluster is not reachable.

* The scheduler will continue to trigger the next executions regardless of the previous trigger status.

* If there are too many pipelines yet to be exeucted, they will get queued up and will execute once the previous pipelines have completed.


