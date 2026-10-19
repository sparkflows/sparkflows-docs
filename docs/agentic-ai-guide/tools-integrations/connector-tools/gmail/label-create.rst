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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_label_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a user label and returns it with its id (Label\_...). A slash in the name nests it under another label, for example Clients/Acme.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.
* The account behind the connection must be allowed to change this data in Gmail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **create** in the **Label** row, then click **Add to agent**.

The agent now sees ``gmail_label_create`` and calls it when a request needs it.

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
   * - ``name``
     - text
     - Yes
     - The label name; a slash nests it, for example Clients/Acme.
   * - ``labelListVisibility``
     - text
     - No
     - labelShow shows it in the label list, labelShowIfUnread only while it has unread mail, labelHide hides it. One of: labelShow, labelShowIfUnread, labelHide.
   * - ``messageListVisibility``
     - text
     - No
     - show or hide the label on messages in the message list. One of: show, hide.
   * - ``backgroundColor``
     - text
     - No
     - A background color from Gmail's label palette, for example #16a766; give textColor with it.
   * - ``textColor``
     - text
     - No
     - A text color from Gmail's label palette, for example #ffffff; give backgroundColor with it.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Gmail.

Need it on every run?
---------------------

To run **Create a label** every time a flow reaches it, without the agent deciding, use the :doc:`Create a label App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/label-create>`.

Other Label tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="label-getmany.html">List labels</a><a href="label-get.html">Get a label with counts</a><a href="label-update.html">Update a label</a><a href="label-delete.html">Delete a label</a></div>
