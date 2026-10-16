:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Create an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an event in the mailbox's default calendar, sends invitations to any attendees, and returns the event with its id.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar>`.
* The account behind the connection must be allowed to change this data in Outlook Calendar.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Outlook Calendar**.
#. **Action:** under **Event**, choose **Create an event**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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
     - The address whose calendar this is, for example someone@company.com.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **If a row is rejected**
     - No
     - What happens when a row cannot be written.

       * ``stop`` (default): The run stops at the first row that fails.
       * ``continue``: The other rows are still written. The failed row is marked ``failed`` in ``result_status``, with the reason in ``result_error``.

Fields to set
-------------

Each row that arrives is written to Outlook Calendar. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Starts**
     - ``start``
     - ``2026-10-05T10:00:00``
   * - **Ends**
     - ``end``
     - ``2026-10-05T10:30:00``
   * - **Title**
     - ``subject``
     - ``Q3 close review``
   * - **Time zone**
     - ``timeZone``
     - ``India Standard Time``
   * - **Attendees**
     - ``attendees``
     - ``["ravi.menon@contoso.com", "finance@contoso.com"]``
   * - **Location**
     - ``location``
     - ``Board room, 4th floor``
   * - **Description**
     - ``body``
     - 
   * - **All day**
     - ``allDay``
     - 
   * - **Online meeting**
     - ``isOnlineMeeting``
     - 

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Outlook Calendar gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Create an event** only when a request needs it, add the :doc:`Create an event tool </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar/event-create>` to an Agent Node.

Other Event actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
