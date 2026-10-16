:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Block</p>

Append content to a page
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Block</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_block_append</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds content blocks at the end of a page or block, or after a given child block, and returns the new blocks. Up to 100 blocks go in one call.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.
* The account behind the connection must be allowed to change this data in Notion.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **append** in the **Block** row, then click **Add to agent**.

The agent now sees ``notion_block_append`` and calls it when a request needs it.

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
   * - ``blockId``
     - text
     - Yes
     - The page or block to add the content to. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``children``
     - list of JSON object
     - Yes
     - The blocks to add, as Notion block objects. Example: [{"object": "block", "type": "to\_do", "to\_do": {"rich\_text": [{"type": "text", "text": {"content": "Send the signed contract"}}], "checked": false}}].
   * - ``after``
     - text
     - No
     - The id of an existing child block to insert after; blank adds at the end. Example: c02fc1d3-db8b-45c5-a222-27595b15aea7.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Notion.

Other Block tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="block-getmany.html">List a page&#x27;s content blocks</a><a href="block-delete.html">Delete a block</a></div>
