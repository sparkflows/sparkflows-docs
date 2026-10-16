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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_file_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Commits a new file to a branch and returns the commit and the file's new SHA. The content must be Base64-encoded; to change a file that already exists use File update.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **create** in the **File** row, then click **Add to agent**.

The agent now sees ``github_file_create`` and calls it when a request needs it.

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

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-update.html">Update a file</a><a href="file-delete.html">Delete a file</a></div>
