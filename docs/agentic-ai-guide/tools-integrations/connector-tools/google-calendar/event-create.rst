:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

Create an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_calendar_event_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an event on a calendar and returns it, with its id, link and, when conferenceType asks for one, its Meet link. Give start and end as date-times with a zone offset, or startDate and endDate for an all-day event; guests in attendees are emailed an invitation unless sendUpdates says otherwise.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.
* The account behind the connection must be allowed to change this data in Google Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **create** in the **Event** row, then click **Add to agent**.

The agent now sees ``google_calendar_event_create`` and calls it when a request needs it.

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
   * - ``calendarId``
     - text
     - No
     - The calendar's id: an address such as asha@company.com, a shared calendar's id from List calendars, or primary; blank means the primary calendar.
   * - ``summary``
     - text
     - No
     - The event's title. Example: Quarterly review with Acme.
   * - ``start``
     - text
     - No
     - When the event starts, as ISO 8601 with a zone offset, for example 2026-10-01T10:00:00+05:30; for an all-day event use startDate instead.
   * - ``end``
     - text
     - No
     - When the event ends, in the same format as start; for an all-day event use endDate instead. Example: 2026-10-01T10:30:00+05:30.
   * - ``startDate``
     - text
     - No
     - For an all-day event, its first day as YYYY-MM-DD, given instead of start. Example: 2026-10-02.
   * - ``endDate``
     - text
     - No
     - For an all-day event, the day after its last day as YYYY-MM-DD (the end is exclusive), given instead of end. Example: 2026-10-03.
   * - ``attendees``
     - list of JSON object
     - No
     - The guests as [{"email": "asha@company.com"}], adding "optional": true for an optional guest. Example: [{"email": "asha@company.com"}, {"email": "vikram@acme.example.com"}].
   * - ``description``
     - text
     - No
     - The event's notes or agenda. Example: Agenda: Q3 numbers, renewal terms, next steps..
   * - ``location``
     - text
     - No
     - A room, place or address. Example: Conference room 4B, Pune office.
   * - ``conferenceType``
     - text
     - No
     - hangoutsMeet adds a Google Meet link to the event; blank adds none.
   * - ``sendUpdates``
     - text
     - No
     - Which guests Google emails about it: all, externalOnly (only guests outside the organisation) or none; all is used when it is left out. Default: all. One of: all, externalOnly, none.
   * - ``conferenceDataVersion``
     - whole number
     - No
     - Keep 1, which is what lets Google create the Meet link conferenceType asks for; 0 drops it. Default: 1. One of: 0, 1.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Calendar.

Need it on every run?
---------------------

To run **Create an event** every time a flow reaches it, without the agent deciding, use the :doc:`Create an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/event-create>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-quickadd.html">Quick add an event</a></div>
