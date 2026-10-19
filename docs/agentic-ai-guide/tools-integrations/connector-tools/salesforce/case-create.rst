:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

Create a case
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_case_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a case (a customer issue or support request) from the given fields and returns its new Id. Salesforce assigns the case number; link the customer with accountId and contactId.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Case** row, then click **Add to agent**.

The agent now sees ``salesforce_case_create`` and calls it when a request needs it.

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
   * - ``origin``
     - text
     - No
     - How the case came in, for example Phone, Email or Web.
   * - ``type``
     - text
     - No
     - The case type, for example Problem, Question or Feature Request.
   * - ``reason``
     - text
     - No
     - The case reason from the org's picklist, for example Performance or Installation.
   * - ``accountId``
     - text
     - No
     - The Id of the customer's account, starting 001. Example: 001XX000003DHPh.
   * - ``contactId``
     - text
     - No
     - The Id of the contact who raised the case, starting 003. Example: 003XX000004TmiQ.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create a case** every time a flow reaches it, without the agent deciding, use the :doc:`Create a case App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/case-create>`.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-getmany.html">List cases</a><a href="case-update.html">Update a case</a><a href="case-delete.html">Delete a case</a><a href="case-describe.html">Describe case fields</a><a href="case-addcomment.html">Add a case comment</a></div>
