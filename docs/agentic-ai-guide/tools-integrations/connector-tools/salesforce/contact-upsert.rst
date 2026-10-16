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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a contact, or updates the one whose external id field already holds the same value, so a repeated sync never makes duplicates; returns the external id. Use it for records that another system keys; use Create a contact or Update a contact when there is no external id.

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
   * - ``externalIdField``
     - External id field
     - text
     - Yes
     - The API name of a Contact field marked External ID, for example External\_Id\_\_c; its value goes in fields.
   * - ``fields``
     - Fields
     - JSON object
     - Yes
     - The contact's fields as API name to value, including the external id field with its value and, in case the contact is new, its required fields, for example {"External\_Id\_\_c": "HR-5531", "LastName": "Rao", "Email": "asha.rao@acme-energy.example.com"}.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **upsert** in the **Contact** row. The model sees it as ``salesforce_contact_upsert``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Create or update a contact by external id**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
