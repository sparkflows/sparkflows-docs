Update H2 DB Path
========

Fire Insights comes up with embedded H2 DB. By default the H2 DB files are created in the users home directory.

The path of the H2 DB files can be updated as below :

Open ''db.properties'' file available inside ''fire-x-y.z/conf/db.properties'' directory and update ''spring.datasource.url'' path you want to.

::

    spring.datasource.url = jdbc:h2:file:/path/firedb
    
    
.. note:: Make sure to update actual path and have write access to the directory.   
