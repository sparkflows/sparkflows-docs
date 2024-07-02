OAuth Authentication
====================

Fire Insights supports OAuth Authentication.

Create Users in Fire
--------------------

First create the user in Fire under ``Administration/Users``.

Log into Fire with the ``admin`` user in order to be able to create the New Users.


Configuring OAuth
-----------------

In order to configure OAuth in Fire Insights, add the OAuth configuration parameters to ``conf/application.properties``.

Below is an example of configuring OAuth in Fire with Okta:

::


  # Okta settings
  oauth.client.clientId: 0oadvfdsfsdA7Y68356
  oauth.client.clientSecret: YSWFdZf9kfdsfsdfsdfsdnI0SVrswOJpHl
  oauth.client.accessTokenUri: https://xyz.okta.com/oauth2/default/v1/token
  oauth.client.userAuthorizationUri: https://xyz.okta.com/oauth2/default/v1/authorize
  oauth.client.clientAuthenticationScheme: form
  oauth.client.scope: openid profile offline_access
  oauth.resource.userInfoUri: https://xyz.okta.com/oauth2/default/v1/userinfo


Fire OAuth URL
--------------

In order to log in to the user into Fire using OAuth, use the following URL:

* http://machine_name:port/login/oauth

This URL will take the user to the OAuth login page. After the user logs in there, the user is redirected back to Fire and is logged in.

If the user is already logged in, going to the above URL, automatically brings up the Fire page for the user.
