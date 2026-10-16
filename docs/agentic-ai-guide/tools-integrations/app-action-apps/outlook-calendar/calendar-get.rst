:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Calendar</p>

Get a calendar
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Calendar</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one calendar by its id with its name, colour, owner and edit and sharing rights.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Outlook Calendar**.
#. **Action:** under **Calendar**, choose **Get a calendar**.
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

Let an agent decide instead
---------------------------

To let an agent call **Get a calendar** only when a request needs it, add the :doc:`Get a calendar tool </agentic-ai-guide/tools-integrations/connector-tools/outlook-calendar/calendar-get>` to an Agent Node.

Other Calendar actions
----------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-getmany.html">List calendars</a></div>
