Scheduler
=======

Update on Scheduler:
--------------------
The latest upgrade of the Sparflows scheduler requires updating the following property in the quartz.properties file for proper functionality:
::
   org.quartz.jobStore.class=org.quartz.impl.jdbcjobstore.JobStoreTX 
**To** 
::
   org.quartz.jobStore.class=org.springframework.scheduling.quartz.LocalDataSourceJobStore
