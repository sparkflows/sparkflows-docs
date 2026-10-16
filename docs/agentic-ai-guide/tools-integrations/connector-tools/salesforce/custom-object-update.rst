:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Custom Object</p>

Update a custom object record
=============================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Custom Object</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing record of the custom object and leaves the others as they are; returns the record's Id. The record's Id goes inside fields, next to the values to change.

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
   * - ``objectApiName``
     - Custom object
     - text
     - Yes
     - The custom object's API name, ending in \_\_c, for example Invoice\_\_c.
   * - ``fields``
     - Id and fields
     - JSON object
     - Yes
     - The record's Id plus the fields to change, for example {"Id": "a01XX000003GhIj", "Status\_\_c": "Paid"}; the Id must be inside this object.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Custom Object** row. The model sees it as ``salesforce_custom_object_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update a custom object record**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Custom Object tools
-------------------------

.. raw:: html

   <div class="tool-related"><a href="custom-object-get.html">Get a custom object record</a><a href="custom-object-getmany.html">List custom object records</a><a href="custom-object-create.html">Create a custom object record</a><a href="custom-object-upsert.html">Create or update a custom object record by external id</a><a href="custom-object-delete.html">Delete a custom object record</a><a href="custom-object-describe.html">Describe custom object fields</a><a href="custom-object-count.html">Count custom object records</a></div>
