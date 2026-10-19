:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Campaign</p>

Create a campaign
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Campaign</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a campaign (a marketing initiative) from the given fields and returns its new Id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Campaign**, choose **Create a campaign**.
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
     - What happens when a row cannot be written.

       * ``stop`` (default): The run stops at the first row that fails.
       * ``continue``: The other rows are still written. The failed row is marked ``failed`` in ``result_status``, with the reason in ``result_error``.
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
   * - **Campaign name**
     - ``Name``
     - ``Energy Transition Webinar 2026``
   * - **Type**
     - ``Type``
     - ``Webinar``
   * - **Status**
     - ``Status``
     - ``Planned``
   * - **Start date**
     - ``StartDate``
     - ``2026-11-04``
   * - **End date**
     - ``EndDate``
     - ``2026-11-30``
   * - **Active**
     - ``IsActive``
     - ``true``
   * - **Budgeted cost**
     - ``BudgetedCost``
     - ``15000``
   * - **Expected revenue**
     - ``ExpectedRevenue``
     - ``120000``
   * - **Description**
     - ``Description``
     - ``Joint webinar with the grid-storage partner.``

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

To let an agent call **Create a campaign** only when a request needs it, add the :doc:`Create a campaign tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/campaign-create>` to an Agent Node.

Other Campaign actions
----------------------

.. raw:: html

   <div class="tool-related"><a href="campaign-get.html">Get a campaign</a><a href="campaign-getmany.html">List campaigns</a><a href="campaign-update.html">Update a campaign</a><a href="campaign-delete.html">Delete a campaign</a></div>
