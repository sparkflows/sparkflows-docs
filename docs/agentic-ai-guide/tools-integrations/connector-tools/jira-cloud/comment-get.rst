:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Comment</p>

Get a comment
=============

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

   Fetches one comment on an issue by its id and returns its author, body (in Atlassian Document Format) and created and updated times. Comment getMany lists every comment on an issue with the ids this needs.

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
   * - ``commentId``
     - Comment id
     - text
     - Yes
     - The id of the comment, from Comment getMany. Example: 10042.
   * - ``expand``
     - Expand
     - text
     - No
     - renderedBody adds the comment's body as HTML beside the Atlassian Document Format one.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **get** in the **Comment** row. The model sees it as ``jira_cloud_comment_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Get a comment**, and fill in the inputs above. It runs every time the flow reaches it.

Other Comment tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="comment-getmany.html">List comments on an issue</a><a href="comment-create.html">Add a comment</a><a href="comment-update.html">Edit a comment</a><a href="comment-delete.html">Delete a comment</a></div>
