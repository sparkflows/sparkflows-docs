:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Create an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_event_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an event in the mailbox's default calendar, sends invitations to any attendees, and returns the event with its id. Use it to book a meeting or block time; to change an existing event use Event update.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.
* The account behind the connection must be allowed to change this data in Outlook Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **create** in the **Event** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_event_create`` and calls it when a request needs it.

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
     - The address whose calendar gets the event; it is the organizer. Example: asha.rao@contoso.com.
   * - ``start``
     - text
     - Yes
     - When it starts, as a local date and time without an offset, read in timeZone. Example: 2026-10-05T10:00:00.
   * - ``end``
     - text
     - Yes
     - When it ends, in the same form as start. Example: 2026-10-05T10:30:00.
   * - ``subject``
     - text
     - No
     - The event's title. Example: Q3 close review.
   * - ``timeZone``
     - text
     - No
     - The time zone start and end are in, as a Windows or IANA name such as India Standard Time or UTC; blank means UTC.
   * - ``attendees``
     - list of text
     - No
     - Addresses to invite as required attendees; Outlook sends each an invitation. Example: ["ravi.menon@contoso.com", "finance@contoso.com"].
   * - ``location``
     - text
     - No
     - Where it takes place, as free text. Example: Board room, 4th floor.
   * - ``body``
     - text
     - No
     - The event's description, as plain text.
   * - ``allDay``
     - true or false
     - No
     - true makes it an all-day event, in which case start and end must be midnights and end the day after the last day.
   * - ``isOnlineMeeting``
     - true or false
     - No
     - true adds a Teams meeting link to the event.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Outlook Calendar.

Need it on every run?
---------------------

To run **Create an event** every time a flow reaches it, without the agent deciding, use the :doc:`Create an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/event-create>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
