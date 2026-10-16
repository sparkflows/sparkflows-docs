:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Get a contact
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_contact_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one contact by its Salesforce Id and returns all of its fields, custom fields included. Use it when the Id is known; to find contacts by name or another value use List contacts.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **get** in the **Contact** row, then click **Add to agent**.

The agent now sees ``salesforce_contact_get`` and calls it when a request needs it.

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
   * - ``contactId``
     - text
     - Yes
     - The contact's Salesforce Id, 15 or 18 characters starting 003, for example 003XX000004TmiQ; List contacts returns it.

Need it on every run?
---------------------

To run **Get a contact** every time a flow reaches it, without the agent deciding, use the :doc:`Get a contact App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/contact-get>`.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
