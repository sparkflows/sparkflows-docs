:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Block</p>

List a page's content blocks
============================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Block</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the content blocks directly inside a page or block (paragraphs, headings, lists, to-dos and so on), each with its type, text and whether it has children. Blocks whose has\_children is true hold more content, which another call on their id returns.

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
   * - ``blockId``
     - text
     - Yes
     - The page or block whose child blocks to list; a page id lists the page's content. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``limit``
     - whole number
     - No
     - How many blocks at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **list** in the **Block** row. The model sees it as ``notion_block_getmany``.

Other Block tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="block-append.html">Append content to a page</a><a href="block-delete.html">Delete a block</a></div>
