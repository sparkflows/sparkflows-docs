Securing Session
=================

Fire Insights enables you to secure the http session. By Default it runs on both HTTP & HTTPS.

Disable HTTP Session
-------------------
Below are the steps to disable HTTP session:

Go to ``fire-x.y.z/conf/application.properties`` and set the below configurations:

::

    fire.cors.enable=false
    fire.security.csrf.enable=true
    server.cookie.secure=true
    server.cookie.secure.httpOnly=true
    

.. note:: Make sure to change the default value of above parameters to true.
