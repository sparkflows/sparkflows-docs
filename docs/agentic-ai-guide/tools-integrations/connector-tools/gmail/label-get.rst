:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Label</p>

Get a label with counts
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Label</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one label with exact counts: messagesTotal, messagesUnread, threadsTotal and threadsUnread. Use it to answer how many (unread) emails there are, with INBOX, UNREAD or a user label id; the message lists stop at their limit and are no count.

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
   * - ``labelId``
     - Label
     - text
     - Yes
     - The label id: a system label such as INBOX, UNREAD, SENT, STARRED or SPAM, or a user label id such as Label\_3 from Label getMany.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **get** in the **Label** row. The model sees it as ``gmail_label_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Get a label with counts**, and fill in the inputs above. It runs every time the flow reaches it.

Other Label tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="label-getmany.html">List labels</a><a href="label-create.html">Create a label</a><a href="label-update.html">Update a label</a><a href="label-delete.html">Delete a label</a></div>
