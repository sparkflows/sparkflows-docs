:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Create a contact
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_contact_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a contact (a person, usually at an account) from the given fields and returns its new Id. It needs lastName; link the contact to its company with accountId.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Contact** row, then click **Add to agent**.

The agent now sees ``salesforce_contact_create`` and calls it when a request needs it.

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
     - The contact's last name. Example: Rao.
   * - ``firstName``
     - text
     - No
     - The contact's first name. Example: Asha.
   * - ``email``
     - text
     - No
     - The contact's email address. Example: asha.rao@acme-energy.example.com.
   * - ``phone``
     - text
     - No
     - The contact's work phone number. Example: +91 20 6605 1234.
   * - ``mobilePhone``
     - text
     - No
     - The contact's mobile number. Example: +91 98220 12345.
   * - ``title``
     - text
     - No
     - The contact's job title. Example: Head of Procurement.
   * - ``accountId``
     - text
     - No
     - The Id of the account the contact belongs to, starting 001; List accounts returns it. Example: 001XX000003DHPh.
   * - ``department``
     - text
     - No
     - The contact's department. Example: Procurement.
   * - ``mailingCity``
     - text
     - No
     - The city of the mailing address. Example: Pune.
   * - ``mailingCountry``
     - text
     - No
     - The country of the mailing address. Example: India.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create a contact** every time a flow reaches it, without the agent deciding, use the :doc:`Create a contact App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/contact-create>`.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
