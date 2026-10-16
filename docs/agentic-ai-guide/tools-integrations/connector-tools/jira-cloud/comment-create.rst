:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Comment</p>

Add a comment
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Comment</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_comment_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds a comment to an issue and returns it with its id. The text is plain; the connector turns it into Jira's rich-text format. To change a comment that exists use Comment update.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **create** in the **Comment** row, then click **Add to agent**.

The agent now sees ``jira_cloud_comment_create`` and calls it when a request needs it.

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
   * - ``body``
     - text
     - Yes
     - The comment text as plain text; each line becomes a paragraph. Example: Reproduced on staging; the fix is in review..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Add a comment** every time a flow reaches it, without the agent deciding, use the :doc:`Add a comment App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/comment-create>`.

Other Comment tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="comment-get.html">Get a comment</a><a href="comment-getmany.html">List comments on an issue</a><a href="comment-update.html">Edit a comment</a><a href="comment-delete.html">Delete a comment</a></div>
