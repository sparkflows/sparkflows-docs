:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Opportunity</p>

List opportunities
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Opportunity</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries opportunities with an optional SOQL condition and returns up to limit rows.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Opportunity**, choose **List opportunities**.
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
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

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
   * - **Opportunity created**
     - Reports each opportunity created since the last check, with its standard fields.
   * - **Opportunity updated**
     - Reports each opportunity every time it is changed, with its standard fields.
   * - **Opportunity stage changed**
     - Reports each opportunity whose stage changed since the last check, with the new stage in StageName.
   * - **Opportunity closed won**
     - Reports each opportunity moved to a won stage since the last check.
   * - **Opportunity closed lost**
     - Reports each opportunity moved to a lost stage since the last check.
   * - **Opportunity starts matching a condition**
     - Filter is a SOQL condition without WHERE, for example Amount > 100000 AND IsClosed = false. The first check records the opportunities that already match; later checks report each one that newly matches. Best for conditions that fewer than 500 opportunities meet.

Let an agent decide instead
---------------------------

To let an agent call **List opportunities** only when a request needs it, add the :doc:`List opportunities tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/opportunity-getmany>` to an Agent Node.

Other Opportunity actions
-------------------------

.. raw:: html

   <div class="tool-related"><a href="opportunity-get.html">Get an opportunity</a><a href="opportunity-create.html">Create an opportunity</a><a href="opportunity-update.html">Update an opportunity</a><a href="opportunity-upsert.html">Create or update an opportunity by external id</a><a href="opportunity-delete.html">Delete an opportunity</a><a href="opportunity-describe.html">Describe opportunity fields</a><a href="opportunity-addnote.html">Add a note to an opportunity</a></div>
