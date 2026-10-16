:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../postgresql.html">PostgreSQL</a> › Query</p>

Run a SQL statement
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/postgresql.svg" alt="PostgreSQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>PostgreSQL</dd></div>
     <div><dt>Resource</dt><dd>Query</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/postgresql.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs one PostgreSQL statement and commits it: a SELECT, WITH, VALUES or EXPLAIN statement returns its rows up to limit, and any other statement returns rowsAffected. Use it for joins, grouping and anything Table getMany cannot express; since it can also change data, it counts as a change.

Prerequisites
-------------

* **Connection:** PostgreSQL connection connection. See :doc:`the PostgreSQL prerequisites <../postgresql>`.
* The connection's account must be allowed to change this data in PostgreSQL.

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
     - One PostgreSQL statement, run as written and committed; add LIMIT for large results, since limit only cuts the rows after the database has returned them. Example: SELECT date\_trunc('month', created\_at) AS month, SUM(total) AS revenue FROM orders GROUP BY 1 ORDER BY 1 DESC LIMIT 12.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many rows of a query's result to return at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **PostgreSQL**, connect, and tick **run** in the **Query** row. The model sees it as ``postgresql_query_run``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **PostgreSQL**, then **Run a SQL statement**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.
