:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Request</p>

Send a GET request
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Request</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/web-search.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sends an HTTP GET to a URL and returns the HTTP status (status and httpStatus), content type, size and the response as JSON text (json) or as text (body), cut to maxChars. Error statuses are returned rather than raised; Page fetch is better for reading a web page.

Prerequisites
-------------

* **Connection:** Serper (searches only) connection. See :doc:`the Web Search prerequisites <../web-search>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``url``
     - URL
     - text
     - Yes
     - The address to request, with any query parameters in it; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://api.example.com/v1/orders?status=open.
   * - ``headers``
     - Headers
     - JSON object
     - No
     - Extra request headers as a JSON object, such as Authorization, sent beside a Sparkflows User-Agent. Example: {"Authorization": "Bearer <token>", "Accept": "application/json"}.
   * - ``maxChars``
     - Characters kept
     - whole number
     - No
     - The most characters of the response kept. Default: 60000.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Web Search**, connect, and tick **get** in the **Request** row. The model sees it as ``web_tools_request_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Web Search**, then **Send a GET request**, and fill in the inputs above. It runs every time the flow reaches it.

Other Request tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="request-post.html">Send a POST request</a><a href="request-put.html">Send a PUT request</a><a href="request-patch.html">Send a PATCH request</a><a href="request-delete.html">Send a DELETE request</a></div>
