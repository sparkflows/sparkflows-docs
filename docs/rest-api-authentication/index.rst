REST API Authentication
==========

Sparkflows provides REST API for interacting with it.

Swagger is also enabled and is available at http://<machine-name>:8080/swagger-ui.html

To authenticate and access Fire Insights REST APIs, you can use personal access tokens or passwords. We strongly recommend that you use tokens. Like passwords, tokens should be treated with care. Unlike passwords, tokens expire and can be revoked.

Tokens can be generated using Postman.

You can also log in with your username/password, get a session cookie, store it into a file and use it in subsequent requests.

.. toctree::
   :maxdepth: 2

   acquire-session-cookie.rst
   restapi-postman.rst
   python-session-cookie.rst
   python-token.rst

