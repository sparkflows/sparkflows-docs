:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Label</p>

List labels
===========

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

   Lists the mailbox's labels with id, name and type (system or user), without any message counts. Use it to find a label id for Message modify or labelIds, then Label get for that label's totals.

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
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many labels at most. Default: 100.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **list** in the **Label** row. The model sees it as ``gmail_label_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **List labels**, and fill in the inputs above. It runs every time the flow reaches it.

Other Label tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="label-get.html">Get a label with counts</a><a href="label-create.html">Create a label</a><a href="label-update.html">Update a label</a><a href="label-delete.html">Delete a label</a></div>
