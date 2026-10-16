:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../jira-cloud.html">Jira</a> › Comment</p>

Edit a comment
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Jira</dd></div>
     <div><dt>Resource</dt><dd>Comment</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Replaces the text of an existing comment and returns the updated comment.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Jira**.
#. **Action:** under **Comment**, choose **Edit a comment**.
#. **Details:** choose your Jira connection, click **Test**, then fill in the boxes below.
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
   * - **Comment or board id**
     - No
     - The id of the comment to act on, or the board a sprint list belongs to. A status change takes its transition id in Fields to set, as transition. For example ``10042 (a comment id or a board id)``.
   * - **Issue key**
     - No
     - The issue key, for example FIN-12 (or the attachment id, project key or sprint id where the operation names one).

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

Fields to set
-------------

Each row that arrives is written to Jira. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Comment**
     - ``body``
     - ``Reproduced on staging; the fix is in review.``

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
     - The id Jira gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Edit a comment** only when a request needs it, add the :doc:`Edit a comment tool </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud/comment-update>` to an Agent Node.

Other Comment actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="comment-get.html">Get a comment</a><a href="comment-getmany.html">List comments on an issue</a><a href="comment-create.html">Add a comment</a><a href="comment-delete.html">Delete a comment</a></div>
