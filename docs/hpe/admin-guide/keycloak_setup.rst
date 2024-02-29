Keycloak setup
=====

This document explains in detail the steps involved in setting up Keycloak on HPE UA.

Pre-requisites
------

#. you need to have **Sparkflows Domain** available.
#. Keycloak Login access with admin privilege.

Keycloak setup
-------

Below are steps for setting up Keycloak in UA.

#. Once you've decided on the Sparkflows' url to be used, navigate to the keycloak web ui, and login to the server with admin credentials. For the keycloak server details, connect with the HPE team :
   ::
     
     Server: https://keycloak.dev.hpeua.com/
     Username: admin
     Password: ******************

#. Select the UA realm from the left drop down menu and click on clients to view the list of clients currently registered.

   .. figure:: ../../_assets/hpe/hpe-keycloak-clients.png
      :width: 60%
      :alt: HPE UA Keycloak clients

#. Click on the ua client and then navigate to the settings section. Scroll down and add the sparkflows oidc callback url

   .. figure:: ../../_assets/hpe/keycloak-redirect-uris.png
      :width: 60%
      :alt: HPE UA Keycloak callback urls

#. Navigate to the Credentials section to copy the client secret, which will be used in sparkflows application properties.

   .. figure:: ../../_assets/hpe/client-details.png
      :width: 60%
      :alt: HPE UA Keycloak Client secrets

#. Copy the **Client Id, clientSecret, accessTokenUri, userAuthorizationUri, userInfoUri** which will be used in configuring Sparkflows.
