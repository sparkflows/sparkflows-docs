Database Cleanup
================

Sparkflows provides methods to clean up database tables storing metadata related to workflow executions, pipeline executions, and their results. This can be done **manually** or **automated** as per configuration settings.

Manual Cleanup
++++++++++++++++++

You can manually clean up past workflow and pipeline executions on demand by following these steps:

**Step 1 : Accessing the Database Cleanup Page**
-------------------------------------------------

* Login to **Fire Insights**. 
* From the Dashboard, navigate to **Administration -> Cleanup Data**, as shown below.

  .. figure:: ../_assets/DB_cleanup/data-cleanup/administration-cleanup.PNG
     :alt: workflow execution cleanup
     :width: 60%

**Step 2 : Cleaning up Workflow Executions**
------------------------------------------------

* Click on **Delete Workflow Executions** button located in the right corner. A dropdown will open up, as shown below.

  .. figure:: ../_assets/DB_cleanup/data-cleanup/delete-workflow-executions-dropdown.png
     :alt: workflow execution cleanup
     :width: 60%

* Now, select the **Older than 90 days** option from the dropdown, to delete workflow executions from the database that are older than the specified number of days.

  .. figure:: ../_assets/DB_cleanup/data-cleanup/workflows-executions-90daysbeyond.png
     :alt: workflow execution cleanup
     :width: 60%

**Step 3 : Cleaning Up Pipeline Executions**
------------------------------------------------
* Click on **Pipeline Executions** tab from the Cleanup Data page. 
* Click on **Delete Pipeline Executions** button located in the right corner. A dropdown will open up, as shown below.

  .. figure:: ../_assets/DB_cleanup/data-cleanup/delete-pipeline-executions-dropdown.png
       :alt: workflow execution cleanup
       :width: 60%

* Now, select the **Older than 90 days** option from the dropdown, to delete pipeline executions from the database that are older than the specified number of days.

  .. figure:: ../_assets/DB_cleanup/data-cleanup/pipeline-executions-90daysbeyond.png
       :alt: workflow execution cleanup
       :width: 60%

**Step 4 : Cleaning Up Audit Logs**
-----------------------------
* Click on **Audit Logs** tab from the Cleanup Data page.
* Click on **Delete Audit Logs** button located in the right corner. A dropdown will open up, as shown below.
  
  .. figure:: ../_assets/DB_cleanup/data-cleanup/delete-auditlogs-dropdown.png
       :alt: workflow execution cleanup
       :width: 60%

* Now, select the **Older than 90 days** option from the dropdown, to delete audit logs from the database that are older than the specified number of days.

  .. figure:: ../_assets/DB_cleanup/data-cleanup/auditlogs-90daysbeyond.png
       :alt: workflow execution cleanup
       :width: 60%

Automated Cleanup
++++++++++++++++++
You can enable automated database cleanup by configuring specific settings. Follow the steps below:

**Step 1 : Enabling Automation of Database Cleanup**
--------------------------------------------------------

* Login to **Fire Insights**.
* From the Dashboard, navigate to **Administration -> Configurations**.
* Set the following property and click on **Save Configurations** button, as shown below. 
  :: 
    app.db.cleanup.enabled=true

  .. figure:: ../_assets/DB_cleanup/data-cleanup/db-cleanup-enabled-true.png
       :alt: workflow execution cleanup
       :width: 60%


**Step 2 : Configuring Cleanup Properties**
---------------------------------------------------
* The following properties are used to configure the database cleanup automation job:

  ::
   
      app.max.execution.storeInDb = 15000  => workflow executions to be stored in database
      app.max.pipeline.execution.storeInDb = 15000 => pipeline executions to be stored in databse
      app.db.cleanup.data.older.than.days = 1000 => All executions will be deleted if the data is older than the specified number of days

**Step 3 : Scheduling Cleanup Execution**
-------------------------------------------------

* By default, the database cleanup job runs once a day using the following **cron expression**:

  ::
   
     0 1 1 * * ?

  This schedule triggers the job at **01:01 AM everyday**. The admin can configure this in the **application.properties** file.


**Step 4 : Viewing Cleanup Job Logs**
-----------------------------------------
* After configuring the database cleanup job, users can monitor the process using the following logs:
 
  * **Job Scheduling Logs**

  ::

     scheduleDeleteWorkflowExecutionJob: Db cleanup job : Workflow execution threshold 340 : Pipeline execution threshold : 240 
     scheduleDeleteWorkflowExecutionJob : schedule job : scheduleDeleteWorkflowExecutionJob


  * **Execution Logs During Cleanup**
  ::

    fireui.schedulerquartz.DbCleanUpJob SCHEDULER : DbCleanUpJob::execute() fired
    fireui.services.OperationsServiceImpl Max Execution Flow ID: 18812
    fireui.services.OperationsServiceImpl deleteOldWorkflowExecution called.
    fireui.services.OperationsServiceImpl Total deleted execution records: 300
    fireui.schedulerquartz.DbCleanUpJob DbCleanup: Workflow executions and results deletion : Successfully deleted 300 executions and execution results.
    fireui.services.PipelineExecutorServiceImpl Total pipeline executions deleted: 627
    fireui.schedulerquartz.DbCleanUpJob DbCleanup: Pipeline executions and results deletion : Total 627 Pipeline Executions deleted successfully
    fireui.schedulerquartz.JobListenerService Job was executed deleteWorkflowExecutionJob

By following the above steps, you can efficiently manage database cleanup in Sparkflows and ensure optimal performance.

