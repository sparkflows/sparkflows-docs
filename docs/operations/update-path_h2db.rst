Update H2 DB Path
========

Sparkflows comes up with embedded H2 DB by default its getting created in user home directory.

You can Update database path using below :

Open ''db.properties'' file available inside ''fire-x-y.z/conf'' directory and update ''spring.datasource.url'' path you want to.

::

    spring.datasource.url = jdbc:h2:file:/path/firedb
    
    
.. note:: Make sure to update actual path and have write access to the directory.   
