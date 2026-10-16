:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Database</p>

Query a database
================

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

   Returns the rows (pages) of a database that match a filter, in the order given, each with its id, URL, times and property values, following Notion's pages up to the limit. Database get shows the property names a filter uses.

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
     - The database to query, from Search run or the database's URL. Example: d9824bdc-8445-4327-be8b-5b47500af6ce.
   * - ``filter``
     - JSON object
     - No
     - A Notion filter object on a property or a timestamp, combined with and/or; blank returns every row. Example: {"property": "Status", "select": {"equals": "Open"}}.
   * - ``sorts``
     - list of JSON object
     - No
     - The sort order as a list of property or timestamp sorts, each with a direction of ascending or descending. Example: [{"property": "Due", "direction": "ascending"}].
   * - ``limit``
     - whole number
     - No
     - How many rows at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **query** in the **Database** row. The model sees it as ``notion_database_query``.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-get.html">Get a database</a><a href="database-create.html">Create a database</a><a href="database-update.html">Update a database</a></div>
