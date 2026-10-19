:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › Query</p>

Run a SQL statement
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>Query</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>database_query_run</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs one statement in the connected database's own SQL and commits it: a query returns its rows up to limit, and any other statement returns rowsAffected. Use it for joins, sorting, grouping and anything the table operations cannot express; since it can also change data, it counts as a change.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.
* The account behind the connection must be allowed to change this data in SQL Database.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **run** in the **Query** row, then click **Add to agent**.

The agent now sees ``database_query_run`` and calls it when a request needs it.

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
     - One statement in the database's own SQL, run as written and committed; add LIMIT (TOP on SQL Server, FETCH FIRST n ROWS ONLY on Oracle) for large results, since limit only cuts the rows after the database has returned them. Example: SELECT status, COUNT(\*) AS orders FROM orders GROUP BY status.
   * - ``limit``
     - whole number
     - No
     - How many rows of a query's result to return at most. Default: 50.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SQL Database.

Other Query tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="query-explain.html">Explain a query</a></div>
