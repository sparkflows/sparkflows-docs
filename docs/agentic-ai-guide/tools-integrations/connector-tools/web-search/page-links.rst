:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Page</p>

List the links on a page
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/web-search.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches a page and returns the unique links in it as absolute URLs with their host, capped at limit; by default only links to the page's own host. Relative links are resolved the way a browser does.

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
     - The page's address; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://www.sparkflows.io/.
   * - ``sameHostOnly``
     - Same host only
     - true or false
     - No
     - true keeps links to the page's own host only. Default: True.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many links at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Web Search**, connect, and tick **links** in the **Page** row. The model sees it as ``web_tools_page_links``.

**As an App Action.** Drop **App Action** on the canvas, pick **Web Search**, then **List the links on a page**, and fill in the inputs above. It runs every time the flow reaches it.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-fetch.html">Fetch a web page</a><a href="page-status.html">Check a URL</a><a href="page-crawl.html">Crawl a site</a></div>
