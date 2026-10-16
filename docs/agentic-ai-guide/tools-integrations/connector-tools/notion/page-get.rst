:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Page</p>

Get a page
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one page's property values, parent, URL and created and last edited times. The page's content is read with Block getMany on the same id.

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
   * - ``pageId``
     - text
     - Yes
     - The page's id, from Database query, Search run or the last part of the page's URL. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **get** in the **Page** row. The model sees it as ``notion_page_get``.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-create.html">Create a page</a><a href="page-update.html">Update page properties</a></div>
