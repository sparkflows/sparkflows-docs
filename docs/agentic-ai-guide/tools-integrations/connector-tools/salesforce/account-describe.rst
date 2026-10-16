:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Account</p>

Describe account fields
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Account</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_account_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the Account object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the org's exact field names, custom \_\_c fields included, before a create, update or query.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **Account** row, then click **Add to agent**.

The agent now sees ``salesforce_account_describe`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **Describe account fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe account fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/account-describe>`.

Other Account tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="account-get.html">Get an account</a><a href="account-getmany.html">List accounts</a><a href="account-create.html">Create an account</a><a href="account-update.html">Update an account</a><a href="account-upsert.html">Create or update an account by external id</a><a href="account-delete.html">Delete an account</a><a href="account-search.html">Search accounts</a><a href="account-count.html">Count accounts</a><a href="account-addnote.html">Add a note to an account</a></div>
