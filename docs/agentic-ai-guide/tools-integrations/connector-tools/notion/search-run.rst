:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Search</p>

Search pages and databases
==========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds the pages and databases shared with the integration whose titles match words, and returns them with ids, URLs and last edited times, following Notion's pages up to the limit. To find database rows by property values use Database query.

Prerequisites
-------------

* **Connection:** Notion connection. See :doc:`the Notion prerequisites <../notion>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``query``
     - text
     - No
     - Words matched against page and database titles; blank returns everything the integration can see. Example: Q3 review.
   * - ``filter``
     - JSON object
     - No
     - Only pages or only databases, as {"property": "object", "value": "page"} or with value database.
   * - ``sort``
     - JSON object
     - No
     - Order by last edit, as {"timestamp": "last\_edited\_time", "direction": "descending"} or ascending.
   * - ``limit``
     - whole number
     - No
     - How many results at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **run** in the **Search** row. The model sees it as ``notion_search_run``.
