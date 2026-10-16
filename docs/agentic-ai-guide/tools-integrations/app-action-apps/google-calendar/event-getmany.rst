:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

List events
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the events on a calendar, with repeating events expanded into single occurrences and sorted by start time by default.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-calendar>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Calendar**.
#. **Action:** under **Event**, choose **List events**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Google Calendar** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Calendar**
     - No
     - The calendar id. Blank means the primary calendar.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``summary, start.dateTime, location``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Extra query parameters (JSON)**
     - No
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"timeMin": "2026-10-01T00:00:00Z"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Google Calendar** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Google Calendar with this action and start the flow when something new turns up. Pick **Google Calendar** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Event created**
     - Reports each event newly created on the calendar; a repeating series is reported once, with its recurrence rule. Calendar is blank for the primary calendar.
   * - **Event created or updated**
     - Reports each event created or changed since the last check; a repeating series is reported once, and cancelled events are left out. Calendar is blank for the primary calendar.
   * - **Event cancelled**
     - Reports each event deleted or cancelled, including one cancelled occurrence of a repeating event; a deleted event can carry little more than its id. Calendar is blank for the primary calendar.
   * - **Event created matching a search**
     - Filter is words to find in the title, description, location or guests, for example interview. Reports each new event that matches them. Calendar is blank for the primary calendar.
   * - **Event starting within the hour**
     - Reports each event once, about an hour before it starts, or on the first check after it is booked when it starts sooner; each occurrence of a repeating event counts. Events already that close at the first check are recorded, not reported. Calendar is blank for the primary calendar.
   * - **Invitation received**
     - Reports each event organised by someone else that reaches the calendar while a guest has yet to answer it, once per change. Calendar is blank for the primary calendar.
   * - **Out of office added**
     - Reports each out-of-office block newly added, with its start, end and decline message; Google Workspace accounts only. Calendar is blank for the primary calendar.

Let an agent decide instead
---------------------------

To let an agent call **List events** only when a request needs it, add the :doc:`List events tool </agentic-ai-guide/tools-integrations/connector-tools/google-calendar/event-getmany>` to an Agent Node.

Other Event actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-quickadd.html">Quick add an event</a></div>
