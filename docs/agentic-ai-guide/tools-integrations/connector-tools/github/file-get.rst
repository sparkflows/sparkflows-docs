:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › File</p>

Get a file
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one file from a repository and returns its name, path, size, SHA and content, which GitHub sends Base64-encoded; a folder path returns the folder's entries instead. The SHA it returns is what File update and File delete need.

Prerequisites
-------------

* **Connection:** GitHub connection. See :doc:`the GitHub prerequisites <../github>`.

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
   * - ``ref``
     - text
     - No
     - The branch, tag or commit to read from; blank is the default branch. Example: main.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **get** in the **File** row. The model sees it as ``github_file_get``.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-create.html">Create a file</a><a href="file-update.html">Update a file</a><a href="file-delete.html">Delete a file</a></div>
