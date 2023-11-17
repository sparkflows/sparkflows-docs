H2 Database
===========

This document segment addresses common challenges encountered by our users in connection with H2 Database and provides effective resolutions for each the issues.



1. Database is Read Only
---------------------

**Problem**
+++++++

**fireserver.log** is displays the following error message: 

**Database is Read Only**

**Solution**
+++++++

H2 DB data is stored in the file **firedb.mv**.

Make sure that the user with which Fire Insights is running has write access to the file.

2. H2 Database Looks Corrupted
---------------------------

**Problem**
+++++++++
**fireserver.log** is displays the following error message: 

**Could not read from position...**

**Solution**
+++++++
Log into H2 DB and run the below:
::

 SHUTDOWN COMPACT 

.. Note:: H2 DB commands can be found at the below location:

 `H2DB Commands Cheatsheet <https://docs.sparkflows.io/en/latest/commands/h2-db.html>`_

