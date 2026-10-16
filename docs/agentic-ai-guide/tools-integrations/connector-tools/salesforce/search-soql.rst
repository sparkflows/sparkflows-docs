:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Search</p>

Run a SOQL query
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_search_soql</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs any SOQL statement and returns every matching row, following Salesforce's paging, with relationship fields nested. Use it for joins, subqueries, GROUP BY or objects the other operations do not cover; put a LIMIT in the statement, because nothing else caps the rows.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **soql** in the **Search** row, then click **Add to agent**.

The agent now sees ``salesforce_search_soql`` and calls it when a request needs it.

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
   * - ``soql``
     - text
     - Yes
     - A complete SOQL statement, for example SELECT Id, Name, Account.Name FROM Opportunity WHERE StageName = 'Closed Won' AND CloseDate = THIS\_YEAR LIMIT 200. Example: SELECT Id, Name, Industry FROM Account WHERE Industry = 'Energy' LIMIT 100.

Need it on every run?
---------------------

To run **Run a SOQL query** every time a flow reaches it, without the agent deciding, use the :doc:`Run a SOQL query App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/search-soql>`.
