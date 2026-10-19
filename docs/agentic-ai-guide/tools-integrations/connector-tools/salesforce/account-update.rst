:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Account</p>

Update an account
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Account</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_account_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing account and leaves the others as they are; returns the account's Id. The account is named by its Salesforce Id, which List accounts returns.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **update** in the **Account** row, then click **Add to agent**.

The agent now sees ``salesforce_account_update`` and calls it when a request needs it.

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
   * - ``accountId``
     - text
     - Yes
     - The Salesforce Id of the account to change, starting 001, for example 001XX000003DHPh; List accounts returns it.
   * - ``name``
     - text
     - No
     - The company or organisation name. Example: Acme Energy Ltd.
   * - ``type``
     - text
     - No
     - The account type as the org's picklist names it, for example Prospect or Customer - Direct.
   * - ``industry``
     - text
     - No
     - The industry picklist value, for example Energy or Banking.
   * - ``phone``
     - text
     - No
     - The main phone number. Example: +44 20 7946 0958.
   * - ``website``
     - text
     - No
     - The company's website address. Example: https://www.acme-energy.example.com.
   * - ``billingCity``
     - text
     - No
     - The city of the billing address. Example: Pune.
   * - ``annualRevenue``
     - number
     - No
     - Yearly revenue as a number, in the org's currency. Example: 25000000.
   * - ``numberOfEmployees``
     - whole number
     - No
     - The number of employees. Example: 1200.
   * - ``ownerId``
     - text
     - No
     - The Id of the user who owns the account, starting 005; List users returns it. Example: 005XX000001Sv6e.
   * - ``description``
     - text
     - No
     - Free-text notes about the account. Example: Key account for the western region; renewal due in March..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Update an account** every time a flow reaches it, without the agent deciding, use the :doc:`Update an account App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/account-update>`.

Other Account tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="account-get.html">Get an account</a><a href="account-getmany.html">List accounts</a><a href="account-create.html">Create an account</a><a href="account-upsert.html">Create or update an account by external id</a><a href="account-delete.html">Delete an account</a><a href="account-search.html">Search accounts</a><a href="account-describe.html">Describe account fields</a><a href="account-count.html">Count accounts</a><a href="account-addnote.html">Add a note to an account</a></div>
