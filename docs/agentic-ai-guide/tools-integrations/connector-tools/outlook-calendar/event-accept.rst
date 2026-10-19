:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Accept a meeting invitation
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_event_accept</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Accepts a meeting invitation in the mailbox's calendar, optionally with a note to the organizer. Use Event decline to turn it down.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.
* The account behind the connection must be allowed to change this data in Outlook Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **accept** in the **Event** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_event_accept`` and calls it when a request needs it.

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
     - The address of the invited mailbox. Example: asha.rao@contoso.com.
   * - ``eventId``
     - text
     - Yes
     - The id of the invitation's event, from the id column of Event getMany. Example: AAMkAGI2TGuLAAA=.
   * - ``comment``
     - text
     - No
     - A note sent to the organizer with the response. Example: See you there.
   * - ``sendResponse``
     - true or false
     - No
     - true (the default) sends the response to the organizer; false accepts silently.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Outlook Calendar.

Need it on every run?
---------------------

To run **Accept a meeting invitation** every time a flow reaches it, without the agent deciding, use the :doc:`Accept a meeting invitation App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/event-accept>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
