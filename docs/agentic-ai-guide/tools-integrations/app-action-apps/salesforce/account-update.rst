:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../salesforce.html">Salesforce</a> › Account</p>

Update an account
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Account</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing account and leaves the others as they are; returns the account's Id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Salesforce**.
#. **Action:** under **Account**, choose **Update an account**.
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
   * - **Account Id**
     - ``Id``
     - ``001XX000003DHPh``
   * - **Account name**
     - ``Name``
     - ``Acme Energy Ltd``
   * - **Type**
     - ``Type``
     - ``Customer - Direct``
   * - **Industry**
     - ``Industry``
     - ``Energy``
   * - **Phone**
     - ``Phone``
     - ``+44 20 7946 0958``
   * - **Website**
     - ``Website``
     - ``https://www.acme-energy.example.com``
   * - **Billing city**
     - ``BillingCity``
     - ``Pune``
   * - **Annual revenue**
     - ``AnnualRevenue``
     - ``25000000``
   * - **Employees**
     - ``NumberOfEmployees``
     - ``1200``
   * - **Owner Id**
     - ``OwnerId``
     - ``005XX000001Sv6e``
   * - **Description**
     - ``Description``
     - ``Key account for the western region; renewal due in March.``

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

To let an agent call **Update an account** only when a request needs it, add the :doc:`Update an account tool </agentic-ai-guide/tools-integrations/connector-tools/salesforce/account-update>` to an Agent Node.

Other Account actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="account-get.html">Get an account</a><a href="account-getmany.html">List accounts</a><a href="account-create.html">Create an account</a><a href="account-upsert.html">Create or update an account by external id</a><a href="account-delete.html">Delete an account</a><a href="account-search.html">Search accounts</a><a href="account-describe.html">Describe account fields</a><a href="account-count.html">Count accounts</a><a href="account-addnote.html">Add a note to an account</a></div>
