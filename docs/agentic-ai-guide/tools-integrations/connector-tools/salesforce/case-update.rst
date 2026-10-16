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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_case_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing case and leaves the others as they are; returns the case's Id. The case is named by its Salesforce Id, which List cases returns.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **update** in the **Case** row, then click **Add to agent**.

The agent now sees ``salesforce_case_update`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``caseId``
     - text
     - Yes
     - The Salesforce Id of the case to change, starting 500, for example 500XX000001AbCd; List cases returns it.
   * - ``subject``
     - text
     - No
     - A one-line summary of the issue. Example: Invoice portal shows the wrong balance.
   * - ``description``
     - text
     - No
     - The full details of the issue. Example: Since 28 Sep the portal shows last month's balance on every invoice..
   * - ``status``
     - text
     - No
     - The case status from the org's picklist, for example New, Working or Escalated.
   * - ``priority``
     - text
     - No
     - The priority from the org's picklist, for example High, Medium or Low.
   * - ``type``
     - text
     - No
     - The case type, for example Problem, Question or Feature Request.
   * - ``reason``
     - text
     - No
     - The case reason from the org's picklist, for example Performance or Installation.
   * - ``ownerId``
     - text
     - No
     - The Id of the user or queue that owns the case; a user Id starts 005 and a queue Id 00G. Example: 00GXX000000QcRs.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Update a case** every time a flow reaches it, without the agent deciding, use the :doc:`Update a case App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/case-update>`.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-getmany.html">List cases</a><a href="case-create.html">Create a case</a><a href="case-delete.html">Delete a case</a><a href="case-describe.html">Describe case fields</a><a href="case-addcomment.html">Add a case comment</a></div>
