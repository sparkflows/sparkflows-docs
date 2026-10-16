:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

Get a case
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_case_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one case by its Salesforce Id and returns all of its fields, custom fields included. Use it when the Id is known; to find cases by name or another value use List cases.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **get** in the **Case** row, then click **Add to agent**.

The agent now sees ``salesforce_case_get`` and calls it when a request needs it.

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
     - The case's Salesforce Id, 15 or 18 characters starting 500, for example 500XX000001AbCd; List cases returns it.

Need it on every run?
---------------------

To run **Get a case** every time a flow reaches it, without the agent deciding, use the :doc:`Get a case App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/case-get>`.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-getmany.html">List cases</a><a href="case-create.html">Create a case</a><a href="case-update.html">Update a case</a><a href="case-delete.html">Delete a case</a><a href="case-describe.html">Describe case fields</a><a href="case-addcomment.html">Add a case comment</a></div>
