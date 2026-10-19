:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../slack.html">Slack</a> › File</p>

Delete a file
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a file from Slack for everyone.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/slack>`.
* The account behind the connection must be allowed to change this data in Slack.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Slack**.
#. **Action:** under **File**, choose **Delete a file**.
#. **Details:** choose your Slack connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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
   * - **Message, user or file id**
     - No
     - The message timestamp (ts) for message operations, the user id for user operations, the file id for file operations. For example ``1712345678.000100 (a message ts) or U0123ABC``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **If a row is rejected**
     - No
     - What happens when a row cannot be written.

       * ``stop`` (default): The run stops at the first row that fails.
       * ``continue``: The other rows are still written. The failed row is marked ``failed`` in ``result_status``, with the reason in ``result_error``.

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Slack gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Delete a file** only when a request needs it, add the :doc:`Delete a file tool </agentic-ai-guide/tools-integrations/connector-tools/slack/file-delete>` to an Agent Node.

Other File actions
------------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a></div>
