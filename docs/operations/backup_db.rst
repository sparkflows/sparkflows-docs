Backup and Recovery
------

Fire Insights stores the metadata into a Relational Database.

It comes with an embedded H2 database. It scales well for pretty heavy loads and upto 50 users. Sparkflows can be easily configured to run with a MySQL database.

When running with the H2 database, Sparkflows, by default, stores the database files in the user home directory which is running Sparkflows. There are 2 files :

- firedb.mv.db	
- firedb.trace.db

For backup, just copying these files to a backup location is enough. There is no need to stop Sparkflows. It is a good idea to copy it to another machine.


When configured with MySQL, the MySQL database named ``Fire`` needs to be backed up manually or by enabling RDS Auto Backup feature.

Automate Backup of H2 DB
================

Fire Insights enable Administrator to avail options for Automate Backup of H2 DB from UI and can be stored on same vm or in s3 bucket if its accessible from Fire Inisghts Machine.

Below are steps ::

