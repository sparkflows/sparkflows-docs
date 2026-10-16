:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Draft</p>

Delete a draft
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Draft</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_draft_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a draft immediately and permanently; it does not go to the Trash. The draft id comes from Draft getMany.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.
* The account behind the connection must be allowed to change this data in Gmail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **delete** in the **Draft** row, then click **Add to agent**.

The agent now sees ``gmail_draft_delete`` and calls it when a request needs it.

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
   * - ``draftId``
     - text
     - Yes
     - The draft id, from Draft getMany or Draft create. Example: r-5843521846237418962.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Gmail.

Need it on every run?
---------------------

To run **Delete a draft** every time a flow reaches it, without the agent deciding, use the :doc:`Delete a draft App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/draft-delete>`.

Other Draft tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="draft-getmany.html">List drafts</a><a href="draft-get.html">Get a draft</a><a href="draft-create.html">Create a draft</a><a href="draft-send.html">Send a draft</a></div>
