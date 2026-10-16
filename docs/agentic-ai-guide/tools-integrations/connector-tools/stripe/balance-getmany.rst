:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Balance</p>

List balance transactions
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Balance</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists balance transactions, the entries behind every change to the balance (charges, refunds, fees, payouts and adjustments), newest first, from one Stripe page of up to 100. Returns id, type, amount, fee, net, currency, status, available\_on and source for each. Use it for reconciliation or to break a payout down; for current totals use Balance get.

Prerequisites
-------------

* **Connection:** Stripe connection. See :doc:`the Stripe prerequisites <../stripe>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``type``
     - text
     - No
     - Only transactions of this type, such as charge, refund, payout, stripe\_fee or adjustment.
   * - ``payout``
     - text
     - No
     - Only the transactions settled in this payout id (po\_...). Example: po\_1QzT2bLkdIwHu7ixPq8Rst9U.
   * - ``currency``
     - text
     - No
     - Only transactions in this currency, as a lowercase three-letter ISO code. Example: usd.
   * - ``createdAfter``
     - whole number
     - No
     - Only transactions created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only transactions created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``pageSize``
     - whole number
     - No
     - How many transactions Stripe returns in its single page, 1 to 100; Stripe's own default is 10, so keep it at or above limit. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many transactions to return at most, up to 100, since one call reads a single Stripe page. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **list** in the **Balance** row. The model sees it as ``stripe_balance_getmany``.

Other Balance tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="balance-get.html">Get the account balance</a></div>
