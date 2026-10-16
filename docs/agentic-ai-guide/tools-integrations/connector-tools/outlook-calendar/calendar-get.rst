:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Calendar</p>

Get a calendar
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Calendar</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one calendar by its id with its name, colour, owner and edit and sharing rights. Use Calendar getMany to find the id.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Calendar prerequisites <../outlook-calendar>`.

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
   * - ``mailbox``
     - Mailbox
     - text
     - Yes
     - The address the calendar belongs to. Example: asha.rao@contoso.com.
   * - ``calendarId``
     - Calendar id
     - text
     - Yes
     - The id of the calendar, from the id column of Calendar getMany. Example: AAMkAGI2TGuLAAAuAAAAAAAiQ8W967B7TKBjgx9rVEURAQAiIsqMbYjsT5e-T7KzowPTAAAAAAEGAAA=.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph calendar properties to return, such as name, owner and canEdit; blank returns them all.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **get** in the **Calendar** row. The model sees it as ``outlook_calendar_calendar_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **Get a calendar**, and fill in the inputs above. It runs every time the flow reaches it.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-getmany.html">List calendars</a></div>
