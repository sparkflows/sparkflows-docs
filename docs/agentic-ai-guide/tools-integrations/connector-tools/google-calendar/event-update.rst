:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

Update an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_calendar_event_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes only the given fields of an existing event and returns the updated event. A new attendees list replaces the whole guest list, and guests are emailed about the change only when sendUpdates asks for it.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.
* The account behind the connection must be allowed to change this data in Google Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **update** in the **Event** row, then click **Add to agent**.

The agent now sees ``google_calendar_event_update`` and calls it when a request needs it.

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
   * - ``eventId``
     - text
     - Yes
     - The event's id, from List events or Create an event. Example: 5qk2m8r0ht7s3l1c9vfp2d4e6a.
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
     - The full guest list as [{"email": "asha@company.com"}]; it replaces the current list, so include everyone who should stay invited. Example: [{"email": "asha@company.com"}, {"email": "vikram@acme.example.com"}].
   * - ``description``
     - text
     - No
     - The event's notes or agenda. Example: Agenda: Q3 numbers, renewal terms, next steps..
   * - ``location``
     - text
     - No
     - A room, place or address. Example: Conference room 4B, Pune office.
   * - ``sendUpdates``
     - text
     - No
     - Which guests Google emails about it: all, externalOnly (only guests outside the organisation) or none; blank sends no email. One of: all, externalOnly, none.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Calendar.

Need it on every run?
---------------------

To run **Update an event** every time a flow reaches it, without the agent deciding, use the :doc:`Update an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/event-update>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-delete.html">Delete an event</a><a href="event-quickadd.html">Quick add an event</a></div>
