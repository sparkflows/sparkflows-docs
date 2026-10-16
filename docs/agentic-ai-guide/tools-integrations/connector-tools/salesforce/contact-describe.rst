:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Describe contact fields
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_contact_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the Contact object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the org's exact field names, custom \_\_c fields included, before a create, update or query.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **Contact** row, then click **Add to agent**.

The agent now sees ``salesforce_contact_describe`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **Describe contact fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe contact fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/contact-describe>`.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-addnote.html">Add a note to a contact</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
