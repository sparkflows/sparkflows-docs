:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Campaign</p>

Get a campaign
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Campaign</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one campaign by its Salesforce Id and returns all of its fields, custom fields included. Use it when the Id is known; to find campaigns by name or another value use List campaigns.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.

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
     - The campaign's Salesforce Id, 15 or 18 characters starting 701, for example 701XX0000001234; List campaigns returns it.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **get** in the **Campaign** row. The model sees it as ``salesforce_campaign_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Get a campaign**, and fill in the inputs above. It runs every time the flow reaches it.

Other Campaign tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="campaign-getmany.html">List campaigns</a><a href="campaign-create.html">Create a campaign</a><a href="campaign-update.html">Update a campaign</a><a href="campaign-delete.html">Delete a campaign</a></div>
