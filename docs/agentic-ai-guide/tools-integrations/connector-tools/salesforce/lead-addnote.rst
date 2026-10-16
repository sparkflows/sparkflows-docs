:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Add a note to a lead
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_addnote</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Attaches a note (a classic Salesforce Note with a title and body) to the lead and returns the note's Id. Use it to record free-text context, such as call notes, on the lead.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **addNote** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_addnote`` and calls it when a request needs it.

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
   * - ``leadId``
     - text
     - Yes
     - The Salesforce Id of the lead the note belongs to, starting 00Q, for example 00QXX000001Bc3K.
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

To run **Add a note to a lead** every time a flow reaches it, without the agent deciding, use the :doc:`Add a note to a lead App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-addnote>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-create.html">Create a lead</a><a href="lead-update.html">Update a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a><a href="lead-convert.html">Convert a lead</a></div>
