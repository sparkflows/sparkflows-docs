Database Clean up
================

Sparkflows offers methods to clean up database tables used for storing metadata related to workflow executions, pipeline executions, and their results.

Manual Cleanup
++++++++++++++++++

**To Access Database Cleanup Data**

Login to ``Sparkflows`` application -> ``Administration`` -> ``Cleanup Data``

Past workflow and pipeline executions can be cleaned up manually on demand.

Clean up workflow executions:
-----------------------------

By selecting the ``Older than 90 days`` button, the user can delete workflow executions from the database that are older than the specified number of days

  .. figure:: ../_assets/DB_cleanup/workflow_execution_cleanup.png
     :alt: workflow execution cleanup
     :width: 60%

Clean up pipeline executions:
-----------------------------

By selecting the ``Older than 90 days`` button, the user can delete pipeline executions from the database that are older than the specified number of days

  .. figure:: ../_assets/DB_cleanup/pipeline_execution_cleanup.png
     :alt: pipeline execution cleanup
     :width: 60%

Clean up audit logs:
-----------------------------
By selecting the ``Older than 90 days`` button, the user can delete audit logs from the database that are older than the specified number of days

  .. figure:: ../_assets/DB_cleanup/auditlog_cleanup.png
     :alt: audit log cleanup
     :width: 60%

Automated Cleanup
++++++++++++++++++

**To Enable Automation of Database Cleanup**

Login to ``Sparkflows`` application -> ``Administration`` -> ``Configuration`` -> ``app.db.cleanup.enabled=true``

Below properties are used to configure the database cleanup automation job

   ::
   
      app.max.execution.storeInDb = 15000  => workflow executions to be stored in database
      app.max.pipeline.execution.storeInDb = 15000 => pipeline executions to be stored in databse
      app.db.cleanup.data.older.than.days = 1000 => All executions will be deleted if the data is older than the specified number of days



By default, the database cleanup job runs once a day using the cron expression below. This can be configured by the admin in the ``application.properties`` file

``0 1 1 * * ?`` - > The cron expression which trigger At 01:01 AM of everyday.

After the database cleanup job is configured, users can view the following log for it

  ::

   scheduleDeleteWorkflowExecutionJob: Db cleanup job : Workflow execution threshold 340 : Pipeline execution threshold : 240 
   scheduleDeleteWorkflowExecutionJob : schedule job : scheduleDeleteWorkflowExecutionJob


While executing the database cleanup job, users can view the following logs for the database cleanup process

  ::

    fireui.schedulerquartz.DbCleanUpJob SCHEDULER : DbCleanUpJob::execute() fired
    fireui.services.OperationsServiceImpl Max Execution Flow ID: 18812
    fireui.services.OperationsServiceImpl deleteOldWorkflowExecution called.
    fireui.services.OperationsServiceImpl Total deleted execution records: 300
    fireui.schedulerquartz.DbCleanUpJob DbCleanup: Workflow executions and results deletion : Successfully deleted 300 executions and execution results.
    fireui.services.PipelineExecutorServiceImpl Total pipeline executions deleted: 627
    fireui.schedulerquartz.DbCleanUpJob DbCleanup: Pipeline executions and results deletion : Total 627 Pipeline Executions deleted successfully
    fireui.schedulerquartz.JobListenerService Job was executed deleteWorkflowExecutionJob



