:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

List events
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists events in the mailbox's default calendar with subject, start and end, location, organizer, attendees, online meeting link and status.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Outlook Calendar**.
#. **Action:** under **Event**, choose **List events**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Outlook Calendar** so later steps can use the columns, then **Save action**.

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
   * - **Mailbox**
     - No
     - The address whose calendar this is, for example someone@company.com. For example ``someone@company.com``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``subject, start, end, location``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.
   * - **Show times in**
     - No
     - The time zone to return start and end in, as a Windows or IANA name; blank returns them in UTC.

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
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"start": "2026-10-01T00:00:00", "end": "2026-10-08T00:00:00"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Outlook Calendar** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Outlook Calendar with this action and start the flow when something new turns up. Pick **Outlook Calendar** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Event created**
     - Mailbox is the calendar to watch. Reports each event added to the calendar, created there or accepted from an invitation.
   * - **Event created or changed**
     - Mailbox is the calendar to watch. Reports each event added or changed since the last check, including a guest's reply.
   * - **Event starting within the hour**
     - Mailbox is the calendar to watch. Reports each meeting once, about an hour before it starts, or on the first check after it is booked when it starts sooner. Meetings already that close at the first check are recorded, not reported.
   * - **Event cancelled**
     - Mailbox is the calendar to watch. Reports each meeting its organizer cancels; a meeting the mailbox itself cancels leaves the calendar and is not seen.
   * - **Event created with a title containing**
     - Mailbox is the calendar to watch, and Filter the words to find in the title, for example interview. Reports each new event whose title contains them, regardless of case.
   * - **Event created with an attendee**
     - Mailbox is the calendar to watch, and Filter an attendee's email address or domain, for example contoso.com. Reports each new event that invites a matching attendee.
   * - **Event created by an organizer**
     - Mailbox is the calendar to watch, and Filter the organizer's email address. Reports each new event in the calendar that this person organizes.
   * - **Event created at a location**
     - Mailbox is the calendar to watch, and Filter the words to find in the location, for example Boardroom. Reports each new event booked at a matching location.
   * - **Online meeting scheduled**
     - Mailbox is the calendar to watch. Reports each new event that carries an online meeting, such as a Teams meeting.
   * - **Out-of-office time booked**
     - Mailbox is the calendar to watch. Reports each new event shown as Out of office, such as leave or travel.
   * - **Recurring meeting created**
     - Mailbox is the calendar to watch. Reports each new repeating meeting once, as its series.

Let an agent decide instead
---------------------------

To let an agent call **List events** only when a request needs it, add the :doc:`List events tool </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar/event-getmany>` to an Agent Node.

Other Event actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
