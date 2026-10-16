:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Free Time</p>

Find meeting times
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Free Time</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_free_time_find</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Suggests meeting times when the organizer and the attendees are free, one row per suggestion with its time, a confidence score and who is available; when nothing fits, one row gives Graph's emptySuggestionsReason. Microsoft Graph serves this only to a connection signed in as a user, not to an app-only connection.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **find** in the **Free Time** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_free_time_find`` and calls it when a request needs it.

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
   * - ``mailbox``
     - text
     - Yes
     - The organizer's address; the organizer's own calendar is checked too. Example: asha.rao@contoso.com.
   * - ``attendees``
     - list of JSON object
     - No
     - The people to meet, as Graph attendee objects with an emailAddress and a type of required or optional. Example: [{"emailAddress": {"address": "ravi.menon@contoso.com"}, "type": "required"}].
   * - ``meetingDuration``
     - text
     - No
     - How long the meeting lasts, as an ISO 8601 duration such as PT30M or PT1H; blank means 30 minutes.
   * - ``timeSlots``
     - list of JSON object
     - No
     - The periods to search, each a start and an end with a dateTime and a timeZone; blank lets Outlook search the coming working days. Example: [{"start": {"dateTime": "2026-10-05T09:00:00", "timeZone": "UTC"}, "end": {"dateTime": "2026-10-05T17:00:00", "timeZone": "UTC"}}].
   * - ``activityDomain``
     - text
     - No
     - Which hours count: work (working hours, the default), personal or unrestricted. One of: work, personal, unrestricted.
   * - ``maxCandidates``
     - whole number
     - No
     - How many suggestions at most. Example: 5.
   * - ``isOrganizerOptional``
     - true or false
     - No
     - true lets suggestions ignore the organizer's own availability.

Need it on every run?
---------------------

To run **Find meeting times** every time a flow reaches it, without the agent deciding, use the :doc:`Find meeting times App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/free-time-find>`.

Other Free Time tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="free-time-schedule.html">Get free/busy schedules</a></div>
