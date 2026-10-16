:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../web-search.html">Web Search</a> › Search</p>

Search places
=============

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

   Searches Google Maps through Serper and returns places with title, address, rating, category, phone number and website. Use it for businesses and locations, adding the city to the search text.

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

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Web Search**, connect, and tick **places** in the **Search** row. The model sees it as ``web_tools_search_places``.

**As an App Action.** Drop **App Action** on the canvas, pick **Web Search**, then **Search places**, and fill in the inputs above. It runs every time the flow reaches it.

Other Search tools
------------------

.. raw:: html

   <div class="tool-related"><a href="search-web.html">Search the web</a><a href="search-news.html">Search the news</a><a href="search-images.html">Search images</a></div>
