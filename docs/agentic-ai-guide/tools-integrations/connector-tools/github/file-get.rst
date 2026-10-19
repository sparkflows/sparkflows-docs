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
     <div><dt>Tool name</dt><dd><code>github_file_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one file from a repository and returns its name, path, size, SHA and content, which GitHub sends Base64-encoded; a folder path returns the folder's entries instead. The SHA it returns is what File update and File delete need.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **get** in the **File** row, then click **Add to agent**.

The agent now sees ``github_file_get`` and calls it when a request needs it.

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

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-create.html">Create a file</a><a href="file-update.html">Update a file</a><a href="file-delete.html">Delete a file</a></div>
