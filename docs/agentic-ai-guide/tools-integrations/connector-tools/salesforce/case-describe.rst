:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Case</p>

Describe case fields
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Case</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_case_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the Case object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the org's exact field names, custom \_\_c fields included, before a create, update or query.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **Case** row, then click **Add to agent**.

The agent now sees ``salesforce_case_describe`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **Describe case fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe case fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/case-describe>`.

Other Case tools
----------------

.. raw:: html

   <div class="tool-related"><a href="case-get.html">Get a case</a><a href="case-getmany.html">List cases</a><a href="case-create.html">Create a case</a><a href="case-update.html">Update a case</a><a href="case-delete.html">Delete a case</a><a href="case-addcomment.html">Add a case comment</a></div>
