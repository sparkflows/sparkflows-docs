:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

List events
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_calendar_event_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the events on a calendar, with repeating events expanded into single occurrences and sorted by start time by default. Bound the window with timeMin and timeMax, or it runs from the calendar's earliest event; searchText matches words in the title, description, location and guests.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Event** row, then click **Add to agent**.

The agent now sees ``google_calendar_event_getmany`` and calls it when a request needs it.

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
   * - ``timeMin``
     - text
     - No
     - Only events that end after this moment, as ISO 8601 with a zone offset, for example 2026-10-01T00:00:00+05:30.
   * - ``timeMax``
     - text
     - No
     - Only events that start before this moment, in the same format as timeMin. Example: 2026-10-08T00:00:00+05:30.
   * - ``searchText``
     - text
     - No
     - Words to find in the title, description, location, organiser or guests of the events. Example: budget review.
   * - ``singleEvents``
     - true or false
     - No
     - true lists every occurrence of a repeating event on its own; false returns each series once. Default: True.
   * - ``orderBy``
     - text
     - No
     - startTime sorts by start and needs singleEvents true; updated sorts by the last change. Default: startTime. One of: startTime, updated.
   * - ``updatedMin``
     - text
     - No
     - Only events changed after this moment, deleted ones included, as ISO 8601 with a zone offset. Example: 2026-09-29T00:00:00Z.
   * - ``limit``
     - whole number
     - No
     - How many events at most. Example: 50. Default: 50.
   * - ``fields``
     - list of text
     - No
     - Event fields to return, for example ["id", "summary", "start", "end", "attendees"]; blank returns every field.

Need it on every run?
---------------------

To run **List events** every time a flow reaches it, without the agent deciding, use the :doc:`List events App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/event-getmany>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-quickadd.html">Quick add an event</a></div>
