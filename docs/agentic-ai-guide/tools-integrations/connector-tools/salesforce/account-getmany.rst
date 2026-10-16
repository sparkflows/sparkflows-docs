:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Account</p>

List accounts
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Account</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries accounts with an optional SOQL condition and returns up to limit rows. Only standard fields come back unless fields names them, so list custom (\_\_c) and relationship fields such as Owner.Name explicitly. Use Run a SOQL query for aggregates, subqueries or several objects at once.

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
   * - ``where``
     - Where
     - text
     - No
     - A SOQL condition without the word WHERE, such as Industry = 'Energy' AND AnnualRevenue > 1000000, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every account up to the limit.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Field API names to return, such as ["Id", "Name", "Industry", "Owner.Name"]; blank returns the standard fields only.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many accounts at most. Example: 50. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **list** in the **Account** row. The model sees it as ``salesforce_account_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **List accounts**, and fill in the inputs above. It runs every time the flow reaches it.

Other Account tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="account-get.html">Get an account</a><a href="account-create.html">Create an account</a><a href="account-update.html">Update an account</a><a href="account-upsert.html">Create or update an account by external id</a><a href="account-delete.html">Delete an account</a><a href="account-search.html">Search accounts</a><a href="account-describe.html">Describe account fields</a><a href="account-count.html">Count accounts</a><a href="account-addnote.html">Add a note to an account</a></div>
