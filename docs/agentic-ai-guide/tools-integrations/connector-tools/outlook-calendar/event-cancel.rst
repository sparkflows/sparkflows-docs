:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Cancel a meeting
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_event_cancel</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Cancels a meeting the mailbox organizes and sends every attendee a cancellation carrying the comment. It works only for the organizer; an attendee turns a meeting down with Event decline.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.
* The account behind the connection must be allowed to change this data in Outlook Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **cancel** in the **Event** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_event_cancel`` and calls it when a request needs it.

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
     - The organizer's address. Example: asha.rao@contoso.com.
   * - ``eventId``
     - text
     - Yes
     - The id of the meeting to cancel, from the id column of Event getMany. Example: AAMkAGI2TGuLAAA=.
   * - ``comment``
     - text
     - No
     - The message sent with the cancellation. Example: Cancelled: the review moves to next week.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Outlook Calendar.

Need it on every run?
---------------------

To run **Cancel a meeting** every time a flow reaches it, without the agent deciding, use the :doc:`Cancel a meeting App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/event-cancel>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a></div>
