:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Event</p>

Create an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_event_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an event (a meeting on the Salesforce calendar) from the given fields and returns its new Id. It needs startDateTime and endDateTime; link people and records with whoId and whatId, as for a task.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Event** row, then click **Add to agent**.

The agent now sees ``salesforce_event_create`` and calls it when a request needs it.

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
   * - ``startDateTime``
     - text
     - Yes
     - When the event starts, as ISO 8601 with a zone, for example 2026-10-06T10:00:00Z.
   * - ``endDateTime``
     - text
     - Yes
     - When the event ends, in the same format as the start. Example: 2026-10-06T11:00:00Z.
   * - ``subject``
     - text
     - No
     - The event's title. Example: Quarterly business review.
   * - ``location``
     - text
     - No
     - Where the event takes place. Example: Acme Energy, Pune office.
   * - ``whoId``
     - text
     - No
     - The contact (an Id starting 003) or lead (00Q) the event is with. Example: 003XX000004TmiQ.
   * - ``whatId``
     - text
     - No
     - The account, opportunity or other record the event relates to. Example: 001XX000003DHPh.
   * - ``ownerId``
     - text
     - No
     - The Id of the user whose calendar the event is on, starting 005. Example: 005XX000001Sv6e.
   * - ``description``
     - text
     - No
     - Notes or an agenda for the event. Example: Agenda: Q3 usage and renewal options..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create an event** every time a flow reaches it, without the agent deciding, use the :doc:`Create an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/event-create>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a></div>
