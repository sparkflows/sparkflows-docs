Operational Guide
=================

This document serves as a detailed guide for operating Sparkflows when running on AWS.

Below is the list of ways through which you can operate Sparkflows using AWS:

1. Onboarding New Users
2. Health Check
3. Backup and Recovery
4. Routing Maintenance
5. Support

Onboarding New Users
--------

New users can be created in Sparklows by logging into it. Then go to Administration/Users.

Health Check
-----

The main server process which handles the web requests is fire-ui. This is a long-running process and very stable. This process can be checked for responsiveness for any health checks.

Backup and Recovery
------

Fire Insights stores the metadata into a Relational Database. It comes with an embedded H2 database. It scales well for pretty heavy loads and upto 50 users. Sparkflows can be easily configured to run with MySQL database.

When running with the H2 database, Sparkflows by default stores the database files in the user's home directory which is running Sparkflows. There are 2 files:

- firedb.mv.db	
- firedb.trace.db

For keeping backup, one only needs to copy these files to a backup location. There is no need to stop Sparkflows while backing up. It is suggested to copy the above files to another machine.

When running Sparkflows with MySQL running on the same or different machine, the MySQL database named ``fire`` needs to be backed up.

Routing Maintenance
--------------------

Apart from backups of the database, Fire does not need much routine maintenance.

Fire stores the details of the job executions in the relational database. Over time, you may have too many jobs executed. Although it has the capacity to handle millions of jobs simultaneously and ofcourse, you need not to worry much about it yet it is suggested to delete older jobs from the Workflow Executions page so that the database is not cluttered excessively.

Support
-------

For support, you can contact Sparkflows at support@sparkflows.io. We will guide you through the process.

Sparkflows can also support you through Zendesk tickets. Get in touch with us for guidance and setup.
