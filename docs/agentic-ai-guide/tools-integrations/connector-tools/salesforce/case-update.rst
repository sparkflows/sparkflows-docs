:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

Update a case
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing case and leaves the others as they are; returns the case's Id. The case is named by its Salesforce Id, which List cases returns.

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
     - The Salesforce Id of the case to change, starting 500, for example 500XX000001AbCd; List cases returns it.
   * - ``subject``
     - Subject
     - text
     - No
     - A one-line summary of the issue. Example: Invoice portal shows the wrong balance.
   * - ``description``
     - Description
     - text
     - No
     - The full details of the issue. Example: Since 28 Sep the portal shows last month's balance on every invoice..
   * - ``status``
     - Status
     - text
     - No
     - The case status from the org's picklist, for example New, Working or Escalated.
   * - ``priority``
     - Priority
     - text
     - No
     - The priority from the org's picklist, for example High, Medium or Low.
   * - ``type``
     - Type
     - text
     - No
     - The case type, for example Problem, Question or Feature Request.
   * - ``reason``
     - Reason
     - text
     - No
     - The case reason from the org's picklist, for example Performance or Installation.
   * - ``ownerId``
     - Owner Id
     - text
     - No
     - The Id of the user or queue that owns the case; a user Id starts 005 and a queue Id 00G. Example: 00GXX000000QcRs.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Case** row. The model sees it as ``salesforce_case_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update a case**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-getmany.html">List cases</a><a href="case-create.html">Create a case</a><a href="case-delete.html">Delete a case</a><a href="case-describe.html">Describe case fields</a><a href="case-addcomment.html">Add a case comment</a></div>
