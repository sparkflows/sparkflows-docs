:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

List contacts
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries contacts with an optional SOQL condition and returns up to limit rows. Only standard fields come back unless fields names them, so list custom (\_\_c) and relationship fields such as Account.Name explicitly. Use Run a SOQL query for aggregates, subqueries or several objects at once.

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
   * - ``where``
     - Where
     - text
     - No
     - A SOQL condition without the word WHERE, such as AccountId = '001XX000003DHPh' AND Email != null, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every contact up to the limit.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Field API names to return, such as ["Id", "Name", "Email", "Account.Name"]; blank returns the standard fields only.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many contacts at most. Example: 50. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **list** in the **Contact** row. The model sees it as ``salesforce_contact_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **List contacts**, and fill in the inputs above. It runs every time the flow reaches it.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
