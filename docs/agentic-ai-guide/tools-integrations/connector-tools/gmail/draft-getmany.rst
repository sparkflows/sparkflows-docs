:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Draft</p>

List drafts
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Draft</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_draft_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the drafts in the mailbox as readable rows: the draft id, messageId, to, cc, subject, snippet and body text. The draft id is what Draft get, Draft send and Draft delete take.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Draft** row, then click **Add to agent**.

The agent now sees ``gmail_draft_getmany`` and calls it when a request needs it.

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
   * - ``search``
     - text
     - No
     - Only drafts matching this Gmail search, for example to:asha@example.com or subject:invoice.
   * - ``fields``
     - list of text
     - No
     - Columns to keep: id, messageId, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments, message-id; blank keeps them all. Example: from,subject,received,snippet.
   * - ``limit``
     - whole number
     - No
     - How many drafts at most. Default: 10.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Need it on every run?
---------------------

To run **List drafts** every time a flow reaches it, without the agent deciding, use the :doc:`List drafts App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/draft-getmany>`.

Other Draft tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="draft-get.html">Get a draft</a><a href="draft-create.html">Create a draft</a><a href="draft-send.html">Send a draft</a><a href="draft-delete.html">Delete a draft</a></div>
