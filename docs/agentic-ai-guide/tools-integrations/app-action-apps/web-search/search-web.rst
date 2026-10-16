:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../web-search.html">Web Search</a> › Search</p>

Search the web
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches Google through Serper and returns the organic results with title, link, snippet and position.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/web-search>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Web Search**.
#. **Action:** under **Search**, choose **Search the web**.
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
   * - **Search text**
     - No
     - What to search for, as it would be typed into Google; operators such as site: and quotes work. For example ``sparkflows agent platform site:sparkflows.io``.
   * - **Limit**
     - No
     - How many links at most. Default: ``100``.
   * - **Country**
     - No
     - Two-letter country code for local results, for example us or in. For example ``in``.

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
   * - **New web search result**
     - Search text is what to search Google for through the Serper connection. The first check records the results already there; later checks report pages that newly appear among the top results.

Let an agent decide instead
---------------------------

To let an agent call **Search the web** only when a request needs it, add the :doc:`Search the web tool </agentic-ai-guide/tools-integrations/connector-tools/web-search/search-web>` to an Agent Node.

Other Search actions
--------------------

.. raw:: html

   <div class="tool-related"><a href="search-news.html">Search the news</a><a href="search-images.html">Search images</a><a href="search-places.html">Search places</a></div>
