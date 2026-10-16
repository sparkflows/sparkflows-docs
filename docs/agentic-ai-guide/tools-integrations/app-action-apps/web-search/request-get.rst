:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../web-search.html">Web Search</a> › Request</p>

Send a GET request
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Request</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sends an HTTP GET to a URL and returns the HTTP status (status and httpStatus), content type, size and the response as JSON text (json) or as text (body), cut to maxChars.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/web-search>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Web Search**.
#. **Action:** under **Request**, choose **Send a GET request**.
#. **Details:** choose your Serper (searches only) connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Web Search** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **URL**
     - No
     - The address to request, with any query parameters in it; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. For example ``https://api.example.com/v1/orders?status=open``.
   * - **Headers**
     - No
     - Extra request headers as a JSON object, such as Authorization, sent beside a Sparkflows User-Agent. For example ``{"Authorization": "Bearer <token>", "Accept": "application/json"}``.
   * - **Characters kept**
     - No
     - The most characters of the response kept.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Web Search** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Web Search with this action and start the flow when something new turns up. Pick **Web Search** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **API response changed**
     - URL is the address to call with GET. The first check records the answer; later checks report it, with httpStatus and the json or body, whenever anything in it differs. An answer holding a time or a request id differs on every check.

Let an agent decide instead
---------------------------

To let an agent call **Send a GET request** only when a request needs it, add the :doc:`Send a GET request tool </agentic-ai-guide/tools-integrations/connector-tools/web-search/request-get>` to an Agent Node.

Other Request actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="request-post.html">Send a POST request</a><a href="request-put.html">Send a PUT request</a><a href="request-patch.html">Send a PATCH request</a><a href="request-delete.html">Send a DELETE request</a></div>
