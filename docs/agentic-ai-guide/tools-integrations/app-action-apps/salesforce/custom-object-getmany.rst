:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Custom Object</p>

List custom object records
==========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Custom Object</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries records of the custom object with an optional SOQL condition and returns up to limit rows.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Custom Object**, choose **List custom object records**.
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
   * - **Custom Object API Name**
     - No
     - The API name of the custom object, for example Invoice\_\_c. For example ``Invoice__c``.
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

Let an agent decide instead
---------------------------

To let an agent call **List custom object records** only when a request needs it, add the :doc:`List custom object records tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/custom-object-getmany>` to an Agent Node.

Other Custom Object actions
---------------------------

.. raw:: html

   <div class="tool-related"><a href="custom-object-get.html">Get a custom object record</a><a href="custom-object-create.html">Create a custom object record</a><a href="custom-object-update.html">Update a custom object record</a><a href="custom-object-upsert.html">Create or update a custom object record by external id</a><a href="custom-object-delete.html">Delete a custom object record</a><a href="custom-object-describe.html">Describe custom object fields</a><a href="custom-object-count.html">Count custom object records</a></div>
