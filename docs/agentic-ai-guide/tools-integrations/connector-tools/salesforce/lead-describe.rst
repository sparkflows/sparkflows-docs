:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Lead</p>

Describe lead fields
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Lead</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_lead_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the Lead object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the org's exact field names, custom \_\_c fields included, before a create, update or query.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **Lead** row, then click **Add to agent**.

The agent now sees ``salesforce_lead_describe`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **Describe lead fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe lead fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/lead-describe>`.

Other Lead tools
----------------

.. raw:: html

   <div class="tool-related"><a href="lead-get.html">Get a lead</a><a href="lead-getmany.html">List leads</a><a href="lead-create.html">Create a lead</a><a href="lead-update.html">Update a lead</a><a href="lead-upsert.html">Create or update a lead by external id</a><a href="lead-delete.html">Delete a lead</a><a href="lead-addnote.html">Add a note to a lead</a><a href="lead-addtocampaign.html">Add a lead to a campaign</a><a href="lead-convert.html">Convert a lead</a></div>
