Accessing REST API using OAuth token
====================================

Below is an example Python code for accessing the Fire REST API using tokens.

  ::
    
    #!/usr/bin/python

    import requests

    import json

    import getpass

    token_url = "http://localhost:8080/oauth/token"

    processor_count_api_url = "http://localhost:8080/getNodeCount" # processor list count api of sparkflows

    Step A - resource owner supplies credentials
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
  
