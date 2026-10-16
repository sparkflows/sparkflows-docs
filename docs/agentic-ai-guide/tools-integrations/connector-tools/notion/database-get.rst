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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a database's title, parent and property schema: each property's name and type and, for select properties, their options. Use it before Database query or Page create to learn the exact property names.

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
   * - ``databaseId``
     - text
     - Yes
     - The database's id, from Search run or the database's URL. Example: d9824bdc-8445-4327-be8b-5b47500af6ce.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **get** in the **Database** row. The model sees it as ``notion_database_get``.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-query.html">Query a database</a><a href="database-create.html">Create a database</a><a href="database-update.html">Update a database</a></div>
