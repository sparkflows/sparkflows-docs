Acquire Session Cookie in Python
==================

Fire Insights REST API's can be accessed with Python. The Session Cookie can be acquired using the username and password, and then can be used in the subsequent calls.


Get List of Processors
----------------------

The below code in the Python, logs in the user and acquires the session cookie via the Fire Insights REST API.

It then gets the list of Processors in Fire Insights using the REST API and prints them.

.. code-block:: python
   :linenos:

   #!/usr/bin/python

   # This python script logs into an instance of sparkflows, and then gets the list of Processors/Operators supported

   # -*- coding: utf-8 -*-
   import json
   import requests

   payload = {'username':'admin', 'password':'admin'}

   # login url
   urllogin = 'http://localhost:8080/authenticate'

   # get list of processors url
   urlprocessors = 'http://localhost:8080/nodeList'

   with requests.session() as s:

     # log into sparkflows
     r = s.post(urllogin, data=payload)

     # get list of processors
     resp = s.get(urlprocessors)

     parsed_resp = json.loads(resp.text)

     for i in parsed_resp:
       print (i['name'])
    
