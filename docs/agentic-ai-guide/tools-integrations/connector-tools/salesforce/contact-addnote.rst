:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Contact</p>

Add a note to a contact
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Contact</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_contact_addnote</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Attaches a note (a classic Salesforce Note with a title and body) to the contact and returns the note's Id. Use it to record free-text context, such as call notes, on the contact.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **addNote** in the **Contact** row, then click **Add to agent**.

The agent now sees ``salesforce_contact_addnote`` and calls it when a request needs it.

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
   * - ``contactId``
     - text
     - Yes
     - The Salesforce Id of the contact the note belongs to, starting 003, for example 003XX000004TmiQ.
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

To run **Add a note to a contact** every time a flow reaches it, without the agent deciding, use the :doc:`Add a note to a contact App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/contact-addnote>`.

Other Contact tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="contact-get.html">Get a contact</a><a href="contact-getmany.html">List contacts</a><a href="contact-create.html">Create a contact</a><a href="contact-update.html">Update a contact</a><a href="contact-upsert.html">Create or update a contact by external id</a><a href="contact-delete.html">Delete a contact</a><a href="contact-describe.html">Describe contact fields</a><a href="contact-addtocampaign.html">Add a contact to a campaign</a></div>
