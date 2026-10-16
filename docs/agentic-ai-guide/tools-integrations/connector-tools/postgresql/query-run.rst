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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>postgresql_query_run</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs one PostgreSQL statement and commits it: a SELECT, WITH, VALUES or EXPLAIN statement returns its rows up to limit, and any other statement returns rowsAffected. Use it for joins, grouping and anything Table getMany cannot express; since it can also change data, it counts as a change.

Before you start
----------------

* A PostgreSQL connection. See :doc:`how to set one up <../postgresql>`.
* The account behind the connection must be allowed to change this data in PostgreSQL.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **PostgreSQL** under **Connectors** and connect your PostgreSQL connection.
#. Tick **run** in the **Query** row, then click **Add to agent**.

The agent now sees ``postgresql_query_run`` and calls it when a request needs it.

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
   * - ``sql``
     - text
     - Yes
     - One PostgreSQL statement, run as written and committed; add LIMIT for large results, since limit only cuts the rows after the database has returned them. Example: SELECT date\_trunc('month', created\_at) AS month, SUM(total) AS revenue FROM orders GROUP BY 1 ORDER BY 1 DESC LIMIT 12.
   * - ``limit``
     - whole number
     - No
     - How many rows of a query's result to return at most. Default: 50.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in PostgreSQL.

Need it on every run?
---------------------

To run **Run a SQL statement** every time a flow reaches it, without the agent deciding, use the :doc:`Run a SQL statement App Action </agentic-ai-guide/tools-integrations/app-action-apps/postgresql/query-run>`.
