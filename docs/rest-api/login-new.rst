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
    
    
 .. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/tutorials/token/token1.PNG
   :alt: Token
   :align: center   

Now WE can use this access_token to access rest api like below:
---------------------------------------------------------------

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/tutorials/token/token2.PNG
   :alt: Token
   :align: center 
               

