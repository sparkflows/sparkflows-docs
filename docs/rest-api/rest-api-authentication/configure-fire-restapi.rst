Configuration REST API's
===========

Once the Access Token acquired from Fire Insights Application, you can update below Configuration in Fire Insights Application to access REST API's.


Below are steps :

1. Update below parameters inside ``application.properties``

Do this by adding the line below to application.properties
::

    fire.cors.enable=true
    fire.security.csrf.enable=false

2. Restart the Fire Server

Once the above parameter is being updated in ``application.properties``, Restart the Fire Server.

Now you will be able to access Fire Insights REST API's.


