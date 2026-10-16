:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Convert a lead
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_convert</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Converts a lead into an account and a contact, plus an opportunity unless doNotCreateOpportunity is true, and returns Salesforce's answer. Use it once a lead is qualified; a converted lead can no longer be edited.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **convert** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_convert`` and calls it when a request needs it.

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
   * - ``leadId``
     - text
     - Yes
     - The lead's Salesforce Id, 15 or 18 characters starting 00Q, for example 00QXX000001Bc3K; List leads returns it.
   * - ``convertedStatus``
     - text
     - No
     - A lead status that this org marks as converted, for example Closed - Converted; blank sends Qualified.
   * - ``doNotCreateOpportunity``
     - true or false
     - No
     - true converts the lead without creating an opportunity. Example: false.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Convert a lead** every time a flow reaches it, without the agent deciding, use the :doc:`Convert a lead App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-convert>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-create.html">Create a lead</a><a href="lead-update.html">Update a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a></div>
