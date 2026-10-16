:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Custom Object</p>

List custom object records
==========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Custom Object</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries records of the custom object with an optional SOQL condition and returns up to limit rows. Without fields only the standard fields (Id, Name, owner and system dates) come back, so name the object's \_\_c fields to get its data. Use Run a SOQL query for aggregates or joins.

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
   * - ``objectApiName``
     - Custom object
     - text
     - Yes
     - The custom object's API name, ending in \_\_c, for example Invoice\_\_c.
   * - ``where``
     - Where
     - text
     - No
     - A SOQL condition without the word WHERE, such as Status\_\_c = 'Open' AND CreatedDate = LAST\_N\_DAYS:30, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every record up to the limit.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Field API names to return, such as ["Id", "Name", "Status\_\_c", "Amount\_\_c"]; blank returns only the standard fields, which leaves out every \_\_c field.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many records at most. Example: 50. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **list** in the **Custom Object** row. The model sees it as ``salesforce_custom_object_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **List custom object records**, and fill in the inputs above. It runs every time the flow reaches it.

Other Custom Object tools
-------------------------

.. raw:: html

   <div class="tool-related"><a href="custom-object-get.html">Get a custom object record</a><a href="custom-object-create.html">Create a custom object record</a><a href="custom-object-update.html">Update a custom object record</a><a href="custom-object-upsert.html">Create or update a custom object record by external id</a><a href="custom-object-delete.html">Delete a custom object record</a><a href="custom-object-describe.html">Describe custom object fields</a><a href="custom-object-count.html">Count custom object records</a></div>
