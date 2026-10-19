:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Thread</p>

Get a thread
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Thread</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_thread_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns every message of one conversation as readable rows, oldest first: from, to, subject, received, body text, labels and attachment names. The thread id is the threadId of any message row, or comes from Thread getMany.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **get** in the **Thread** row, then click **Add to agent**.

The agent now sees ``gmail_thread_get`` and calls it when a request needs it.

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
   * - ``threadId``
     - text
     - Yes
     - The thread id: the threadId of a message row, or an id from Thread getMany. Example: 18c3f2a9b7d4e1f0.
   * - ``fields``
     - list of text
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments, message-id; blank keeps them all. Example: from,subject,received,snippet.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Need it on every run?
---------------------

To run **Get a thread** every time a flow reaches it, without the agent deciding, use the :doc:`Get a thread App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/thread-get>`.

Other Thread tools
------------------

.. raw:: html

   <div class="tool-related"><a href="thread-getmany.html">List threads</a><a href="thread-trash.html">Move a thread to trash</a></div>
