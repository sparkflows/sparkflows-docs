:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Meeting</p>

Create an online meeting
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Meeting</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_meeting_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a Teams online meeting on behalf of a user and returns its joinWebUrl, id, start and end. The meeting is not put in anyone's calendar, and an app-only connection also needs an application access policy for that user, granted by a Teams admin.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.
* The account behind the connection must be allowed to change this data in Microsoft Teams.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **create** in the **Meeting** row, then click **Add to agent**.

The agent now sees ``msteams_meeting_create`` and calls it when a request needs it.

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
   * - ``subject``
     - text
     - Yes
     - The meeting title. Example: Quarterly review.
   * - ``startDateTime``
     - text
     - No
     - When the meeting starts, with a time zone, for example 2026-10-01T10:00:00Z.
   * - ``endDateTime``
     - text
     - No
     - When the meeting ends, with a time zone, for example 2026-10-01T10:30:00Z.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Microsoft Teams.

Need it on every run?
---------------------

To run **Create an online meeting** every time a flow reaches it, without the agent deciding, use the :doc:`Create an online meeting App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/meeting-create>`.

Other Meeting tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="meeting-get.html">Get an online meeting</a></div>
