New Login
+++++++++

This document describes using the token based authentication in Fire Insights.

Right Now we are supporting Two method Of getting Token to access Fire:
-----------------------------------------------------------------------

- By using Grant Types – Password
- By using Grant Types – Authorization code

By using Grant Type – Password
------------------------------

Post Request:
==============
 
- http://localhost:8080/oauth/token?grant_type=password&username=<username>&password=<password> 

Set client Id and Secret key in request headers:
------------------------------------------------
 
- Client Id = sparkflows
- Secret – (****)  

Updated As below:
-------------------
    
.. figure:: ../_assets/tutorials/token/token1.PNG
   :alt: Token
   :align: center   

Now We can use this access_token to access rest api like below:
---------------------------------------------------------------

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

- Fill up the username and password and click on signIn

.. figure:: ../_assets/tutorials/token/token5.PNG
   :alt: Token
   :align: center 

- Click on Use token

.. figure:: ../_assets/tutorials/token/token6.PNG
   :alt: Token
   :align: center

We have token now. Use it for requesting rest apis
---------------------------------------------------

.. figure:: ../_assets/tutorials/token/token7.PNG
   :alt: Token
   :align: center
