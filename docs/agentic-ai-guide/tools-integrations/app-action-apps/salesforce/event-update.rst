:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Event</p>

Update an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing event and leaves the others as they are; returns the event's Id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Event**, choose **Update an event**.
#. **Details:** choose your Salesforce connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

Fill in the details
-------------------

Only the connection. There are no other boxes to fill in.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **If a row is rejected**
     - No
     - stop fails the run at the first rejected row. continue writes the rest and marks that row failed in result\_status and result\_error. Choices: ``stop``, ``continue``. Default: ``stop``.
   * - **Use the Bulk API from this many rows**
     - No
     - Below this many rows each row is one REST call; from this many the whole set goes as one Bulk API job. 0 never uses the Bulk API. Default: ``200``.

Fields to set
-------------

Each row that arrives is written to Salesforce. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Event Id**
     - ``Id``
     - ``00UXX000001XyZa``
   * - **Subject**
     - ``Subject``
     - ``Quarterly business review``
   * - **Starts**
     - ``StartDateTime``
     - ``2026-10-06T10:00:00Z``
   * - **Ends**
     - ``EndDateTime``
     - ``2026-10-06T11:00:00Z``
   * - **Location**
     - ``Location``
     - ``Acme Energy, Pune office``
   * - **Description**
     - ``Description``
     - ``Agenda: Q3 usage and renewal options.``

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Salesforce gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Update an event** only when a request needs it, add the :doc:`Update an event tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/event-update>` to an Agent Node.

Other Event actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-delete.html">Delete an event</a></div>
