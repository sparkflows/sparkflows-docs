:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Update a lead
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing lead and leaves the others as they are; returns the lead's Id. The lead is named by its Salesforce Id, which List leads returns.

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
   * - ``leadId``
     - Lead Id
     - text
     - Yes
     - The Salesforce Id of the lead to change, starting 00Q, for example 00QXX000001Bc3K; List leads returns it.
   * - ``firstName``
     - First name
     - text
     - No
     - The lead's first name. Example: Vikram.
   * - ``lastName``
     - Last name
     - text
     - No
     - The lead's last name. Example: Mehta.
   * - ``company``
     - Company
     - text
     - No
     - The company the lead works for. Example: Brightline Solar.
   * - ``email``
     - Email
     - text
     - No
     - The lead's email address. Example: vikram.mehta@brightline-solar.example.com.
   * - ``phone``
     - Phone
     - text
     - No
     - The lead's phone number. Example: +91 22 4012 5566.
   * - ``title``
     - Job title
     - text
     - No
     - The lead's job title. Example: Operations Manager.
   * - ``status``
     - Lead status
     - text
     - No
     - A lead status from the org's picklist, for example Open - Not Contacted or Working - Contacted.
   * - ``leadSource``
     - Lead source
     - text
     - No
     - Where the lead came from, for example Web, Phone Inquiry or Partner Referral.
   * - ``ownerId``
     - Owner Id
     - text
     - No
     - The Id of the user or queue that owns the lead; a user Id starts 005 and a queue Id 00G. Example: 005XX000001Sv6e.
   * - ``description``
     - Description
     - text
     - No
     - Free-text notes about the lead. Example: Asked for a demo of the monitoring add-on..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Lead** row. The model sees it as ``salesforce_lead_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update a lead**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-create.html">Create a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a><a href="lead-convert.html">Convert a lead</a></div>
