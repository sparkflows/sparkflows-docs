:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › User</p>

Get a user
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_user_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one Salesforce user by Id and returns all of their fields, such as name, email, username, profile and whether they are active. Use List users to find a user's Id from a name or email.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **get** in the **User** row, then click **Add to agent**.

The agent now sees ``salesforce_user_get`` and calls it when a request needs it.

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
     - The user's Salesforce Id, 15 or 18 characters starting 005, for example 005XX000001Sv6e; List users returns it.

Need it on every run?
---------------------

To run **Get a user** every time a flow reaches it, without the agent deciding, use the :doc:`Get a user App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/user-get>`.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-getmany.html">List users</a><a href="user-describe.html">Describe user fields</a></div>
