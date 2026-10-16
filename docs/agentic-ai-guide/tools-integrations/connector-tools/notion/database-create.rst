:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Database</p>

Create a database
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Database</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_database_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a database under a page with the columns given and returns it with its id. Page create with that id as databaseId then adds rows.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.
* The account behind the connection must be allowed to change this data in Notion.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **create** in the **Database** row, then click **Add to agent**.

The agent now sees ``notion_database_create`` and calls it when a request needs it.

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
   * - ``parentPageId``
     - text
     - Yes
     - The page the database goes under. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``properties``
     - JSON object
     - Yes
     - The columns as Notion property definitions keyed by name, with exactly one title property. Example: {"Name": {"title": {}}, "Status": {"select": {"options": [{"name": "Open"}, {"name": "Done"}]}}, "Due": {"date": {}}}.
   * - ``title``
     - list of JSON object
     - No
     - The database title as Notion rich text. Example: [{"type": "text", "text": {"content": "Vendor tasks"}}].
   * - ``isInline``
     - true or false
     - No
     - true shows the database inside the parent page rather than as a page of its own.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Notion.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-get.html">Get a database</a><a href="database-query.html">Query a database</a><a href="database-update.html">Update a database</a></div>
