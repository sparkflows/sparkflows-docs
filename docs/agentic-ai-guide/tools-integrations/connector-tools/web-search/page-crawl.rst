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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/web-search.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Starts at a URL and follows links breadth-first, returning one row per page visited with its URL, title and the first 4,000 characters of its text, up to limit pages. Page fetch reads one whole page.

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
     - The page to start from; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://docs.sparkflows.io/.
   * - ``limit``
     - Pages
     - whole number
     - No
     - How many pages at most; 25 is the ceiling. Default: 10.
   * - ``sameHostOnly``
     - Same host only
     - true or false
     - No
     - true follows links to the starting host only. Default: True.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Web Search**, connect, and tick **crawl** in the **Page** row. The model sees it as ``web_tools_page_crawl``.

**As an App Action.** Drop **App Action** on the canvas, pick **Web Search**, then **Crawl a site**, and fill in the inputs above. It runs every time the flow reaches it.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-fetch.html">Fetch a web page</a><a href="page-links.html">List the links on a page</a><a href="page-status.html">Check a URL</a></div>
