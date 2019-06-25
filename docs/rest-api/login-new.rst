OAuth 2.0 - Obtaining an Access Token
++++++++++++++++++++++++++++++++++++++

This documents illustrate the interaction necessary to obtain and use OAuth 2.0 access tokens using Postman.

Grants are the heart of OAuth 2.0. Each Grant defines one way for a client to retrieve an authorization.

Fire supports two grant types for retrieving the access token:
---------------------------------------------------------------

- By using Grant Types – Password
- By using Grant Types – Authorization code

By using Grant Type – Password
------------------------------

Post Request:
==============
 
- http://localhost:8080/oauth/token?grant_type=password&username=<username>&password=<password> 

Click on Authorization tab and select type - Basic and fill username (clientId) and password (secret key) in request headers:
-----------------------------------------------------------------------------------------------------------------------------
 
- Client Id = sparkflows
- Secret – (****)  

Example below:
--------------
    
.. figure:: ../_assets/tutorials/token/token1.PNG
   :alt: Token
   :align: center   

Now use access_token to access rest api:
----------------------------------------

.. figure:: ../_assets/tutorials/token/token2.PNG
   :alt: Token
   :align: center 
   
Get the access token using grant type - authorization code
==========================================================

Get the access token
---------------------

- Click on Authorization tab
- Select Type OAuth 2.0

.. figure:: ../_assets/tutorials/token/token3.PNG
   :alt: Token
   :align: center 

- Click on Request Token

.. figure:: ../_assets/tutorials/token/token4.PNG
   :alt: Token
   :align: center 

- Fill the username and password and click on signIn

.. figure:: ../_assets/tutorials/token/token5.PNG
   :alt: Token
   :align: center 

Click on Use token
--------------------
.. figure:: ../_assets/tutorials/token/token6.PNG
   :alt: Token
   :align: center

Using tokens for accessing REST API
-----------------------------------

.. figure:: ../_assets/tutorials/token/token7.PNG
   :alt: Token
   :align: center
