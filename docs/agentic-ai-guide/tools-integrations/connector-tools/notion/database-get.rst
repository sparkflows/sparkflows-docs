:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Database</p>

Get a database
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Database</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_database_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a database's title, parent and property schema: each property's name and type and, for select properties, their options. Use it before Database query or Page create to learn the exact property names.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **get** in the **Database** row, then click **Add to agent**.

The agent now sees ``notion_database_get`` and calls it when a request needs it.

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
     - The database's id, from Search run or the database's URL. Example: d9824bdc-8445-4327-be8b-5b47500af6ce.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-query.html">Query a database</a><a href="database-create.html">Create a database</a><a href="database-update.html">Update a database</a></div>
