Accessing REST API using Python
====================================

Below are examples of Python code for accessing the Fire REST API using Python.

It is used to get processor count with below REST API using Python.

Get Processor Count
--------------------

  ::
    
    #!/usr/bin/python

    import requests

    import json

    import getpass

    token_url = "http://localhost:8080/oauth/token"

    processor_count_api_url = "http://localhost:8080/getNodeCount" # processor list count api of sparkflows

    #Step A - resource owner supplies credentials
    #Resource owner (enduser) credentials

    RO_user = 'admin'
    RO_password = 'admin'

    #client (application) credentials
    client_id = 'sparkflows'
    client_secret = 'secret'

    #step B, C - single call with resource owner credentials in the body and client credentials as the basic auth header will return #access_token

    data = {'grant_type': 'password','username': RO_user, 'password': RO_password}

    access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

    print(access_token_response.headers)
    print(access_token_response.text)

    tokens = json.loads(access_token_response.text)
    print( "access token: " + tokens['access_token'])

    # Step C - now we can use the access_token to make as many calls as we want.

    api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}

    print( api_call_headers)

    api_call_response = requests.get(processor_count_api_url, headers=api_call_headers, verify=False)

    print(api_call_response.text)

After running above REST API using Python, got the results as below


.. figure:: ../../_assets/tutorials/token/8.PNG
   :alt: REST API
   :align: center
   :width: 60%

  
Infer Cluster Configs
----------------------

The below code in Python invokes the Fire Insights REST API to infer the cluster configs. It then saves the inferred cluster configs as updated values.

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
   
   
