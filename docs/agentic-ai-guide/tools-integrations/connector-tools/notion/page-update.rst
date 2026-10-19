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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_page_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes a page's property values, or moves the page to the trash or back, and returns the updated page. Content blocks are changed with Block append and Block delete instead.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.
* The account behind the connection must be allowed to change this data in Notion.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **update** in the **Page** row, then click **Add to agent**.

The agent now sees ``notion_page_update`` and calls it when a request needs it.

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
     - The id of the page to change, from Database query or Search run. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``properties``
     - JSON object
     - No
     - Property values to change, in the same JSON as Page create; properties not named keep their values. Example: {"Status": {"select": {"name": "Done"}}}.
   * - ``archived``
     - true or false
     - No
     - true moves the page to the trash, false restores it.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Notion.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-get.html">Get a page</a><a href="page-create.html">Create a page</a></div>
