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
     <div><dt>Tool name</dt><dd><code>gmail_label_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the mailbox's labels with id, name and type (system or user), without any message counts. Use it to find a label id for Message modify or labelIds, then Label get for that label's totals.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Label** row, then click **Add to agent**.

The agent now sees ``gmail_label_getmany`` and calls it when a request needs it.

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
   * - ``limit``
     - whole number
     - No
     - How many labels at most. Default: 100.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Need it on every run?
---------------------

To run **List labels** every time a flow reaches it, without the agent deciding, use the :doc:`List labels App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/label-getmany>`.

Other Label tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="label-get.html">Get a label with counts</a><a href="label-create.html">Create a label</a><a href="label-update.html">Update a label</a><a href="label-delete.html">Delete a label</a></div>
