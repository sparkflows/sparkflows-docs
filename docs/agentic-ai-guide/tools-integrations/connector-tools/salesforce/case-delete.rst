:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

Delete a case
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes one case by its Salesforce Id and returns that Id. Salesforce moves it to the Recycle Bin, where it can be restored for 15 days.

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
   * - ``caseId``
     - Case Id
     - text
     - Yes
     - The Salesforce Id of the case to delete, starting 500, for example 500XX000001AbCd; List cases returns it.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **delete** in the **Case** row. The model sees it as ``salesforce_case_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Delete a case**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-getmany.html">List cases</a><a href="case-create.html">Create a case</a><a href="case-update.html">Update a case</a><a href="case-describe.html">Describe case fields</a><a href="case-addcomment.html">Add a case comment</a></div>
