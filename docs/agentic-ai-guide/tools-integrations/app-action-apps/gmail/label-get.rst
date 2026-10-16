:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../gmail.html">Gmail</a> › Label</p>

Get a label with counts
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Label</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one label with exact counts: messagesTotal, messagesUnread, threadsTotal and threadsUnread.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/gmail>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Gmail**.
#. **Action:** under **Label**, choose **Get a label with counts**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Gmail** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Mailbox**
     - No
     - Blank means the mailbox the connection belongs to.
   * - **Message, draft, label or thread id**
     - No
     - The id of the item to act on. For attachments, the message id (several comma-separated), or leave it blank and search.
   * - **Fields to return**
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments. Blank keeps them all. For example ``from, subject, received, snippet``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Gmail** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **Get a label with counts** only when a request needs it, add the :doc:`Get a label with counts tool </agentic-ai-guide/tools-integrations/connector-tools/gmail/label-get>` to an Agent Node.

Other Label actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="label-getmany.html">List labels</a><a href="label-create.html">Create a label</a><a href="label-update.html">Update a label</a><a href="label-delete.html">Delete a label</a></div>
