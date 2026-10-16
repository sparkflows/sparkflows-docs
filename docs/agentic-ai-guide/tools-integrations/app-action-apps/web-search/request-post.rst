:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../web-search.html">Web Search</a> › Request</p>

Send a POST request
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Request</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sends an HTTP POST with a JSON body to a URL and returns the response as JSON text (json) or as text (body).

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/web-search>`.
* The account behind the connection must be allowed to change this data in Web Search.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Web Search**.
#. **Action:** under **Request**, choose **Send a POST request**.
#. **Details:** choose your Serper (searches only) connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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
   * - **If a row is rejected**
     - No
     - stop fails the run at the first rejected row. continue writes the rest and marks that row failed in result\_status and result\_error. Choices: ``stop``, ``continue``. Default: ``stop``.

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Web Search gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Send a POST request** only when a request needs it, add the :doc:`Send a POST request tool </agentic-ai-guide/tools-integrations/connector-tools/web-search/request-post>` to an Agent Node.

Other Request actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="request-get.html">Send a GET request</a><a href="request-put.html">Send a PUT request</a><a href="request-patch.html">Send a PATCH request</a><a href="request-delete.html">Send a DELETE request</a></div>
