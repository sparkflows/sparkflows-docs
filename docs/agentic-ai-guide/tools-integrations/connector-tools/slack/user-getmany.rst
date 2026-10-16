:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › User</p>

List users
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_user_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the workspace's members, bots and deactivated accounts included (deleted is true), with id, name, real\_name, profile and tz. To find one person by email use User lookupByEmail instead.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **list** in the **User** row, then click **Add to agent**.

The agent now sees ``slack_user_getmany`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: id,real\_name,profile.email.
   * - ``limit``
     - whole number
     - No
     - How many members at most. Default: 50.

Need it on every run?
---------------------

To run **List users** every time a flow reaches it, without the agent deciding, use the :doc:`List users App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/user-getmany>`.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-get.html">Get a user</a><a href="user-getprofile.html">Get a user&#x27;s profile</a><a href="user-getstatus.html">Get a user&#x27;s presence</a><a href="user-lookupbyemail.html">Find a user by email</a></div>
