:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Opportunity</p>

Update an opportunity
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Opportunity</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing opportunity and leaves the others as they are; returns the opportunity's Id. The opportunity is named by its Salesforce Id, which List opportunities returns.

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
   * - ``opportunityId``
     - Opportunity Id
     - text
     - Yes
     - The Salesforce Id of the opportunity to change, starting 006, for example 006XX000002kLmN; List opportunities returns it.
   * - ``name``
     - Opportunity name
     - text
     - No
     - The deal's name. Example: Acme Energy - 500 licences.
   * - ``stageName``
     - Stage
     - text
     - No
     - A stage from the org's sales process, for example Prospecting, Proposal/Price Quote or Closed Won.
   * - ``closeDate``
     - Close date
     - text
     - No
     - The expected close date as YYYY-MM-DD. Example: 2026-12-15.
   * - ``amount``
     - Amount
     - number
     - No
     - The deal value as a number, in the org's currency. Example: 48000.
   * - ``probability``
     - Probability (%)
     - number
     - No
     - The chance of winning from 0 to 100; blank takes the stage's default. Example: 60.
   * - ``type``
     - Type
     - text
     - No
     - The opportunity type, for example New Business or Existing Business.
   * - ``nextStep``
     - Next step
     - text
     - No
     - The next action planned on the deal. Example: Send the revised quote by Friday.
   * - ``ownerId``
     - Owner Id
     - text
     - No
     - The Id of the user who owns the deal, starting 005; List users returns it. Example: 005XX000001Sv6e.
   * - ``description``
     - Description
     - text
     - No
     - Free-text notes about the deal. Example: Replaces their legacy SCADA reporting..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Opportunity** row. The model sees it as ``salesforce_opportunity_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update an opportunity**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Opportunity tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="opportunity-get.html">Get an opportunity</a><a href="opportunity-getmany.html">List opportunities</a><a href="opportunity-create.html">Create an opportunity</a><a href="opportunity-upsert.html">Create or update an opportunity by external id</a><a href="opportunity-delete.html">Delete an opportunity</a><a href="opportunity-describe.html">Describe opportunity fields</a><a href="opportunity-addnote.html">Add a note to an opportunity</a></div>
