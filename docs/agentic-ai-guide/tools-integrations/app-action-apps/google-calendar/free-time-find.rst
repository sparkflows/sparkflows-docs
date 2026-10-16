:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-calendar.html">Google Calendar</a> › Free Time</p>

Find busy times
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Free Time</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the busy intervals of one or more calendars between timeMin and timeMax, so the free slots are the gaps between them.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-calendar>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Calendar**.
#. **Action:** under **Free Time**, choose **Find busy times**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Google Calendar** so later steps can use the columns, then **Save action**.

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
   * - **Calendar**
     - No
     - The calendar id. Blank means the primary calendar.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``summary, start.dateTime, location``.

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

The records come out as rows, one per record. Click **Load the fields from Google Calendar** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **Find busy times** only when a request needs it, add the :doc:`Find busy times tool </agentic-ai-guide/tools-integrations/connector-tools/google-calendar/free-time-find>` to an Agent Node.
