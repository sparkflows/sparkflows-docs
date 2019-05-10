REST API with Python
==================

Below is an example program for accessing Fire Insights REST API's with Python.

```

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
    
    
```

