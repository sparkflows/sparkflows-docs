:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Charge</p>

List charges
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Charge</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists charges, newest first, from one Stripe page of up to 100, including failed and refunded ones. Returns id, amount, currency, status, paid, refunded, customer and created for each. Use it to review a customer's payments or the payments of a period; for one known charge use Charge get.

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
     - Only charges of this customer id (cus\_...); Customer getMany returns it. Example: cus\_QzT2bLkdIwHu7i.
   * - ``paymentIntent``
     - text
     - No
     - Only charges made for this PaymentIntent id (pi\_...). Example: pi\_3QzT2bLkdIwHu7ix0xYz1234.
   * - ``createdAfter``
     - whole number
     - No
     - Only charges created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only charges created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``pageSize``
     - whole number
     - No
     - How many charges Stripe returns in its single page, 1 to 100; Stripe's own default is 10, so keep it at or above limit. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many charges to return at most, up to 100, since one call reads a single Stripe page. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **list** in the **Charge** row. The model sees it as ``stripe_charge_getmany``.

Other Charge tools
------------------

.. raw:: html

   <div class="tool-related"><a href="charge-get.html">Get a charge</a></div>
