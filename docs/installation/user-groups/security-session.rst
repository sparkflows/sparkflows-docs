Securing Session
=================

Fire Insights enables you to secure the HTTP session. By default, it runs on both HTTP and HTTPS.

Disable HTTP Session
-------------------
Below are the steps to disable the HTTP session:

Go to **fire-x.y.z/conf/application.properties** and set the below configurations:

::

    fire.cors.enable=false
    fire.security.csrf.enable=true
    server.cookie.secure=true
    server.cookie.secure.httpOnly=true
    

.. note:: Make sure to change the default values of the above parameters to true.
