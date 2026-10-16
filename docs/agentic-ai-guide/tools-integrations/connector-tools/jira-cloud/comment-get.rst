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
     <div><dt>Tool name</dt><dd><code>jira_cloud_comment_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one comment on an issue by its id and returns its author, body (in Atlassian Document Format) and created and updated times. Comment getMany lists every comment on an issue with the ids this needs.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **get** in the **Comment** row, then click **Add to agent**.

The agent now sees ``jira_cloud_comment_get`` and calls it when a request needs it.

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
   * - ``issueKey``
     - text
     - Yes
     - The issue key, for example FIN-12.
   * - ``commentId``
     - text
     - Yes
     - The id of the comment, from Comment getMany. Example: 10042.
   * - ``expand``
     - text
     - No
     - renderedBody adds the comment's body as HTML beside the Atlassian Document Format one.

Need it on every run?
---------------------

To run **Get a comment** every time a flow reaches it, without the agent deciding, use the :doc:`Get a comment App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/comment-get>`.

Other Comment tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="comment-getmany.html">List comments on an issue</a><a href="comment-create.html">Add a comment</a><a href="comment-update.html">Edit a comment</a><a href="comment-delete.html">Delete a comment</a></div>
