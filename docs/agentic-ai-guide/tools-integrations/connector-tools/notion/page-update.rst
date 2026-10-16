:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Page</p>

Update page properties
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes a page's property values, or moves the page to the trash or back, and returns the updated page. Content blocks are changed with Block append and Block delete instead.

Prerequisites
-------------

* **Connection:** Notion connection. See :doc:`the Notion prerequisites <../notion>`.
* The connection's account must be allowed to change this data in Notion.

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
     - The id of the page to change, from Database query or Search run. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``properties``
     - JSON object
     - No
     - Property values to change, in the same JSON as Page create; properties not named keep their values. Example: {"Status": {"select": {"name": "Done"}}}.
   * - ``archived``
     - true or false
     - No
     - true moves the page to the trash, false restores it.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **update** in the **Page** row. The model sees it as ``notion_page_update``. Each call waits for human approval before it changes anything.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-get.html">Get a page</a><a href="page-create.html">Create a page</a></div>
