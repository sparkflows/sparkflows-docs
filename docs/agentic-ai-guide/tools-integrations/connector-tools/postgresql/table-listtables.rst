:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../postgresql.html">PostgreSQL</a> › Table</p>

List tables
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/postgresql.svg" alt="PostgreSQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>PostgreSQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/postgresql.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the tables in one schema, one row per table with its schema and name. Use it to find what the database holds; Table describe then gives a table's columns.

Prerequisites
-------------

* **Connection:** PostgreSQL connection connection. See :doc:`the PostgreSQL prerequisites <../postgresql>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``schema``
     - Schema
     - text
     - No
     - The schema to list, for example sales; blank lists the connection's default schema, usually public.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **PostgreSQL**, connect, and tick **listTables** in the **Table** row. The model sees it as ``postgresql_table_listtables``.

**As an App Action.** Drop **App Action** on the canvas, pick **PostgreSQL**, then **List tables**, and fill in the inputs above. It runs every time the flow reaches it.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listschemas.html">List schemas</a></div>
