:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Account</p>

Search accounts
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Account</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_account_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds accounts that match a SOQL condition and returns up to limit rows with the chosen fields. It runs the same query as List accounts, so either serves; use Run a SOQL query for joins, aggregates or other objects.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **search** in the **Account** row, then click **Add to agent**.

The agent now sees ``salesforce_account_search`` and calls it when a request needs it.

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
   * - ``where``
     - text
     - No
     - A SOQL condition without the word WHERE, such as Industry = 'Energy' AND AnnualRevenue > 1000000, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every account up to the limit.
   * - ``fields``
     - list of text
     - No
     - Field API names to return, such as ["Id", "Name", "Industry", "Owner.Name"]; blank returns the standard fields only.
   * - ``limit``
     - whole number
     - No
     - How many accounts at most. Example: 50. Default: 50.

Need it on every run?
---------------------

To run **Search accounts** every time a flow reaches it, without the agent deciding, use the :doc:`Search accounts App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/account-search>`.

Other Account tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="account-get.html">Get an account</a><a href="account-getmany.html">List accounts</a><a href="account-create.html">Create an account</a><a href="account-update.html">Update an account</a><a href="account-upsert.html">Create or update an account by external id</a><a href="account-delete.html">Delete an account</a><a href="account-describe.html">Describe account fields</a><a href="account-count.html">Count accounts</a><a href="account-addnote.html">Add a note to an account</a></div>
