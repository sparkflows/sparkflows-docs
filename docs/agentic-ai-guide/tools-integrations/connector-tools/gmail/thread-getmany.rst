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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists conversation threads, newest first, with each thread's id and a snippet of its latest message. Call Thread get on an id to read its messages; search narrows the list with Gmail's search syntax.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Gmail prerequisites <../gmail>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``search``
     - Search
     - text
     - No
     - Only threads matching this Gmail search, for example subject:invoice newer\_than:30d.
   * - ``labelIds``
     - Labels
     - list of text
     - No
     - Only threads that carry all of these label ids, for example ["INBOX"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many threads at most. Default: 50.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **list** in the **Thread** row. The model sees it as ``gmail_thread_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **List threads**, and fill in the inputs above. It runs every time the flow reaches it.

Other Thread tools
------------------

.. raw:: html

   <div class="tool-related"><a href="thread-get.html">Get a thread</a><a href="thread-trash.html">Move a thread to trash</a></div>
