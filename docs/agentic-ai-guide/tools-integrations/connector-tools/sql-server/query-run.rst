:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-server.html">SQL Server</a> › Query</p>

Run a SQL statement
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Query</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sql-server.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs one SQL Server statement and commits it: a SELECT or WITH query returns its rows up to limit, and any other statement returns rowsAffected. Use it for joins, grouping and anything Table getMany cannot express; since it can also change data, it counts as a change.

Prerequisites
-------------

* **Connection:** SQL Server connection connection. See :doc:`the SQL Server prerequisites <../sql-server>`.
* The connection's account must be allowed to change this data in SQL Server.

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
   * - ``sql``
     - SQL
     - text
     - Yes
     - One T-SQL statement, run as written and committed; add TOP for large results, since limit only cuts the rows after the database has returned them. Example: SELECT TOP 20 c.name, COUNT(\*) AS orders FROM customers c JOIN orders o ON o.customer\_id = c.id GROUP BY c.name ORDER BY orders DESC.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many rows of a query's result to return at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SQL Server**, connect, and tick **run** in the **Query** row. The model sees it as ``sqlserver_query_run``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SQL Server**, then **Run a SQL statement**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.
