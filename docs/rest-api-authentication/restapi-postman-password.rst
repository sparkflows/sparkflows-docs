Acquire Token using Postman and Grant Type - Password
++++++++++++++++++++++++++++++++++++++

This document describes the steps to obtain and use OAuth 2.0 access tokens using Postman.

Grants are at the heart of OAuth 2.0. Each grant defines one way for a client to retrieve an authorization.

Fire supports two grant types for retrieving the access token:

- Grant Types – Password
- Grant Types – Authorization code

Overview of Grant Type – Password
=====================

The Password grant is used when the application presents a traditional username and password login form to collect the user’s credentials and makes a POST request to the server to exchange the password for an access token. The POST request that the application makes looks like the example below.

Form the Post Request
=====================

The POST Request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it


- URL: http://hostname:port/oauth/token?grant_type=password&username=<username>&password=<password> 
  
  Update the username and password in URL and use as request header.

Click on Authorization tab and select Type - Basic Auth
==================================================

Basic Auth is an authorization type that requires a verified username and password to access a data resource.

Use default Username ``sparkflows`` and Password ``secret`` for client authentication. Click on ``Send`` to authorize the user and get the access token.

Example
===========
    
.. figure:: ../_assets/tutorials/token/token1.PNG
   :alt: Token
   :align: center 
   :width: 60%

Now use access_token from previous step to access the REST API
===========================================

An Access Token is a credential that can be used by an application to access an API, Below is an example to invoke the ``nodeList`` REST API of Fire Insights.

.. figure:: ../_assets/tutorials/token/token2.PNG
   :alt: Token
   :align: center 
   :width: 60%
   
   
