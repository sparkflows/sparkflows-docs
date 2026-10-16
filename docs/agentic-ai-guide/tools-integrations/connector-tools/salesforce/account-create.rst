:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Account</p>

Create an account
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Account</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an account (a company or organisation) from the given fields and returns its new Id. Use Create or update an account by external id instead when syncing records that another system keys.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.
* The connection's account must be allowed to change this data in Salesforce.

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
   * - ``name``
     - Account name
     - text
     - Yes
     - The company or organisation name. Example: Acme Energy Ltd.
   * - ``type``
     - Type
     - text
     - No
     - The account type as the org's picklist names it, for example Prospect or Customer - Direct.
   * - ``industry``
     - Industry
     - text
     - No
     - The industry picklist value, for example Energy or Banking.
   * - ``phone``
     - Phone
     - text
     - No
     - The main phone number. Example: +44 20 7946 0958.
   * - ``website``
     - Website
     - text
     - No
     - The company's website address. Example: https://www.acme-energy.example.com.
   * - ``billingCity``
     - Billing city
     - text
     - No
     - The city of the billing address. Example: Pune.
   * - ``billingCountry``
     - Billing country
     - text
     - No
     - The country of the billing address. Example: India.
   * - ``annualRevenue``
     - Annual revenue
     - number
     - No
     - Yearly revenue as a number, in the org's currency. Example: 25000000.
   * - ``numberOfEmployees``
     - Employees
     - whole number
     - No
     - The number of employees. Example: 1200.
   * - ``description``
     - Description
     - text
     - No
     - Free-text notes about the account. Example: Key account for the western region; renewal due in March..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **create** in the **Account** row. The model sees it as ``salesforce_account_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Create an account**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Account tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="account-get.html">Get an account</a><a href="account-getmany.html">List accounts</a><a href="account-update.html">Update an account</a><a href="account-upsert.html">Create or update an account by external id</a><a href="account-delete.html">Delete an account</a><a href="account-search.html">Search accounts</a><a href="account-describe.html">Describe account fields</a><a href="account-count.html">Count accounts</a><a href="account-addnote.html">Add a note to an account</a></div>
