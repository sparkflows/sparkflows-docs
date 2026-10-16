:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Get an event
============

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

   Returns one event by its id with its times, location, organizer, attendees, online meeting link and status.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Outlook Calendar**.
#. **Action:** under **Event**, choose **Get an event**.
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
   * - **Event or calendar id**
     - No
     - The id of the event or calendar to act on.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``subject, start, end, location``.
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
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Outlook Calendar** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Outlook Calendar with this action and start the flow when something new turns up. Pick **Outlook Calendar** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Meeting rescheduled or changed**
     - Mailbox is the calendar to watch, and Event id the meeting's id from an Event list. Reports the meeting each time its title, time, location, attendees or cancellation change.

Let an agent decide instead
---------------------------

To let an agent call **Get an event** only when a request needs it, add the :doc:`Get an event tool </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar/event-get>` to an Agent Node.

Other Event actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
