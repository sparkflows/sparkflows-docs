:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › File</p>

List files
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_file_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists files shared in the workspace, newest first, with id, name, title, filetype, size, user, created and permalink; filter by channel, user, type or time. Returns details only, not the file contents.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **list** in the **File** row, then click **Add to agent**.

The agent now sees ``slack_file_getmany`` and calls it when a request needs it.

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
   * - ``channel``
     - text
     - No
     - Only files shared in this channel ID. Example: C0123ABC.
   * - ``user``
     - text
     - No
     - Only files uploaded by this user ID. Example: U0123ABC.
   * - ``types``
     - text
     - No
     - Comma-separated kinds: all, spaces, snippets, images, gdocs, zips, pdfs. Default all. Example: pdfs,images.
   * - ``tsFrom``
     - text
     - No
     - Only files created after this time, in Unix seconds. Example: 1788220800.
   * - ``tsTo``
     - text
     - No
     - Only files created before this time, in Unix seconds. Example: 1790812800.
   * - ``fields``
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: id,name,filetype,permalink.
   * - ``limit``
     - whole number
     - No
     - How many files at most. Default: 50.

Need it on every run?
---------------------

To run **List files** every time a flow reaches it, without the agent deciding, use the :doc:`List files App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/file-getmany>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-delete.html">Delete a file</a></div>
