:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Page</p>

Crawl a site
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>web_tools_page_crawl</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Starts at a URL and follows links breadth-first, returning one row per page visited with its URL, title and the first 4,000 characters of its text, up to limit pages. Page fetch reads one whole page.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up <../web-search>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Web Search** under **Connectors** and connect your Serper (searches only) connection.
#. Tick **crawl** in the **Page** row, then click **Add to agent**.

The agent now sees ``web_tools_page_crawl`` and calls it when a request needs it.

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
     - The page to start from; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://docs.sparkflows.io/.
   * - ``limit``
     - whole number
     - No
     - How many pages at most; 25 is the ceiling. Default: 10.
   * - ``sameHostOnly``
     - true or false
     - No
     - true follows links to the starting host only. Default: True.

Need it on every run?
---------------------

To run **Crawl a site** every time a flow reaches it, without the agent deciding, use the :doc:`Crawl a site App Action </agentic-ai-guide/tools-integrations/app-action-apps/web-search/page-crawl>`.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-fetch.html">Fetch a web page</a><a href="page-links.html">List the links on a page</a><a href="page-status.html">Check a URL</a></div>
