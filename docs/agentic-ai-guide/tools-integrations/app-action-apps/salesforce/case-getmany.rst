:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

List cases
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries cases with an optional SOQL condition and returns up to limit rows.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Case**, choose **List cases**.
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
   * - **Where clause**
     - No
     - A filter in SOQL syntax, without the word WHERE. Blank returns everything up to the limit. For example ``Industry = 'Energy' AND AnnualRevenue > 1000000``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the standard fields. For example ``Id, Name, Industry, Owner.Name``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.

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
     - Some records keep a value inside another value, such as a priority inside an issue. This decides how those inner values become columns.

       * ``deep`` (default): Every inner value gets its own column, named with dots, such as ``fields.priority.name``.
       * ``oneLevel``: Only the first level is split. Anything deeper stays in one column as JSON text.
       * ``json``: Each inner value stays whole, in one column of JSON text.

       See the example below the table.

**Nested fields, by example.** Take a record ``{"id": 7, "fields": {"priority": {"name": "High"}}}``. Each choice gives you these columns:

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: tool-table

   * - Choice
     - Columns you get
   * - ``deep``
     - ``id`` = ``7`` and ``fields.priority.name`` = ``High``
   * - ``oneLevel``
     - ``id`` = ``7`` and ``fields.priority`` = ``{"name": "High"}``
   * - ``json``
     - ``id`` = ``7`` and ``fields`` = ``{"priority": {"name": "High"}}``

Keep ``deep`` unless a later step needs the whole inner value as JSON.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Salesforce** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Salesforce with this action and start the flow when something new turns up. Pick **Salesforce** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Case created**
     - Reports each case created since the last check, with its standard fields.
   * - **Case updated**
     - Reports each case every time it is changed, with its standard fields.
   * - **Case created matching a condition**
     - Filter is a SOQL condition without WHERE, for example Priority = 'High' AND Origin = 'Email'. Reports each case created since the last check that meets it.
   * - **Case escalated**
     - Reports each escalated case each time it is changed; a case has no escalation time of its own.
   * - **Case closed**
     - Reports each case closed since the last check, with its status and closed date.

Let an agent decide instead
---------------------------

To let an agent call **List cases** only when a request needs it, add the :doc:`List cases tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/case-getmany>` to an Agent Node.

Other Case actions
------------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-create.html">Create a case</a><a href="case-update.html">Update a case</a><a href="case-delete.html">Delete a case</a><a href="case-describe.html">Describe case fields</a><a href="case-addcomment.html">Add a case comment</a></div>
