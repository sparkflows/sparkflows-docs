Configuration REST API
===========

Once the Access Token acquired from Fire Insights Application, you can update below Configuration in Fire Insights Application to access REST API.


Below are steps :

1. Update below parameters inside ``application.properties``

Do this by adding the line below to application.properties
::

    fire.cors.enable=true
    fire.security.csrf.enable=false
