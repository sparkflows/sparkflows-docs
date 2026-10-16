:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › User</p>

Get a user
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_user_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one person or bot by id with their name, type, avatar and, when the integration may read it, email address. Use User getMany to find the id.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **get** in the **User** row, then click **Add to agent**.

The agent now sees ``notion_user_get`` and calls it when a request needs it.

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
   * - ``userId``
     - text
     - Yes
     - The user's id, from User getMany or a people property. Example: 6794760a-1f15-45cd-9c65-0dfe42f5135a.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-getmany.html">List users</a></div>
