Logs Clean up
======
Configuration
===============

- Sparkflows offers automated log directory cleanup for better disk space management
- The log cleanup job can be configured by the admin in the ``application.properties`` file.

  ``0 0 12 * * ?``  -> default cron expression to trigger logs clean up job
- Once the above configuration is configured the logs clean up job will execute based on the cron expression.
- The configuration used to delete log files based on a specified number of days is as follows: ``App.log.file.age.threshold``
- Users can configure the ``app.disk.threshold`` property to delete job logs based on disk size. 
  By default, this value is set to 2 GB. If the size of the log files exceeds the configured threshold, older log files will be deleted.


Logs clean up execution
=======================
- Once logs clean up is configured user can see the below log while restarting the application 

::

  2024-10-14 12:52:51 [restartedMain] "fire-1" INFO  fireui.schedulerquartz.SchedulerQuartzSingleton - Scheduling Logs cleanup Job : cron pattern 0 0 12 * * ?

- The default cron expression of the logs clean up job will be execute  At 12:00 PM everyday.
- While trigger time of the logs clean up jobs user can see the below logs for it

::

  2024-10-14 18:03:00 [fire-quartz-cluster_Worker-1] "fire-1" INFO  fireui.schedulerquartz.JobListenerService - Job execution vetoed logsCleanupJob
  2024-10-14 18:03:07 [fire-quartz-cluster_Worker-1] "fire-1" INFO  fireui.schedulerquartz.LogsCleanerJob - LogsCleanerJob started 14/10/24 6:03 PM 
  2024-10-14 18:03:16 [fire-quartz-cluster_Worker-1] "fire-1" INFO  fireui.schedulerquartz.LogsCleaner - Available disk space : 63873830912
  2024-10-14 18:03:59 [fire-quartz-cluster_Worker-1] "fire-1" INFO  fireui.schedulerquartz.LogsCleaner - Sufficient disk space available.

- If the log file is older than the days which user configured in ``App.log.file.age.threshold`` , it will be deleted, and users can view the following logs 
  related to this action.

::

  2024-10-14 18:33:00 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.JobListenerService - Job execution vetoed logsCleanupJob
  2024-10-14 18:33:00 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.LogsCleanerJob - LogsCleanerJob started 14/10/24 6:33 PM 
  2024-10-14 18:33:00 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.LogsCleaner - Available disk space : 63854682112
  2024-10-14 18:33:00 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.LogsCleaner - Sufficient disk space available.
  2024-10-14 18:33:00 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.LogsCleaner - Deleted log file from : log\fire-pyspark-49156.log
  2024-10-14 18:33:00 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.LogsCleaner - Deleted log file from : log\fire-pyspark-49157.log
  2024-10-14 18:33:01 [fire-quartz-cluster_Worker-6] "fire-1" INFO  fireui.schedulerquartz.JobListenerService - Job was executed logsCleanupJob

