Keycloak Setup
=====

This document explains in detail the steps involved in setting up Keycloak on HPE UA.

Pre-requisites
------

#. You would need to have **Sparkflows Domain** available.
#. Keycloak login access with admin privilege.

Setup Steps
-------

Below are steps for setting up Keycloak in UA.

#. Once you've decided on the Sparkflows' URL to be used, navigate to the Keycloak web UI, and login to the server with admin credentials. For the Keycloak server details, connect with the HPE team :
   ::
     
     Server: https://keycloak.dev.hpeua.com/
     Username: admin
     Password: ******************

#. Select the UA realm from the left drop down menu and click on clients to view the list of clients currently registered.

   .. figure:: ../../_assets/hpe/hpe-keycloak-clients.png
      :width: 60%
      :alt: HPE UA Keycloak clients

#. Click on the UA client and then navigate to the settings section. Scroll down and add the sparkflows OIDC callback URL

   The format of the url is as follows.

   ::

      https://<sparkflows-host>/login/oauth

   .. figure:: ../../_assets/hpe/keycloak-redirect-uris.png
      :width: 60%
      :alt: HPE UA Keycloak callback urls

#. Navigate to the Credentials section to copy the client secret, which will be used in Sparkflows application properties.

   .. figure:: ../../_assets/hpe/client-details.png
      :width: 60%
      :alt: HPE UA Keycloak Client secrets

#. Copy the **Client Id, clientSecret, accessTokenUri, userAuthorizationUri, userInfoUri** which will be used in configuring Sparkflows.

#. Visit the Keycloak client’s OpenID connect endpoint to get following information

   a) accessTokenUri
   b) userAuthorizationUri
   c) userInfoUri

   Open ID Connect URI 
   ::
      https://<keycloakhost:port>/realms/{realm}/.well-known/openid-configuration

#. Create a secret resource in EzUA kubernetes to store the Sparkflows service configuration with name of the secret as **sparkflows-app-secret**
	
   The above urls and the client credentials(Client ID & Secret) will be used to update in this secret file, as shown below.

   ::

      oauth.client.clientId: ua
      oauth.client.clientSecret: ********************
      oauth.client.accessTokenUri: https://keycloak.abc.com/realms/UA/protocol/openid-connect/token
      oauth.client.userAuthorizationUri: https://keycloak.abc.com/realms/UA/protocol/openid-connect/auth
      oauth.resource.userInfoUri: https://keycloak.abc.com/realms/UA/protocol/openid-connect/userinfo
      oauth.client.ssl.disable:false

   Connect with the Sparkflows team to create this secret resource in Ezmeral Kubernetes.

#. Create a secret for storing the SSL certificate of the Keycloak server, with name as **keycloak-sslcert**. This would be required while connecting to the             Keycloak   for authentication. 

   Connect with the HPE Ezmeral team to create this secret resource in Ezmeral Kubernetes.

#. Create a secret for storing the hive-site.xml that will be required for connecting to the Hive thrift server from Sparkflows, with name as **hive-site-secret**. 

   Connect with the HPE Ezmeral team to create this secret resource in Ezmeral Kubernetes.

#. Create a volume for storing the Hive SSL truststore file with name as **hive-ssltrust-store-vol**.

   Connect with the HPE Ezmeral team to create this persistent volume in Ezmeral Kubernetes.

