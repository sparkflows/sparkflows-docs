:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Add a contact to a campaign
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_contact_addtocampaign</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds the contact to a campaign as a campaign member and returns the member's Id. The member gets memberStatus when it is given, otherwise the campaign's default status; List campaigns returns campaign Ids.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **addToCampaign** in the **Contact** row, then click **Add to agent**.

The agent now sees ``salesforce_contact_addtocampaign`` and calls it when a request needs it.

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
   * - ``contactId``
     - text
     - Yes
     - The Salesforce Id of the contact to add, starting 003, for example 003XX000004TmiQ; List contacts returns it.
   * - ``memberStatus``
     - text
     - No
     - The member's status in this campaign, one the campaign defines, for example Sent or Responded; blank uses the campaign's default.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Add a contact to a campaign** every time a flow reaches it, without the agent deciding, use the :doc:`Add a contact to a campaign App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/contact-addtocampaign>`.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a></div>
