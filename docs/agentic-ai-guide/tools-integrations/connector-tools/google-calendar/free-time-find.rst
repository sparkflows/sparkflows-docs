:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Free Time</p>

Find busy times
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Free Time</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_calendar_free_time_find</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the busy intervals of one or more calendars between timeMin and timeMax, so the free slots are the gaps between them. Use it to find a meeting time; it returns no event details.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **find** in the **Free Time** row, then click **Add to agent**.

The agent now sees ``google_calendar_free_time_find`` and calls it when a request needs it.

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
   * - ``timeMin``
     - text
     - Yes
     - Start of the window, as ISO 8601 with a zone offset, for example 2026-10-01T09:00:00+05:30; resolve words such as Monday to dates first.
   * - ``timeMax``
     - text
     - Yes
     - End of the window, in the same format as timeMin. Example: 2026-10-01T18:00:00+05:30.
   * - ``calendarId``
     - text
     - No
     - The one calendar to check when calendars is blank, such as asha@company.com; blank means the primary calendar.
   * - ``calendars``
     - list of JSON object
     - No
     - Several calendars or people to check at once, as [{"id": "asha@company.com"}, {"id": "primary"}]; it replaces calendarId. Example: [{"id": "asha@company.com"}, {"id": "vikram@company.com"}].
   * - ``timeZone``
     - text
     - No
     - The IANA time zone for the busy times returned, for example Asia/Kolkata; blank returns UTC.

Need it on every run?
---------------------

To run **Find busy times** every time a flow reaches it, without the agent deciding, use the :doc:`Find busy times App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/free-time-find>`.
