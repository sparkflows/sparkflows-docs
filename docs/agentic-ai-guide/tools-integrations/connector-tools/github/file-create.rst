:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › File</p>

Create a file
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Commits a new file to a branch and returns the commit and the file's new SHA. The content must be Base64-encoded; to change a file that already exists use File update.

Prerequisites
-------------

* **Connection:** GitHub connection. See :doc:`the GitHub prerequisites <../github>`.
* The connection's account must be allowed to change this data in GitHub.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``repository``
     - text
     - Yes
     - The repository as owner/name, for example octocat/hello-world.
   * - ``path``
     - text
     - Yes
     - The path from the repository root, for example src/app.py. Example: docs/README.md.
   * - ``message``
     - text
     - Yes
     - The commit message. Example: Add runbook for SSO timeouts.
   * - ``content``
     - text
     - Yes
     - The whole file content, Base64-encoded. Example: IyBSdW5ib29rCg==.
   * - ``branch``
     - text
     - No
     - The branch to commit to; blank is the default branch. Example: main.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **create** in the **File** row. The model sees it as ``github_file_create``. Each call waits for human approval before it changes anything.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-update.html">Update a file</a><a href="file-delete.html">Delete a file</a></div>
