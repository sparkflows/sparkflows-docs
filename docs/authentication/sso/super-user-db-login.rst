Super User login using database
==============

Application allows to enable super user login by changing in sso.saml.properties file

sparkflows.sp.db.login.enable=true

After enabling super user db login, one more button appears on Login page.

.. figure:: ../../_assets/authentication/login_page.png
   :alt: sso super user login using database
   :width: 60%
	   
Click on Sign in as Super user button. It will redirect you to super user login page.

.. figure:: ../../_assets/authentication/login_form.png
   :alt: sso super user login using database
   :width: 60%

Fill the username and password. Click on SignIn. On successfully authentication, it will
redirect you to home page of the application.
