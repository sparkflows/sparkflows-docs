:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Subscription</p>

List subscriptions
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Subscription</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists subscriptions, newest first, from one Stripe page of up to 100; canceled subscriptions are left out unless status asks for them. Returns id, customer, status, items with their prices, trial dates, cancel\_at\_period\_end and created for each. Use it to find a customer's active, trialing or past-due subscriptions; for one known subscription use Subscription get.

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
   * - ``customer``
     - text
     - No
     - Only subscriptions of this customer id (cus\_...); Customer getMany returns it. Example: cus\_QzT2bLkdIwHu7i.
   * - ``price``
     - text
     - No
     - Only subscriptions that include this price id (price\_...). Example: price\_1QzT2bLkdIwHu7ixMonthly.
   * - ``status``
     - text
     - No
     - Only subscriptions in this status; all includes canceled ones, and blank lists every status except canceled. One of: active, trialing, past\_due, unpaid, incomplete, incomplete\_expired, paused, canceled, ended, all.
   * - ``createdAfter``
     - whole number
     - No
     - Only subscriptions created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only subscriptions created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``pageSize``
     - whole number
     - No
     - How many subscriptions Stripe returns in its single page, 1 to 100; Stripe's own default is 10, so keep it at or above limit. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many subscriptions to return at most, up to 100, since one call reads a single Stripe page. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **list** in the **Subscription** row. The model sees it as ``stripe_subscription_getmany``.

Other Subscription tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="subscription-get.html">Get a subscription</a><a href="subscription-cancel.html">Cancel a subscription</a></div>
