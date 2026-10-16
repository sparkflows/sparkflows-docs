:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Label</p>

Delete a label
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Label</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a user label for good and removes it from every message and thread that carries it; the messages themselves stay. System labels cannot be deleted.

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
   * - ``labelId``
     - Label
     - text
     - Yes
     - The user label id, for example Label\_3, from Label getMany.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **delete** in the **Label** row. The model sees it as ``gmail_label_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Delete a label**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Label tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="label-getmany.html">List labels</a><a href="label-get.html">Get a label with counts</a><a href="label-create.html">Create a label</a><a href="label-update.html">Update a label</a></div>
