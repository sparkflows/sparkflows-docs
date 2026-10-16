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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing event and leaves the others as they are; returns the event's Id. The event is named by its Salesforce Id, which List events returns.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.
* The connection's account must be allowed to change this data in Salesforce.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``eventId``
     - Event Id
     - text
     - Yes
     - The Salesforce Id of the event to change, starting 00U, for example 00UXX000001XyZa; List events returns it.
   * - ``subject``
     - Subject
     - text
     - No
     - The event's title. Example: Quarterly business review.
   * - ``startDateTime``
     - Starts
     - text
     - No
     - When the event starts, as ISO 8601 with a zone, for example 2026-10-06T10:00:00Z.
   * - ``endDateTime``
     - Ends
     - text
     - No
     - When the event ends, in the same format as the start. Example: 2026-10-06T11:00:00Z.
   * - ``location``
     - Location
     - text
     - No
     - Where the event takes place. Example: Acme Energy, Pune office.
   * - ``description``
     - Description
     - text
     - No
     - Notes or an agenda for the event. Example: Agenda: Q3 usage and renewal options..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **update** in the **Event** row. The model sees it as ``salesforce_event_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Update an event**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-delete.html">Delete an event</a></div>
