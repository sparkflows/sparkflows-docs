:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Meeting</p>

Get an online meeting
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Meeting</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_meeting_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one online meeting: subject, startDateTime, endDateTime, joinWebUrl, participants and dial-in details. The meeting id is the one Meeting create returned.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Meeting** row, then click **Add to agent**.

The agent now sees ``msteams_meeting_get`` and calls it when a request needs it.

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
   * - ``organizer``
     - text
     - Yes
     - The organizer's Microsoft Entra user object id (a GUID), which Team members and Channel members return as userId; the meeting belongs to this user. Example: 6e0f2c1a-9b8d-4f3e-a2c1-7d6e5f4a3b2c.
   * - ``meetingId``
     - text
     - Yes
     - The online meeting id returned by Meeting create. Example: MSo1N2Y5ZGFjYy03MWJmLTQ3NDMtYjQxMy01M2EdFGkdRWHJlQ.

Need it on every run?
---------------------

To run **Get an online meeting** every time a flow reaches it, without the agent deciding, use the :doc:`Get an online meeting App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/meeting-get>`.

Other Meeting tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="meeting-create.html">Create an online meeting</a></div>
