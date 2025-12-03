Update H2 Database Path
========

Sparkflows comes up with embedded H2 database. By default, the H2 database files are created in the users home directory.

The path of the H2 database files can be updated as follows:

#. Open **db.properties** file located inside **fire-x-y.z/conf** directory.
#. Update **spring.datasource.url** path to the desired location.

  ::

      spring.datasource.url = jdbc:h2:file:/path/firedb
    
    
.. note:: Make sure to update the actual path and ensure you have the write access to the directory.   
