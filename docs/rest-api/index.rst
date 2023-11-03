REST API
========

Fire Insights provides REST API for other systems and scripts to integrate with it.

The admin user can also enable swagger through configuration. Once enabled swagger is available at http://<machine-name>:8080/swagger-ui.html.

To authenticate and access Fire Insights REST APIs, you can use personal access tokens or passwords. We strongly recommend that you use tokens. Like passwords, tokens should be treated with care. Unlike passwords, tokens expire and can be revoked.

A number of scripts for interacting with the REST API's can be found here : https://github.com/sparkflows/fire-tools/tree/main/rest-api-scripts

.. panels::
    :container: container-lg pb-3
    :column: col-lg-12 p-2

    :doc:`/rest-api/rest-api-authentication/index`

    Steps to authenticate and access REST APIs.

    ---
    :doc:`/rest-api/rest-api-python/index`

    Accessing REST API Using Python.

    ---

    :doc:`/rest-api/rest-api-java/index`

    Accessing REST API Using Java.

    ---

    :doc:`/rest-api/rest-api-curl/index`

    Accessing REST API Using curl.


.. toctree::
   :hidden:

   rest-api-authentication/index

.. toctree::
   :hidden:

   rest-api-python/index


.. toctree::
   :hidden:

   rest-api-java/index

.. toctree::
   :hidden:

   rest-api-curl/index

.. toctree::
   :hidden:

   rest-apis.rst

