Securing Session
=================

Fire Insights enable you to secure the http session, As by Default its running on both ie http & https.

Below are steps to disbale http session if Fire Insights already running on https
-------------------

Go to ``fire-x.y.z/conf/application.properties`` and make this two below parameter value to ``true``

::

    fire.cors.enable=true
    server.cookie.secure=true
    

.. note:: Make sure to change the default value of above parameter to true, By default these two value is false
