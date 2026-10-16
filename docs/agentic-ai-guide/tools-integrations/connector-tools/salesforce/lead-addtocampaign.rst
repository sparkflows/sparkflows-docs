:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Add a lead to a campaign
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_addtocampaign</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds the lead to a campaign as a campaign member and returns the member's Id. The member gets memberStatus when it is given, otherwise the campaign's default status; List campaigns returns campaign Ids.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **addToCampaign** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_addtocampaign`` and calls it when a request needs it.

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
   * - ``campaignId``
     - text
     - Yes
     - The Salesforce Id of the campaign, starting 701, for example 701XX0000001234; List campaigns returns it.
   * - ``leadId``
     - text
     - Yes
     - The Salesforce Id of the lead to add, starting 00Q, for example 00QXX000001Bc3K; List leads returns it.
   * - ``memberStatus``
     - text
     - No
     - The member's status in this campaign, one the campaign defines, for example Sent or Responded; blank uses the campaign's default.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Add a lead to a campaign** every time a flow reaches it, without the agent deciding, use the :doc:`Add a lead to a campaign App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-addtocampaign>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-create.html">Create a lead</a><a href="lead-update.html">Update a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-convert.html">Convert a lead</a></div>
