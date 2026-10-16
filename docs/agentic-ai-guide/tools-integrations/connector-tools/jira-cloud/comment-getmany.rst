:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Comment</p>

List comments on an issue
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Comment</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the comments on an issue, oldest first unless ordered otherwise, each with its id, author, body (in Atlassian Document Format) and created and updated times. Use it to read a discussion or to find the comment id that Comment update and Comment delete need.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.

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
   * - ``issueKey``
     - Issue key
     - text
     - Yes
     - The issue key, for example FIN-12.
   * - ``orderBy``
     - Order
     - text
     - No
     - created lists the oldest comment first, -created the newest first. One of: created, -created.
   * - ``maxResults``
     - Comments
     - whole number
     - No
     - How many comments at most; with order -created, the latest ones. Example: 20.
   * - ``expand``
     - Expand
     - text
     - No
     - renderedBody adds each comment's body as HTML beside the Atlassian Document Format one.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **list** in the **Comment** row. The model sees it as ``jira_cloud_comment_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **List comments on an issue**, and fill in the inputs above. It runs every time the flow reaches it.

Other Comment tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="comment-get.html">Get a comment</a><a href="comment-create.html">Add a comment</a><a href="comment-update.html">Edit a comment</a><a href="comment-delete.html">Delete a comment</a></div>
