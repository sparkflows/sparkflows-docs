:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Update an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_event_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes an existing event's title, times, location, description or attendees and returns the updated event. Only the fields given change; attendees, when given, replace the whole list.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.
* The account behind the connection must be allowed to change this data in Outlook Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **update** in the **Event** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_event_update`` and calls it when a request needs it.

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
     - The address whose calendar holds the event. Example: asha.rao@contoso.com.
   * - ``eventId``
     - text
     - Yes
     - The id of the event to change, from the id column of Event getMany. Example: AAMkAGI2TGuLAAA=.
   * - ``subject``
     - text
     - No
     - The new title.
   * - ``start``
     - text
     - No
     - The new start, as a local date and time without an offset, read in timeZone. Example: 2026-10-05T11:00:00.
   * - ``end``
     - text
     - No
     - The new end, in the same form as start. Example: 2026-10-05T11:30:00.
   * - ``timeZone``
     - text
     - No
     - The time zone of start and end; give it whenever start or end changes, since blank means UTC. Example: India Standard Time.
   * - ``location``
     - text
     - No
     - The new location, as free text.
   * - ``body``
     - text
     - No
     - The new description, as plain text.
   * - ``attendees``
     - list of text
     - No
     - The full list of attendee addresses; it replaces the current attendees.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Outlook Calendar.

Need it on every run?
---------------------

To run **Update an event** every time a flow reaches it, without the agent deciding, use the :doc:`Update an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/event-update>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
