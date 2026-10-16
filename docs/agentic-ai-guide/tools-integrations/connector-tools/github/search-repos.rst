:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Search</p>

Search repositories
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>github_search_repos</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches repositories across GitHub by name, description, topic, language or owner and returns each match's full name, description, stars, language and URL. Use Repository getMany for the connection's own repositories.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **repos** in the **Search** row, then click **Add to agent**.

The agent now sees ``github_search_repos`` and calls it when a request needs it.

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
   * - ``query``
     - text
     - Yes
     - Words plus qualifiers, for example payments language:go org:acme or topic:kubernetes stars:>1000. Example: billing language:python org:acme.
   * - ``sort``
     - text
     - No
     - Blank sorts by best match. One of: stars, forks, help-wanted-issues, updated.
   * - ``order``
     - text
     - No
     - Default desc. One of: desc, asc.
   * - ``perPage``
     - whole number
     - No
     - How many rows GitHub returns in the single request this operation makes, at most 100; GitHub's own default is 30. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many repositories at most. Default: 50.

Other Search tools
------------------

.. raw:: html

   <div class="tool-related"><a href="search-code.html">Search code</a><a href="search-issues.html">Search issues and pull requests</a></div>
