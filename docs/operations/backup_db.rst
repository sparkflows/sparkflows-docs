Backup and Recovery
------

Fire Insights stores the metadata into a Relational Database.

It comes with an embedded H2 database. It scales well for pretty heavy loads and upto 50 users. Sparkflows can be easily configured to run with a MySQL database.

When running with the H2 database, Sparkflows by default stores the db files in the user home directory which is running Sparkflows. There are 2 files:

- firedb.mv.db	
- firedb.trace.db

For backup, just copying these files to a backup location is enough. There is no need to stop Sparkflows. It is a good idea to copy it to another machine.

When running with MySQL running on the same or different machine, the MySQL database named ``fire`` needs to be backed up or using RDS Auto Backup feature can be enabled.
