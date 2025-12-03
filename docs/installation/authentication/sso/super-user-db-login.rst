Super User login using database
==============

Sparkflows allows to enable super user login by changing in ``sso.saml.properties`` file.

::

    sparkflows.sp.db.login.enable=true

After enabling super user DB login, one more button appears on login page, after starting Sparkflows server.

.. figure:: ../../../_assets/authentication/login_page.png
   :alt: sso super user login using database
   :width: 60%
	
	
Click on ``Sign in as Super user`` button.

::

   It will redirect you to "super user login form page".

.. figure:: ../../../_assets/authentication/login_form.png
   :alt: sso super user login using database
   :width: 60%


On updating the username and password, click on ``Sign In`` button. ::


    On successful authentication, it will redirect user to home page of the Sparkflows application.
