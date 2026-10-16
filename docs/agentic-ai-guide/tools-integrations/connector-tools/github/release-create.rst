:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Release</p>

Create a release
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Release</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_release_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a release for a tag and returns it with its id and URL; a tag that does not exist yet is created from targetCommitish. A draft release stays hidden from people without push access.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **create** in the **Release** row, then click **Add to agent**.

The agent now sees ``github_release_create`` and calls it when a request needs it.

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
   * - ``tagName``
     - text
     - Yes
     - The tag of the release, for example v2.4.1.
   * - ``name``
     - text
     - No
     - The release title; blank uses the tag. Example: v2.4.1.
   * - ``body``
     - text
     - No
     - The notes in GitHub Markdown. Example: Fixes the SSO login timeout..
   * - ``targetCommitish``
     - text
     - No
     - The branch or commit SHA the tag is created from when it does not exist; default is the default branch. Example: main.
   * - ``draft``
     - true or false
     - No
     - true saves it as an unpublished draft. Example: false.
   * - ``prerelease``
     - true or false
     - No
     - true marks it as not ready for production. Example: false.
   * - ``generateReleaseNotes``
     - true or false
     - No
     - true has GitHub write the notes from the pull requests merged since the previous release.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other Release tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="release-getmany.html">List releases</a></div>
