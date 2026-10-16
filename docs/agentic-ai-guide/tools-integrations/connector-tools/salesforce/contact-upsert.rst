:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Create or update a contact by external id
=========================================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_contact_upsert</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a contact, or updates the one whose external id field already holds the same value, so a repeated sync never makes duplicates; returns the external id. Use it for records that another system keys; use Create a contact or Update a contact when there is no external id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **upsert** in the **Contact** row, then click **Add to agent**.

The agent now sees ``salesforce_contact_upsert`` and calls it when a request needs it.

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
   * - ``externalIdField``
     - text
     - Yes
     - The API name of a Contact field marked External ID, for example External\_Id\_\_c; its value goes in fields.
   * - ``fields``
     - JSON object
     - Yes
     - The contact's fields as API name to value, including the external id field with its value and, in case the contact is new, its required fields, for example {"External\_Id\_\_c": "HR-5531", "LastName": "Rao", "Email": "asha.rao@acme-energy.example.com"}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create or update a contact by external id** every time a flow reaches it, without the agent deciding, use the :doc:`Create or update a contact by external id App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/contact-upsert>`.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
