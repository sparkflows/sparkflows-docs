REST API with Python
==================

Fire Insights REST API's can be accessed with Python.

Get List of Processors
----------------------

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
    
    
Create a New Workflow
----------------------

The Workflow JSON is saved in a file called ``workflow.json``.

It creates a new Workflow in the Project with id 1.


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

   # save workflow url
   urlsaveworkflow = 'http://localhost:8080/saveWorkflow'

   # read workflow json
   wf = open("workflow.json","r", encoding='utf8')
   workflow = wf.read()

   # define other parameters
   analysisFlowId = "null"
   projectId = "1"
   engine = "scala"

   with requests.session() as s:

     # log into sparkflows
     s.get(urllogin)

     r = s.post(urllogin, data=payload)

     # save workflow
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'analysisFlowId': analysisFlowId, 'projectId': projectId, 'engine':engine }
     resp = s.post(urlsaveworkflow, data=workflow, headers=headers)

     print(resp)


   

