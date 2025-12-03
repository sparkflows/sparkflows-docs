REST API Authentication
==========

To authenticate and access Sparkflows REST APIs, you can use personal access tokens or passwords. We strongly recommend that you use tokens. Like passwords, tokens should be treated with care. Unlike passwords, tokens expire and can be revoked.

Tokens can be generated using Postman.

You can also log in with your username/password, get a session cookie, store it into a file and use it in subsequent requests.

.. toctree::
   :maxdepth: 2

   acquire-session-cookie.rst
   python-session-cookie.rst
   acquire-token-curl.rst
   configure-fire-restapi.rst
