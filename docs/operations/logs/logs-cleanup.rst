Logs and Temp files Clean up
======
Configuration
++++++++++++

- Sparkflows offers automated log and temp directory cleanup for better disk space management
- This job ensures efficient space management by deleting aged temporary data, improving overall system performance and disk utilization
- The cleanup job can be configured by the admin in the ``application.properties`` file.

  ``0 0 12 * * ?``  -> default cron expression to trigger clean up job
- Once the above configuration is configured the clean up job will execute based on the cron expression.
- The configuration used to delete log files based on a specified number of days is as follows: ``app.log.file.age.threshold``
- The configuration used to delete temp files based on a specified number of days is as follow: ``app.temp.file.age.threshold`` default value is 5 days
- Users can configure the ``app.disk.threshold`` property to delete job logs based on disk size.
  By default, this value is set to 2 GB. If the size of the log files exceeds the configured threshold, older log files will be deleted.


Logs clean up execution
+++++++++++++++++++++++
- Once logs clean up is configured user can see the below log while restarting the application 

::

  2024-10-14 12:52:51 [restartedMain] "fire-1" INFO  fireui.schedulerquartz.SchedulerQuartzSingleton - Scheduling Logs cleanup Job : cron pattern 0 0 12 * * ?

- The default cron expression of the clean up job will be execute  At 12:00 PM everyday.
- While trigger time of the clean up jobs user can see the below logs for it

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

Disk clean up
+++++++++++++++++++++++

- Files within temporary folders will be automatically deleted based on the specified retention period defined in the ``app.temp.file.age.threshold`` configuration if the disk space is low.
- This setting manages the deletion of files in the /tmp directories according to the configured retention period in days.
- If disk space is less than configured threshold value, it will delete all the temp files older than configured temp file age threshold value.

Temp directory clean up
++++++++++++++++++++++++++
Clean up job also automatically clean up temporary files and folders in the /tmp directory. This job ensures efficient space management by deleting aged temporary data, improving overall system performance and disk utilization.

- Configurable File Age Threshold: Application allows users to configure the file age threshold through the UI. Users can set the age (in days) for files and directories, determining which temporary data should be deleted. For example, setting the threshold to 5 days will delete all files and folders older than 5 days.

-Improved Resource Management: By automatically cleaning up temporary files, the system prevents unnecessary disk space consumption, contributing to optimized resource usage.

- Note: Ensure the file age threshold is set according to your system’s temporary file usage pattern to prevent unintended deletions of files needed for ongoing processes.











