:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Get a contact
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one contact by its Salesforce Id and returns all of its fields, custom fields included.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Contact**, choose **Get a contact**.
#. **Details:** choose your Salesforce connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Salesforce** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Record Id**
     - No
     - The Salesforce Id of the record, for example 001XX000003DHPh. For example ``001XX000003DHPh``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Salesforce** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **Get a contact** only when a request needs it, add the :doc:`Get a contact tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/contact-get>` to an Agent Node.

Other Contact actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
