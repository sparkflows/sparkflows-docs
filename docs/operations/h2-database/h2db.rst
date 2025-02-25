Update H2 Database Path
========

Fire Insights comes up with embedded H2 database. By default, the H2 database files are created in the users home directory.

The path of the H2 database files can be updated as below :

Open ``db.properties`` file available inside ``fire-x-y.z/conf`` directory and update ``spring.datasource.url`` path you want to.

::

    spring.datasource.url = jdbc:h2:file:/path/firedb
    
    
.. note:: Make sure to update the actual path and have write access to the directory.   
