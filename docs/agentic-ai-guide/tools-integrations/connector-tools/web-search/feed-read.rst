:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Feed</p>

Read a feed
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/web_tools.svg" alt="Web Search logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Web Search</dd></div>
     <div><dt>Resource</dt><dd>Feed</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/web-search.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Downloads an RSS or Atom feed and returns its entries with title, link, published date and summary, capped at limit. Page fetch reads an entry's full article.

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
     - The feed's address; https:// is added when no scheme is given, and cloud metadata and link-local addresses such as 169.254.169.254 are refused. Example: https://www.example.com/blog/rss.xml.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many entries at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Web Search**, connect, and tick **read** in the **Feed** row. The model sees it as ``web_tools_feed_read``.

**As an App Action.** Drop **App Action** on the canvas, pick **Web Search**, then **Read a feed**, and fill in the inputs above. It runs every time the flow reaches it.
