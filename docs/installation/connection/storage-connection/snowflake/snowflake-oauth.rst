Snowflake Oauth Connection
=======

Sparkflows provides the capability to create "Snowflake Connection" and use the connection to access various resources, using Oauth.
Using Snowflake with OAuth, SSO with OAuth for user loggedIn must be enabled. Below are the steps user will have to follow:
1. SSO Authentication for User Login
    Users log in to the Sparkflow application through Single Sign-On (SSO), which can be implemented using protocol like OAuth. When users 
     authenticate via SSO, the application receives an access token, which will be used to identify the user in subsequent requests
 2. OAuth Connection for Snowflake Access:
    - Sparkflow allows users to create a connection to Snowflake, where the data storage and retrieval happen. This connection relies on OAuth for secure, delegated access to Snowflake resources. The OAuth setup with Snowflake includes configuring Sparkflow as an authorized OAuth client for Snowflake.
   - Once the connection is established, the user’s OAuth token (from SSO login) is passed through to Snowflake. This OAuth token grants the application access to specific Snowflake resources without requiring the user to re-authenticate.

Follow below steps to create a Snowflake connection using OAuth authentication: 

Snowflake Connection Configuration
----------

Use the below configurations for creating the connection to Snowflake.


   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1


      * - Title
        - Description
        - Value
      * - Credential Store  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Storage Connection
      * - Connection Type 
        - Select the Connection type from drop-down
        - Choose Snowflake as Connection Type
      * - Authentication Type 
        - Select the USER_CREDENTIAL or OAUTH
        - Choose OAUTH as Authentication Type
      * - Connection Name
        - Connection Name
        - Add an unique Connection Name
      * - Url
        - Url for Snowflake
        - Url for Snowflake

   .. figure:: ../../../../_assets/installation/connection/snowflake_storage.PNG

      :alt: connection
      :width: 60%    

   .. figure:: ../../../../_assets/installation/connection/snowflake_oauth.png
      :alt: connection
      :width: 60%
Test and save the connection
------

Once you save the connection, resouces can be used inside workflow editor etc. using the above connection.

.. Note:: Make Sure Sparkflows User Login(Using OAuth) should have sufficient Privilege of Snowflake resources.


Documentation
-----

Reference guide : https://docs.sparkflows.io/en/latest/snowflake/index.html
