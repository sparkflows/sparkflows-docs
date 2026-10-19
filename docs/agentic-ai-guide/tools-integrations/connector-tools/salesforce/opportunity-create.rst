:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Opportunity</p>

Create an opportunity
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Opportunity</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_opportunity_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an opportunity (a deal in progress) from the given fields and returns its new Id. It needs name, stageName and closeDate, and stageName must be a stage from the org's sales process.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Opportunity** row, then click **Add to agent**.

The agent now sees ``salesforce_opportunity_create`` and calls it when a request needs it.

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
   * - ``name``
     - text
     - Yes
     - The deal's name. Example: Acme Energy - 500 licences.
   * - ``stageName``
     - text
     - Yes
     - A stage from the org's sales process, for example Prospecting, Proposal/Price Quote or Closed Won.
   * - ``closeDate``
     - text
     - Yes
     - The expected close date as YYYY-MM-DD. Example: 2026-12-15.
   * - ``accountId``
     - text
     - No
     - The Id of the account the deal is with, starting 001; List accounts returns it. Example: 001XX000003DHPh.
   * - ``amount``
     - number
     - No
     - The deal value as a number, in the org's currency. Example: 48000.
   * - ``probability``
     - number
     - No
     - The chance of winning from 0 to 100; blank takes the stage's default. Example: 60.
   * - ``type``
     - text
     - No
     - The opportunity type, for example New Business or Existing Business.
   * - ``leadSource``
     - text
     - No
     - Where the deal came from, for example Web or Partner Referral.
   * - ``nextStep``
     - text
     - No
     - The next action planned on the deal. Example: Send the revised quote by Friday.
   * - ``description``
     - text
     - No
     - Free-text notes about the deal. Example: Replaces their legacy SCADA reporting..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create an opportunity** every time a flow reaches it, without the agent deciding, use the :doc:`Create an opportunity App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/opportunity-create>`.

Other Opportunity tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="opportunity-get.html">Get an opportunity</a><a href="opportunity-getmany.html">List opportunities</a><a href="opportunity-update.html">Update an opportunity</a><a href="opportunity-upsert.html">Create or update an opportunity by external id</a><a href="opportunity-delete.html">Delete an opportunity</a><a href="opportunity-describe.html">Describe opportunity fields</a><a href="opportunity-addnote.html">Add a note to an opportunity</a></div>
