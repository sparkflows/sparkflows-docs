:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Opportunity</p>

Add a note to an opportunity
============================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Opportunity</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_opportunity_addnote</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Attaches a note (a classic Salesforce Note with a title and body) to the opportunity and returns the note's Id. Use it to record free-text context, such as call notes, on the opportunity.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **addNote** in the **Opportunity** row, then click **Add to agent**.

The agent now sees ``salesforce_opportunity_addnote`` and calls it when a request needs it.

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
   * - ``opportunityId``
     - text
     - Yes
     - The Salesforce Id of the opportunity the note belongs to, starting 006, for example 006XX000002kLmN.
   * - ``body``
     - text
     - Yes
     - The note's text; several lines are fine. Example: Procurement wants the three-year price before 15 Oct..
   * - ``title``
     - text
     - No
     - A short title for the note; blank uses Note. Example: Call with procurement, 30 Sep.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Add a note to an opportunity** every time a flow reaches it, without the agent deciding, use the :doc:`Add a note to an opportunity App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/opportunity-addnote>`.

Other Opportunity tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="opportunity-get.html">Get an opportunity</a><a href="opportunity-getmany.html">List opportunities</a><a href="opportunity-create.html">Create an opportunity</a><a href="opportunity-update.html">Update an opportunity</a><a href="opportunity-upsert.html">Create or update an opportunity by external id</a><a href="opportunity-delete.html">Delete an opportunity</a><a href="opportunity-describe.html">Describe opportunity fields</a></div>
