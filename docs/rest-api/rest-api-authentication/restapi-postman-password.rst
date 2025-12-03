Acquire Token using Postman and Grant Type - Password
++++++++++++++++++++++++++++++++++++++++++++++++++++++

This document describes the steps to obtain and use OAuth 2.0 access tokens using the Postman.


Overview of Grant Type – Password
=================================

The Password grant is used when the application presents a traditional username and password login form to collect the user’s credentials and makes a POST request to the server to exchange the password for an access token. The POST requests that the application made looks like the example below.

Form the Post Request
=====================

The POST Request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it.

.. list-table:: Below are the Relevant Request
   :widths: 10 40
   :header-rows: 1

   * - Title
     - URL
     
   * - POST
     - http://hostname:port/oauth/token?grant_type=password&username=<username>&password=<password>
  
Update the username and password in URL, and use it as a request header.

Click on Authorization Tab and Select Type - Basic Auth
==================================================

Basic Auth is an authorization type that requires a verified username and password to access a data resource.

Use default Username ``sparkflows`` and Password ``secret`` for client authentication. Click on ``Send`` to authorize the user and get the access token.

Example
===========
    
.. figure:: ../../_assets/tutorials/token/token1.PNG
   :alt: Token
   :width: 60%

Now Use Access Token from Previous Step to Access the REST API
===========================================

An Access Token is a credential that can be used by an application to access an API. Below is an example to invoke the ``nodeList`` REST API of the Sparkflows.

.. figure:: ../../_assets/tutorials/token/token2.PNG
   :alt: Token
   :width: 60%
   
   
