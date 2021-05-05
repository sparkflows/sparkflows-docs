Maintenance Tasks
==============

Cleaning H2 DB
--------------

Fire Insights by default uses the H2 embedded database.

It is important to keep the size of the database in control. All the Fire Insights tables are relatively small except those which store the result of workflow execution.

Cleaning Old Workflow Executions
+++++++++++++++++

It is important to regularly delete the old workflow executions in order to keep the size of the H2 DB in control.

- Go to the Administration/Cleanup Data
- Click on Delete old Workflow Executions in order to delete the old workflow executions.


Compact H2 DB File
++++++++++++++++++

If the H2 DB file size grows too large (> 3GB), then follow the steps below for compacting it.

By default H2 DB file is in the home folder of the user running Fire Insights. It is named as firedb.mv.db

* Store Fire Insights
* Make a copy of firedb.mv.db file to be safe
* Use the commands below for compacting it

java -cp ~/fire-3.1.0/db/h2/h2-1.4.199.jar  org.h2.tools.Shell
URL: jdbc:h2:./firedb
Driver : org.h2.Driver
User : fire
Password : fire

SHUTDOWN COMPACT

Deleting old files
----------------

Regularly delete the following folders:

* /tmp/fire/workflowlogs
* /tmp/fire/workflows

