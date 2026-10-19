:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › Query</p>

Explain a query
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>Query</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>database_query_explain</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the database's plan for one query without running it (EXPLAIN, or EXPLAIN PLAN FOR on Oracle, which stores the plan in PLAN\_TABLE and returns only ok), and refuses an ANALYZE option or a second statement, since either would run SQL. Use it to see why a query is slow before running it; SQL Server has no EXPLAIN statement, so it fails there.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **explain** in the **Query** row, then click **Add to agent**.

The agent now sees ``database_query_explain`` and calls it when a request needs it.

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
     - The one query to explain, without the word EXPLAIN or its options in front. Example: SELECT \* FROM orders WHERE customer\_id = 42.

Other Query tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="query-run.html">Run a SQL statement</a></div>
