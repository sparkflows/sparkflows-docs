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
     <div><dt>Tool name</dt><dd><code>notion_page_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one page's property values, parent, URL and created and last edited times. The page's content is read with Block getMany on the same id.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **get** in the **Page** row, then click **Add to agent**.

The agent now sees ``notion_page_get`` and calls it when a request needs it.

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
   * - ``pageId``
     - text
     - Yes
     - The page's id, from Database query, Search run or the last part of the page's URL. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-create.html">Create a page</a><a href="page-update.html">Update page properties</a></div>
