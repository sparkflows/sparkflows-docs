OAuth Authentication
====================

Fire Insights supports OAuth Authentication.

Below are Pre-Requisites to Configure OAuth in Fire Insights.

Pre-requisites
--------

#. Fire Insights host URL must be available for setting up OIDC callback URL in application setup in OAuth
#. oauth.client.clientId
#. oauth.client.clientSecret
#. oauth.client.accessTokenUri
#. oauth.client.userAuthorizationUri
#. oauth.resource.userInfoUri


.. note::  Make sure to update ``OIDC callback URL`` as ``https://<sparkflows-host>/login/oauth``.


Configuring OAuth in Fire Insights
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


Update sso.saml.properties 
-----------------

In order to configure OAuth in Fire Insights, update ``conf/sso.saml.properties`` with below parameter:

::


    #enable/disable sso by set the value true or false
    sparkflows.sp.sso.enable=true

    #authentication type - expected value (saml or oauth)
    sparkflows.authentication.type=oauth

    #Enable/disable user auto creation in local database. If user is not present in local database and auto creation is true
    sparkflows.sp.auto.user.create=true

    #disable the db login for admin also.
    sparkflows.sp.db.login.enable=true

Start Fire Insight 
--------------

Once the above Configuration are updated and saved, Start the Fire Insights application and Type Fire Insights host URL in web browser and try login using option ``Login with SSO``.

.. note::  Make sure that user trying to login should have access.

