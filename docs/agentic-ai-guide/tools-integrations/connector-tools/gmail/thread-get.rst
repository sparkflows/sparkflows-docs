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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns every message of one conversation as readable rows, oldest first: from, to, subject, received, body text, labels and attachment names. The thread id is the threadId of any message row, or comes from Thread getMany.

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
   * - ``threadId``
     - Thread
     - text
     - Yes
     - The thread id: the threadId of a message row, or an id from Thread getMany. Example: 18c3f2a9b7d4e1f0.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments, message-id; blank keeps them all. Example: from,subject,received,snippet.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **get** in the **Thread** row. The model sees it as ``gmail_thread_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Get a thread**, and fill in the inputs above. It runs every time the flow reaches it.

Other Thread tools
------------------

.. raw:: html

   <div class="tool-related"><a href="thread-getmany.html">List threads</a><a href="thread-trash.html">Move a thread to trash</a></div>
