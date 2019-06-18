Operational Guidance
=================

This document describes details for operating Sparkflows when running on AWS.

Onboarding New Users
--------

New users can be created in Sparklows by logging into it. Then go to Administration/Users.

Health Check
-----

The main server process which handles the web requests is fire-ui. This is a long running process and very stable. This process can be checked for responsiveness for any health checks.

Backup and Recovery
------

Fire Insights stores the metadata into a Relational Database.

It comes with an embedded H2 database. It scales well for pretty heavy loads and upto 50 users. Sparkflows can be easily configured to run with an MySQL database.

When running with H2 database, Sparkflows by default stores the db files in the user home directory which is running Sparkflows. There are 2 files:

- firedb.mv.db	
- firedb.trace.db

For backup, just copying these files to a backup location is enough. There is no need to stop Sparkflows. It is a good idea to copy it to another maching.

When running with MySQL running on the same or different machine, the MySQL database named ``fire`` needs to be backed up.

Routing Maintenance
--------------------

Apart from backups of the database, Fire does not need much of routine maintenance.

Fire stores the details of the job executions in the relational database. Over time, you may have too many jobs executed. Deleting old jobs from the Workflow Executions page is a good idea so as not to fill up the database too much. But it has the ability to handle millions of jobs, so you do not have to worry too much about it.

Support
-------

For support, you can contact Sparkflows at support@sparkflows.io. We will guide you through the process.

Sparkflows can also support you though Zendesk tickets. Get in touch with us for guidance and setup.
