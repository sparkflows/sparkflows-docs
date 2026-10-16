:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Update a contact
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing contact and leaves the others as they are; returns the contact's Id. The contact is named by its Salesforce Id, which List contacts returns.

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
   * - ``contactId``
     - Contact Id
     - text
     - Yes
     - The Salesforce Id of the contact to change, starting 003, for example 003XX000004TmiQ; List contacts returns it.
   * - ``firstName``
     - First name
     - text
     - No
     - The contact's first name. Example: Asha.
   * - ``lastName``
     - Last name
     - text
     - No
     - The contact's last name. Example: Rao.
   * - ``email``
     - Email
     - text
     - No
     - The contact's email address. Example: asha.rao@acme-energy.example.com.
   * - ``phone``
     - Phone
     - text
     - No
     - The contact's work phone number. Example: +91 20 6605 1234.
   * - ``mobilePhone``
     - Mobile
     - text
     - No
     - The contact's mobile number. Example: +91 98220 12345.
   * - ``title``
     - Job title
     - text
     - No
     - The contact's job title. Example: Head of Procurement.
   * - ``accountId``
     - Account Id
     - text
     - No
     - The Id of the account the contact belongs to, starting 001; List accounts returns it. Example: 001XX000003DHPh.
   * - ``department``
     - Department
     - text
     - No
     - The contact's department. Example: Procurement.
   * - ``mailingCity``
     - Mailing city
     - text
     - No
     - The city of the mailing address. Example: Pune.
   * - ``ownerId``
     - Owner Id
     - text
     - No
     - The Id of the user who owns the contact, starting 005; List users returns it. Example: 005XX000001Sv6e.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Contact** row. The model sees it as ``salesforce_contact_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update a contact**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
