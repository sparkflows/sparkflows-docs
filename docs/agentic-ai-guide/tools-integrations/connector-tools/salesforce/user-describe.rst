:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › User</p>

Describe user fields
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_user_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the User object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn exact field names before querying users.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **User** row, then click **Add to agent**.

The agent now sees ``salesforce_user_describe`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **Describe user fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe user fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/user-describe>`.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-get.html">Get a user</a><a href="user-getmany.html">List users</a></div>
