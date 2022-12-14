H2 Database
===========

Database is Read Only
---------------------

``fireserver.log`` is showing 'Database is Read Only`

H2 DB data is stored in the file firedb.mv.

Make sure that the user with which Fire Insights is running has write access to the file.

H2 Database looks corrupted
---------------------------

``fireserver.log`` is displaying error messages like 'could not read from position...`

Try to run SHUTDOWN COMPACT 

