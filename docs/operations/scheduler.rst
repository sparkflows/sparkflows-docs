Scheduler
=======

Update on Scheduler:
--------------------
To ensure proper functionality with the **latest upgrade** of the Sparkflows scheduler, update the following property in the **quartz.properties** file:
::
   org.quartz.jobStore.class=org.quartz.impl.jdbcjobstore.JobStoreTX 
**To** 
::
   org.quartz.jobStore.class=org.springframework.scheduling.quartz.LocalDataSourceJobStore
