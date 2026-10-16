:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Database</p>

Update a database
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Database</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_database_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes a database's title, description or columns and returns the updated database. Rows are changed with Page update instead.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.
* The account behind the connection must be allowed to change this data in Notion.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **update** in the **Database** row, then click **Add to agent**.

The agent now sees ``notion_database_update`` and calls it when a request needs it.

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
   * - ``databaseId``
     - text
     - Yes
     - The database to change, from Search run or the database's URL. Example: d9824bdc-8445-4327-be8b-5b47500af6ce.
   * - ``title``
     - list of JSON object
     - No
     - The new title as Notion rich text. Example: [{"type": "text", "text": {"content": "Vendor tasks 2026"}}].
   * - ``description``
     - list of JSON object
     - No
     - The new description as Notion rich text. Example: [{"type": "text", "text": {"content": "Open vendor actions, one row each."}}].
   * - ``properties``
     - JSON object
     - No
     - Columns to change by name: a definition adds or changes one, {"name": "New name"} renames one and null removes one. Example: {"Owner": {"people": {}}, "Old column": null}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Notion.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-get.html">Get a database</a><a href="database-query.html">Query a database</a><a href="database-create.html">Create a database</a></div>
