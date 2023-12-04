Enable the Access Token Authentication
====================================

Update below configuration to authenticate the access token.


Below are steps :

1. Update below parameters inside ``application.properties``

Do this by adding the line below to application.properties
::

    fire.cors.enable=true
    fire.security.csrf.enable=false

2. Restart the Fire Server

Once the above parameter is being updated in ``application.properties``, Restart the Fire Server.

Now you will be able to access Fire Insights REST API's.


.. note:: If above properties are not updated in application.properties, below error message will be recevied.

::

    {
    "error": "invalid_token",
    "error_description": "Invalid access token"
    }
