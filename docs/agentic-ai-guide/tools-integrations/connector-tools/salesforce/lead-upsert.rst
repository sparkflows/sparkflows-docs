:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Create or update a lead by external id
======================================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_upsert</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a lead, or updates the one whose external id field already holds the same value, so a repeated sync never makes duplicates; returns the external id. Use it for records that another system keys; use Create a lead or Update a lead when there is no external id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **upsert** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_upsert`` and calls it when a request needs it.

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
   * - ``externalIdField``
     - text
     - Yes
     - The API name of a Lead field marked External ID, for example External\_Id\_\_c; its value goes in fields.
   * - ``fields``
     - JSON object
     - Yes
     - The lead's fields as API name to value, including the external id field with its value and, in case the lead is new, its required fields, for example {"External\_Id\_\_c": "WEB-88120", "LastName": "Mehta", "Company": "Brightline Solar"}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create or update a lead by external id** every time a flow reaches it, without the agent deciding, use the :doc:`Create or update a lead by external id App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-upsert>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-create.html">Create a lead</a><a href="lead-update.html">Update a lead</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a><a href="lead-convert.html">Convert a lead</a></div>
