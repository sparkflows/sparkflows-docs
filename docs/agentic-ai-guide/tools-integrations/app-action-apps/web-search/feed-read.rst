:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../web-search.html">Web Search</a> › Feed</p>

Read a feed
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Feed</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Downloads an RSS or Atom feed and returns its entries with title, link, published date and summary, capped at limit.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/web-search>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Web Search**.
#. **Action:** under **Feed**, choose **Read a feed**.
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
   * - **Limit**
     - No
     - How many links at most. Default: ``100``.
   * - **URL**
     - No
     - The address to request, with any query parameters in it; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. For example ``https://api.example.com/v1/orders?status=open``.

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

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Web Search with this action and start the flow when something new turns up. Pick **Web Search** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **New item in a feed**
     - URL is the RSS or Atom feed. The first check records the items already there; later checks report the new ones.
   * - **New feed item with a text in its title**
     - URL is the RSS or Atom feed, and Filter a text the item's title must contain, such as a company or product name. The first check records the matching items already there; later checks report each new one.

Let an agent decide instead
---------------------------

To let an agent call **Read a feed** only when a request needs it, add the :doc:`Read a feed tool </agentic-ai-guide/tools-integrations/connector-tools/web-search/feed-read>` to an Agent Node.
