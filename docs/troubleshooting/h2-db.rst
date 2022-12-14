H2 Database
===========

Cheatsheet for H2 DB commands is at : https://docs.sparkflows.io/en/latest/commands/h2-db.html



Database is Read Only
---------------------

``fireserver.log`` is showing 'Database is Read Only`

H2 DB data is stored in the file firedb.mv.

Make sure that the user with which Fire Insights is running has write access to the file.

H2 Database looks corrupted
---------------------------

``fireserver.log`` is displaying error messages like 'could not read from position...`

Log into H2 DB and run ``SHUTDOWN COMPACT`` 

