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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/web-search.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches Google through Serper and returns the organic results with title, link, snippet and position. Page fetch reads a result's page; Search news suits recent events.

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
   * - ``query``
     - Search text
     - text
     - Yes
     - What to search for, as it would be typed into Google; operators such as site: and quotes work. Example: sparkflows agent platform site:sparkflows.io.
   * - ``country``
     - Country
     - text
     - No
     - Two-letter country code for local results, for example us or in.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many results at most (up to 100). Default: 10.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Web Search**, connect, and tick **web** in the **Search** row. The model sees it as ``web_tools_search_web``.

**As an App Action.** Drop **App Action** on the canvas, pick **Web Search**, then **Search the web**, and fill in the inputs above. It runs every time the flow reaches it.

Other Search tools
------------------

.. raw:: html

   <div class="tool-related"><a href="search-news.html">Search the news</a><a href="search-images.html">Search images</a><a href="search-places.html">Search places</a></div>
