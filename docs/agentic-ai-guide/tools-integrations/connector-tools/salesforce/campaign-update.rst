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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing campaign and leaves the others as they are; returns the campaign's Id. The campaign is named by its Salesforce Id, which List campaigns returns.

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
   * - ``campaignId``
     - Campaign Id
     - text
     - Yes
     - The Salesforce Id of the campaign to change, starting 701, for example 701XX0000001234; List campaigns returns it.
   * - ``name``
     - Campaign name
     - text
     - No
     - The campaign's name. Example: Energy Transition Webinar 2026.
   * - ``status``
     - Status
     - text
     - No
     - The campaign status, for example Planned, In Progress, Completed or Aborted.
   * - ``startDate``
     - Start date
     - text
     - No
     - The first day as YYYY-MM-DD. Example: 2026-11-04.
   * - ``endDate``
     - End date
     - text
     - No
     - The last day as YYYY-MM-DD. Example: 2026-11-30.
   * - ``isActive``
     - Active
     - true or false
     - No
     - true marks the campaign active.
   * - ``budgetedCost``
     - Budgeted cost
     - number
     - No
     - The planned spend as a number. Example: 15000.
   * - ``description``
     - Description
     - text
     - No
     - Free-text notes about the campaign. Example: Joint webinar with the grid-storage partner..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Campaign** row. The model sees it as ``salesforce_campaign_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update a campaign**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Campaign tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="campaign-get.html">Get a campaign</a><a href="campaign-getmany.html">List campaigns</a><a href="campaign-create.html">Create a campaign</a><a href="campaign-delete.html">Delete a campaign</a></div>
