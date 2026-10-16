:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Campaign</p>

Update a campaign
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Campaign</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_campaign_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing campaign and leaves the others as they are; returns the campaign's Id. The campaign is named by its Salesforce Id, which List campaigns returns.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **update** in the **Campaign** row, then click **Add to agent**.

The agent now sees ``salesforce_campaign_update`` and calls it when a request needs it.

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
     - The Salesforce Id of the campaign to change, starting 701, for example 701XX0000001234; List campaigns returns it.
   * - ``name``
     - text
     - No
     - The campaign's name. Example: Energy Transition Webinar 2026.
   * - ``status``
     - text
     - No
     - The campaign status, for example Planned, In Progress, Completed or Aborted.
   * - ``startDate``
     - text
     - No
     - The first day as YYYY-MM-DD. Example: 2026-11-04.
   * - ``endDate``
     - text
     - No
     - The last day as YYYY-MM-DD. Example: 2026-11-30.
   * - ``isActive``
     - true or false
     - No
     - true marks the campaign active.
   * - ``budgetedCost``
     - number
     - No
     - The planned spend as a number. Example: 15000.
   * - ``description``
     - text
     - No
     - Free-text notes about the campaign. Example: Joint webinar with the grid-storage partner..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Update a campaign** every time a flow reaches it, without the agent deciding, use the :doc:`Update a campaign App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/campaign-update>`.

Other Campaign tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="campaign-get.html">Get a campaign</a><a href="campaign-getmany.html">List campaigns</a><a href="campaign-create.html">Create a campaign</a><a href="campaign-delete.html">Delete a campaign</a></div>
