:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Create a lead
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a lead (a prospect not yet qualified) from the given fields and returns its new Id. It needs lastName and company; Convert a lead later turns it into an account, a contact and an opportunity.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_create`` and calls it when a request needs it.

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
   * - ``lastName``
     - text
     - Yes
     - The lead's last name. Example: Mehta.
   * - ``company``
     - text
     - Yes
     - The company the lead works for. Example: Brightline Solar.
   * - ``firstName``
     - text
     - No
     - The lead's first name. Example: Vikram.
   * - ``email``
     - text
     - No
     - The lead's email address. Example: vikram.mehta@brightline-solar.example.com.
   * - ``phone``
     - text
     - No
     - The lead's phone number. Example: +91 22 4012 5566.
   * - ``title``
     - text
     - No
     - The lead's job title. Example: Operations Manager.
   * - ``status``
     - text
     - No
     - A lead status from the org's picklist, for example Open - Not Contacted or Working - Contacted.
   * - ``leadSource``
     - text
     - No
     - Where the lead came from, for example Web, Phone Inquiry or Partner Referral.
   * - ``industry``
     - text
     - No
     - The lead's industry picklist value, for example Energy.
   * - ``description``
     - text
     - No
     - Free-text notes about the lead. Example: Asked for a demo of the monitoring add-on..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create a lead** every time a flow reaches it, without the agent deciding, use the :doc:`Create a lead App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-create>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-update.html">Update a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a><a href="lead-convert.html">Convert a lead</a></div>
