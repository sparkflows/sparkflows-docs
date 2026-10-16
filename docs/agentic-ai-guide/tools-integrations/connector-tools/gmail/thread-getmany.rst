:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Thread</p>

List threads
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Thread</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_thread_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists conversation threads, newest first, with each thread's id and a snippet of its latest message. Call Thread get on an id to read its messages; search narrows the list with Gmail's search syntax.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Thread** row, then click **Add to agent**.

The agent now sees ``gmail_thread_getmany`` and calls it when a request needs it.

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
     - Only threads matching this Gmail search, for example subject:invoice newer\_than:30d.
   * - ``labelIds``
     - list of text
     - No
     - Only threads that carry all of these label ids, for example ["INBOX"].
   * - ``limit``
     - whole number
     - No
     - How many threads at most. Default: 50.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Need it on every run?
---------------------

To run **List threads** every time a flow reaches it, without the agent deciding, use the :doc:`List threads App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/thread-getmany>`.

Other Thread tools
------------------

.. raw:: html

   <div class="tool-related"><a href="thread-get.html">Get a thread</a><a href="thread-trash.html">Move a thread to trash</a></div>
