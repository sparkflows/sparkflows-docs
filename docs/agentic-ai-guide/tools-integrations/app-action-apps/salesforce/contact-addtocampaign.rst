:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Add a contact to a campaign
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds the contact to a campaign as a campaign member and returns the member's Id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Contact**, choose **Add a contact to a campaign**.
#. **Details:** choose your Salesforce connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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
   * - **Campaign or Flow**
     - No
     - The campaign Id to add to, or the API name of the flow to invoke. For example ``701XX0000001234 (a campaign) or My_Flow``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **If a row is rejected**
     - No
     - What happens when a row cannot be written.

       * ``stop`` (default): The run stops at the first row that fails.
       * ``continue``: The other rows are still written. The failed row is marked ``failed`` in ``result_status``, with the reason in ``result_error``.

Fields to set
-------------

Each row that arrives is written to Salesforce. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Contact Id**
     - ``ContactId``
     - ``003XX000004TmiQ``
   * - **Member status**
     - ``MemberStatus``
     - ``Responded``

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Salesforce gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Add a contact to a campaign** only when a request needs it, add the :doc:`Add a contact to a campaign tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/contact-addtocampaign>` to an Agent Node.

Other Contact actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addnote.html">Add a note to a contact</a></div>
