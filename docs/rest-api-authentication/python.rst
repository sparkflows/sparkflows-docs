Acquire Session Cookie in Python
==================

Fire Insights REST API's can be accessed with Python. Session Cookie can be acquired using username and password and used in the subsequent calls.


Get List of Processors
----------------------

The below code in Python gets the list of Processors in Fire Insights using the REST API and prints them.

.. code-block:: python
   :linenos:

   #!/usr/bin/python

   # This python script logs into an instance of sparkflows, and then gets the list of Processors/Operators supported

   # -*- coding: utf-8 -*-
   import json
   import requests

   payload = {'username':'admin', 'password':'admin'}

   # login url
   urllogin = 'http://localhost:8080/login'

   # get list of processors url
   urlprocessors = 'http://localhost:8080/nodeList'

   with requests.session() as s:

     # log into sparkflows
     s.get(urllogin)

     r = s.post(urllogin, data=payload)

     # get list of processors
     resp = s.get(urlprocessors)

     parsed_resp = json.loads(resp.text)

     for i in parsed_resp:
       print (i['name'])
    
