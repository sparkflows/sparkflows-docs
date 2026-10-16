:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Page</p>

Fetch a web page
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>web_tools_page_fetch</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Downloads a web page and returns its title and readable text with scripts and styles removed, cut to maxChars, or the raw HTML when stripTags is false. An HTTP error status fails the call; Request get suits APIs that answer in JSON.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up <../web-search>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Web Search** under **Connectors** and connect your Serper (searches only) connection.
#. Tick **fetch** in the **Page** row, then click **Add to agent**.

The agent now sees ``web_tools_page_fetch`` and calls it when a request needs it.

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
     - The page's address; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://www.sparkflows.io/.
   * - ``stripTags``
     - true or false
     - No
     - true returns readable text, false the HTML. Default: True.
   * - ``maxChars``
     - whole number
     - No
     - The most characters of text or HTML kept. Default: 60000.
   * - ``headers``
     - JSON object
     - No
     - Extra request headers as a JSON object, such as Authorization, sent beside a Sparkflows User-Agent. Example: {"Authorization": "Bearer <token>", "Accept": "application/json"}.

Need it on every run?
---------------------

To run **Fetch a web page** every time a flow reaches it, without the agent deciding, use the :doc:`Fetch a web page App Action </agentic-ai-guide/tools-integrations/app-action-apps/web-search/page-fetch>`.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-links.html">List the links on a page</a><a href="page-status.html">Check a URL</a><a href="page-crawl.html">Crawl a site</a></div>
