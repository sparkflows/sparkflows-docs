:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../web-search.html">Web Search</a> › Page</p>

Fetch a web page
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Downloads a web page and returns its title and readable text with scripts and styles removed, cut to maxChars, or the raw HTML when stripTags is false.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/web-search>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Web Search**.
#. **Action:** under **Page**, choose **Fetch a web page**.
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
   * - **Readable text only**
     - No
     - What the page comes back as.

       * ``true``: Readable text.
       * ``false``: The page's HTML.

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
     - Some records keep a value inside another value, such as a priority inside an issue. This decides how those inner values become columns.

       * ``deep`` (default): Every inner value gets its own column, named with dots, such as ``fields.priority.name``.
       * ``oneLevel``: Only the first level is split. Anything deeper stays in one column as JSON text.
       * ``json``: Each inner value stays whole, in one column of JSON text.

       See the example below the table.

**Nested fields, by example.** Take a record ``{"id": 7, "fields": {"priority": {"name": "High"}}}``. Each choice gives you these columns:

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: tool-table

   * - Choice
     - Columns you get
   * - ``deep``
     - ``id`` = ``7`` and ``fields.priority.name`` = ``High``
   * - ``oneLevel``
     - ``id`` = ``7`` and ``fields.priority`` = ``{"name": "High"}``
   * - ``json``
     - ``id`` = ``7`` and ``fields`` = ``{"priority": {"name": "High"}}``

Keep ``deep`` unless a later step needs the whole inner value as JSON.

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
   * - **Page changed**
     - URL is the page to watch. Each check reads the page as text and reports it when the text differs from the last check; the first check records the page. A page that answers with an error fails the check.
   * - **Page starts showing a text**
     - URL is the page to watch, and Filter the text to look for, such as In stock or Registration open, matched regardless of case. The page is reported once, on the first check that finds the text; a text already on the page at the first check is recorded, not reported.

Let an agent decide instead
---------------------------

To let an agent call **Fetch a web page** only when a request needs it, add the :doc:`Fetch a web page tool </agentic-ai-guide/tools-integrations/connector-tools/web-search/page-fetch>` to an Agent Node.

Other Page actions
------------------

.. raw:: html

   <div class="tool-related"><a href="page-links.html">List the links on a page</a><a href="page-status.html">Check a URL</a><a href="page-crawl.html">Crawl a site</a></div>
