:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Event</p>

Update an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_event_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing event and leaves the others as they are; returns the event's Id. The event is named by its Salesforce Id, which List events returns.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **update** in the **Event** row, then click **Add to agent**.

The agent now sees ``salesforce_event_update`` and calls it when a request needs it.

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
   * - ``eventId``
     - text
     - Yes
     - The Salesforce Id of the event to change, starting 00U, for example 00UXX000001XyZa; List events returns it.
   * - ``subject``
     - text
     - No
     - The event's title. Example: Quarterly business review.
   * - ``startDateTime``
     - text
     - No
     - When the event starts, as ISO 8601 with a zone, for example 2026-10-06T10:00:00Z.
   * - ``endDateTime``
     - text
     - No
     - When the event ends, in the same format as the start. Example: 2026-10-06T11:00:00Z.
   * - ``location``
     - text
     - No
     - Where the event takes place. Example: Acme Energy, Pune office.
   * - ``description``
     - text
     - No
     - Notes or an agenda for the event. Example: Agenda: Q3 usage and renewal options..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Update an event** every time a flow reaches it, without the agent deciding, use the :doc:`Update an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/event-update>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-delete.html">Delete an event</a></div>
