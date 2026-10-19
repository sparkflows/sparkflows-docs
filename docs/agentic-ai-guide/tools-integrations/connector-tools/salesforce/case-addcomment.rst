:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

Add a case comment
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_case_addcomment</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds a comment to the case's Case Comments and returns the comment's Id. Use it for working notes on a case; the comment stays internal unless publishToCustomer is true.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **addComment** in the **Case** row, then click **Add to agent**.

The agent now sees ``salesforce_case_addcomment`` and calls it when a request needs it.

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
     - The Salesforce Id of the case, starting 500, for example 500XX000001AbCd; List cases returns it.
   * - ``comment``
     - text
     - Yes
     - The comment's text; several lines are fine. Example: Customer confirmed the fix works on their side..
   * - ``publishToCustomer``
     - true or false
     - No
     - true publishes the comment where the customer sees the case, such as a portal or community; blank keeps it internal. Example: false.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Add a case comment** every time a flow reaches it, without the agent deciding, use the :doc:`Add a case comment App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/case-addcomment>`.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-getmany.html">List cases</a><a href="case-create.html">Create a case</a><a href="case-update.html">Update a case</a><a href="case-delete.html">Delete a case</a><a href="case-describe.html">Describe case fields</a></div>
