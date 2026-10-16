:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Search</p>

Run a SOQL query
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs any SOQL statement and returns every matching row, following Salesforce's paging, with relationship fields nested.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Search**, choose **Run a SOQL query**.
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
   * - **SOQL query**
     - No
     - The full SOQL statement to run, for example SELECT Id, Name FROM Account WHERE Industry = 'Energy'. For example ``SELECT Id, Name FROM Account WHERE Industry = 'Energy'``.

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

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Salesforce with this action and start the flow when something new turns up. Pick **Salesforce** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Case comment added**
     - Reports each comment added to a case since the last check, with the case number, the text and whether the comment is public.
   * - **Campaign member added**
     - Reports each lead or contact added to a campaign since the last check, with the campaign name and the member's status.
   * - **Record created (any object)**
     - Filter is the object's API name, for example Invoice\_\_c or Contract. Reports each record of that object created since the last check, with all its fields, at most 200 per check.
   * - **Record updated (any object)**
     - Filter is the object's API name, for example Invoice\_\_c or Contract. Reports each record of that object every time it is changed, with all its fields, at most 200 per check.

Let an agent decide instead
---------------------------

To let an agent call **Run a SOQL query** only when a request needs it, add the :doc:`Run a SOQL query tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/search-soql>` to an Agent Node.
