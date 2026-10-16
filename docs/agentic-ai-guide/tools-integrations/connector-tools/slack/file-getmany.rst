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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists files shared in the workspace, newest first, with id, name, title, filetype, size, user, created and permalink; filter by channel, user, type or time. Returns details only, not the file contents.

Prerequisites
-------------

* **Connection:** Slack connection. See :doc:`the Slack prerequisites <../slack>`.

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
   * - ``channel``
     - Channel
     - text
     - No
     - Only files shared in this channel ID. Example: C0123ABC.
   * - ``user``
     - Uploaded by
     - text
     - No
     - Only files uploaded by this user ID. Example: U0123ABC.
   * - ``types``
     - File types
     - text
     - No
     - Comma-separated kinds: all, spaces, snippets, images, gdocs, zips, pdfs. Default all. Example: pdfs,images.
   * - ``tsFrom``
     - Created after
     - text
     - No
     - Only files created after this time, in Unix seconds. Example: 1788220800.
   * - ``tsTo``
     - Created before
     - text
     - No
     - Only files created before this time, in Unix seconds. Example: 1790812800.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: id,name,filetype,permalink.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many files at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **list** in the **File** row. The model sees it as ``slack_file_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **List files**, and fill in the inputs above. It runs every time the flow reaches it.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-delete.html">Delete a file</a></div>
