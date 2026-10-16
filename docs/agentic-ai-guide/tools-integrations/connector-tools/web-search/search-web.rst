:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Search</p>

Search the web
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>web_tools_search_web</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches Google through Serper and returns the organic results with title, link, snippet and position. Page fetch reads a result's page; Search news suits recent events.

Before you start
----------------

* A Serper (searches only) connection. See :doc:`how to set one up <../web-search>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Web Search** under **Connectors** and connect your Serper (searches only) connection.
#. Tick **web** in the **Search** row, then click **Add to agent**.

The agent now sees ``web_tools_search_web`` and calls it when a request needs it.

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
   * - ``query``
     - text
     - Yes
     - What to search for, as it would be typed into Google; operators such as site: and quotes work. Example: sparkflows agent platform site:sparkflows.io.
   * - ``country``
     - text
     - No
     - Two-letter country code for local results, for example us or in.
   * - ``limit``
     - whole number
     - No
     - How many results at most (up to 100). Default: 10.

Need it on every run?
---------------------

To run **Search the web** every time a flow reaches it, without the agent deciding, use the :doc:`Search the web App Action </agentic-ai-guide/tools-integrations/app-action-apps/web-search/search-web>`.

Other Search tools
------------------

.. raw:: html

   <div class="tool-related"><a href="search-news.html">Search the news</a><a href="search-images.html">Search images</a><a href="search-places.html">Search places</a></div>
