:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Label</p>

Create a label
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Label</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a user label and returns it with its id (Label\_...). A slash in the name nests it under another label, for example Clients/Acme.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Gmail prerequisites <../gmail>`.
* The connection's account must be allowed to change this data in Gmail.

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
   * - ``name``
     - Name
     - text
     - Yes
     - The label name; a slash nests it, for example Clients/Acme.
   * - ``labelListVisibility``
     - In the label list
     - text
     - No
     - labelShow shows it in the label list, labelShowIfUnread only while it has unread mail, labelHide hides it. One of: labelShow, labelShowIfUnread, labelHide.
   * - ``messageListVisibility``
     - On messages
     - text
     - No
     - show or hide the label on messages in the message list. One of: show, hide.
   * - ``backgroundColor``
     - Background color
     - text
     - No
     - A background color from Gmail's label palette, for example #16a766; give textColor with it.
   * - ``textColor``
     - Text color
     - text
     - No
     - A text color from Gmail's label palette, for example #ffffff; give backgroundColor with it.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **create** in the **Label** row. The model sees it as ``gmail_label_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Create a label**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Label tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="label-getmany.html">List labels</a><a href="label-get.html">Get a label with counts</a><a href="label-update.html">Update a label</a><a href="label-delete.html">Delete a label</a></div>
