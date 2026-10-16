:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › Procedure</p>

Call a stored procedure
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>Procedure</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>database_procedure_invoke</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Calls a stored procedure with its arguments in order, argument1 first, as CALL name(...) or, on SQL Server, EXEC name ..., and commits. It returns the rows the procedure selects or hands back (INOUT values on PostgreSQL), or ok with rowsAffected when there are none.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.
* The account behind the connection must be allowed to change this data in SQL Database.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **invoke** in the **Procedure** row, then click **Add to agent**.

The agent now sees ``database_procedure_invoke`` and calls it when a request needs it.

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
   * - ``procedure``
     - text
     - Yes
     - The procedure's name, optionally with its schema, in letters, digits, underscore, dot and $ only (quoted names are refused). Example: billing.close\_month.
   * - ``argument1``
     - text
     - No
     - The procedure's first argument, as text the database converts to the parameter's type. Example: 2026-09.
   * - ``argument2``
     - text
     - No
     - The procedure's second argument, as text the database converts to the parameter's type; fill the arguments from argument1 up without gaps. Example: EMEA.
   * - ``argument3``
     - text
     - No
     - The procedure's third argument, as text the database converts to the parameter's type; fill the arguments from argument1 up without gaps. Example: true.
   * - ``argument4``
     - text
     - No
     - The procedure's fourth argument, as text the database converts to the parameter's type; fill the arguments from argument1 up without gaps. Example: 100.
   * - ``argument5``
     - text
     - No
     - The procedure's fifth argument, as text the database converts to the parameter's type; fill the arguments from argument1 up without gaps. Example: draft.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SQL Database.
