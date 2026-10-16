:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Comment</p>

Delete a comment
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Comment</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Permanently deletes one comment from an issue. It needs the issue key and the comment's id, which Comment getMany returns.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.
* The connection's account must be allowed to change this data in Jira Cloud.

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

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **delete** in the **Comment** row. The model sees it as ``jira_cloud_comment_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Delete a comment**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Comment tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="comment-get.html">Get a comment</a><a href="comment-getmany.html">List comments on an issue</a><a href="comment-create.html">Add a comment</a><a href="comment-update.html">Edit a comment</a></div>
