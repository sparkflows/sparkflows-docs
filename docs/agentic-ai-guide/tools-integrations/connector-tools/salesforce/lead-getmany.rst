:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

List leads
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries leads with an optional SOQL condition and returns up to limit rows. Only standard fields come back unless fields names them, so list custom (\_\_c) and relationship fields such as Owner.Name explicitly. Use Run a SOQL query for aggregates, subqueries or several objects at once.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **list** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_getmany`` and calls it when a request needs it.

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
   * - ``where``
     - text
     - No
     - A SOQL condition without the word WHERE, such as Status = 'Open - Not Contacted' AND CreatedDate = LAST\_N\_DAYS:7, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every lead up to the limit.
   * - ``fields``
     - list of text
     - No
     - Field API names to return, such as ["Id", "Name", "Company", "Status", "Email"]; blank returns the standard fields only.
   * - ``limit``
     - whole number
     - No
     - How many leads at most. Example: 50. Default: 50.

Need it on every run?
---------------------

To run **List leads** every time a flow reaches it, without the agent deciding, use the :doc:`List leads App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-getmany>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-create.html">Create a lead</a><a href="lead-update.html">Update a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-describe.html">Describe lead fields</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a><a href="lead-convert.html">Convert a lead</a></div>
