Keycloak Setup
=====

This document explains in detail the steps involved in setting up Keycloak on HPE UA.

Pre-requisites
------

#. You would need to have **Sparkflows Domain** available.
#. Keycloak login access with admin privilege.


Below are steps for setting up Keycloak in UA.

Step 1 : Log in to Keycloak
---------------------------------
#. Determine the **Sparkflows URL** you will use.
#. Navigate to the **Keycloak web UI** and log in with your admin credentials.

   Server Details:

   ::
     
     Server: https://keycloak.dev.hpeua.com/
     Username: admin
     Password: ******************

   .. Note:: For the Keycloak server details, connect with the HPE team.

Step 2 : Select UA Realm and View Clients
--------------------------------------------
#. From the left drop-down menu, select the **UA Realm**.

#. Click on **Clients** to view the list of currently registered clients.

   .. figure:: ../../_assets/hpe/hpe-keycloak-clients.png
      :width: 60%
      :alt: HPE UA Keycloak clients

Step 3 : Configure the UA Client
---------------------------------

#. Click on the **UA client**.

#. Navigate to the **Settings** section.

#. Scroll down and add the **Sparkflows OIDC callback URL**.

   The format of the url is as follows:

   ::

      https://<sparkflows-host>/login/oauth

   .. figure:: ../../_assets/hpe/keycloak-redirect-uris.png
      :width: 60%
      :alt: HPE UA Keycloak callback urls


Step 4 : Retrieve Client Credentials
---------------------------------------

#. Go to the **Credentials** section to copy the **Client Secret**.

#. Copy the **Client ID, Client Secret, accessTokenUri, userAuthorizationUri, and userInfoUri**.

   These details will be used in the Sparkflows application properties.

   .. figure:: ../../_assets/hpe/client-details.png
      :width: 60%
      :alt: HPE UA Keycloak Client secrets


Step 5 : Obtain OpenID Connect Information
--------------------------------------------

#. Visit the **Keycloak client’s OpenID Connect endpoint** to retrieve the following:

   * **accessTokenUri**
   * **userAuthorizationUri**
   * **userInfoUri**

   Open ID Connect URI is as follows:
   ::
      https://<keycloakhost:port>/realms/{realm}/.well-known/openid-configuration

Step 6 : Create a Secret Resource for Sparkflows in Kubernetes
------------------------------------------------------------

#. Create a secret resource in EzUA Kubernetes to store the Sparkflows service configuration.

   Name the secret as **sparkflows-app-secret**.
   
   The above urls and the client credentials(Client ID & Secret) will be used to update in this secret file, as shown below.

   ::

      oauth.client.clientId: ua
      oauth.client.clientSecret: ********************
      oauth.client.accessTokenUri: https://keycloak.abc.com/realms/UA/protocol/openid-connect/token
      oauth.client.userAuthorizationUri: https://keycloak.abc.com/realms/UA/protocol/openid-connect/auth
      oauth.resource.userInfoUri: https://keycloak.abc.com/realms/UA/protocol/openid-connect/userinfo
      oauth.client.ssl.disable:false

   .. Note:: Connect with the Sparkflows team to create this secret resource in Ezmeral Kubernetes.

Step 7 : Create a Secret for the Keycloak SSL Certificate
-------------------------------------------------------------

#. Create a secret in Kubernetes to store the Keycloak SSL Certificate.

   * Name the secret as **keycloak-sslcert**. This secret is required for connecting to Keycloak for authentication.

   .. Note:: Contact the HPE Ezmeral team to create this secret resource in Ezmeral Kubernetes.

Step 8 : Create a Secret for Hive Connection
-------------------------------------------

#. Create a secret for storing the **hive-site.xml file**, required for connecting to the Hive thrift server from Sparkflows.

   * Name the secret as **hive-site-secret**.

   .. Note:: Contact the HPE Ezmeral team to create this secret resource in Ezmeral Kubernetes.


Step 9 : Create a Volume for Hive SSL Truststore
--------------------------------------------------

#. Create a persistent volume for storing the Hive SSL truststore file.

   * Name the volume as **hive-ssltrust-store-vol**.

   .. Note:: Contact the HPE Ezmeral team to create this persistent volume in Ezmeral Kubernetes.


