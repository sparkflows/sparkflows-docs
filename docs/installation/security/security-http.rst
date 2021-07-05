Securing Port
=================

Fire Insights enable you to secure the http port, As by Default its running on both ie HTTP & HTTPS.

Below are steps to disbale Http port if Fire Insights already running on HTTPS
-------------------

Go to ``fire-x.y.z/conf/application.properties`` and make this two parameter value to true

::

    fire.cors.enable=true
    server.cookie.secure=true
    

.. note:: Make sure to change the default value of above parameter, By default these two value is false
