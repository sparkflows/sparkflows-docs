:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › DDL</p>

Run a DDL statement
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>DDL</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>database_ddl_execute</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs one statement that returns no rows, such as CREATE, ALTER, DROP, GRANT or EXEC, commits it and returns rowsAffected. Use Query run for statements that return rows, and Table create for a plain new table.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.
* The account behind the connection must be allowed to change this data in SQL Database.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **execute** in the **DDL** row, then click **Add to agent**.

The agent now sees ``database_ddl_execute`` and calls it when a request needs it.

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
   * - ``statement``
     - text
     - Yes
     - One statement in the database's own SQL, run as written and committed. Example: ALTER TABLE orders ADD COLUMN channel VARCHAR(40).

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SQL Database.
