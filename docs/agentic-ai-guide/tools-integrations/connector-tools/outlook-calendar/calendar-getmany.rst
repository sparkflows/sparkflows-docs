:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Calendar</p>

List calendars
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

   Lists the calendars of a mailbox with their ids, names, colours, owners and which one is the default. The event operations always work on the default calendar.

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
     - The address whose calendars to list. Example: asha.rao@contoso.com.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph calendar properties to return, such as id, name, isDefaultCalendar and canEdit; blank returns them all. Example: ["id", "name", "isDefaultCalendar"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many calendars at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **list** in the **Calendar** row. The model sees it as ``outlook_calendar_calendar_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **List calendars**, and fill in the inputs above. It runs every time the flow reaches it.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-get.html">Get a calendar</a></div>
