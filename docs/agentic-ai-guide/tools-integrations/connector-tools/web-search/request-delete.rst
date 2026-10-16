:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Request</p>

Send a DELETE request
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Request</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>web_tools_request_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sends an HTTP DELETE to a URL and returns the response as JSON text (json) or as text (body). The HTTP code comes back as httpStatus, and a 4xx or 5xx answer reads as failed.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up <../web-search>`.
* The account behind the connection must be allowed to change this data in Web Search.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Web Search** under **Connectors** and connect your Serper (searches only) connection.
#. Tick **delete** in the **Request** row, then click **Add to agent**.

The agent now sees ``web_tools_request_delete`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``url``
     - text
     - Yes
     - The address to request, with any query parameters in it; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://api.example.com/v1/orders?status=open.
   * - ``headers``
     - JSON object
     - No
     - Extra request headers as a JSON object, such as Authorization, sent beside a Sparkflows User-Agent. Example: {"Authorization": "Bearer <token>", "Accept": "application/json"}.
   * - ``maxChars``
     - whole number
     - No
     - The most characters of the response kept. Default: 60000.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Web Search.

Need it on every run?
---------------------

To run **Send a DELETE request** every time a flow reaches it, without the agent deciding, use the :doc:`Send a DELETE request App Action </agentic-ai-guide/tools-integrations/app-action-apps/web-search/request-delete>`.

Other Request tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="request-get.html">Send a GET request</a><a href="request-post.html">Send a POST request</a><a href="request-put.html">Send a PUT request</a><a href="request-patch.html">Send a PATCH request</a></div>
