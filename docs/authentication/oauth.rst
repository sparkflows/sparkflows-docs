OAuth
=====

Fire Insights supports OAuth.

Configuring OAuth
-----------------

In order the configure OAuth in Fire Insights, add the OAuth configuration parameters to ``conf/application.properties``.

Below is an example of configuring OAuth with Okta.

::

  # external provider
  oauth.client.clientId: 0oadvfdsfsdA7Y68356
  oauth.client.clientSecret: YSWFdZf9kfdsfsdfsdfsdnI0SVrswOJpHl
  oauth.client.accessTokenUri: https://xyz.okta.com/oauth2/default/v1/token
  oauth.client.userAuthorizationUri: https://xyz.okta.com/oauth2/default/v1/authorize
  oauth.client.clientAuthenticationScheme: form
  oauth.client.scope: openid profile email
  oauth.resource.userInfoUri: https://xyz.okta.com/oauth2/default/v1/userinfo



