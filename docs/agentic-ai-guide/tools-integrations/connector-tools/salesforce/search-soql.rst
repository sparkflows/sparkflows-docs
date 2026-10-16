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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs any SOQL statement and returns every matching row, following Salesforce's paging, with relationship fields nested. Use it for joins, subqueries, GROUP BY or objects the other operations do not cover; put a LIMIT in the statement, because nothing else caps the rows.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.

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
   * - ``soql``
     - SOQL query
     - text
     - Yes
     - A complete SOQL statement, for example SELECT Id, Name, Account.Name FROM Opportunity WHERE StageName = 'Closed Won' AND CloseDate = THIS\_YEAR LIMIT 200. Example: SELECT Id, Name, Industry FROM Account WHERE Industry = 'Energy' LIMIT 100.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **soql** in the **Search** row. The model sees it as ``salesforce_search_soql``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Run a SOQL query**, and fill in the inputs above. It runs every time the flow reaches it.
