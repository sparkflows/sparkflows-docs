:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Invoice</p>

List invoices
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Invoice</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists invoices, newest first, from one Stripe page of up to 100. Returns id, number, customer, status, amount\_due, amount\_paid, currency, due\_date and created for each. Use it to find the open or paid invoices of a customer, a subscription or a period; for one known invoice use Invoice get.

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
     - Only invoices of this customer id (cus\_...); Customer getMany returns it. Example: cus\_QzT2bLkdIwHu7i.
   * - ``status``
     - text
     - No
     - Only invoices in this status: open is issued and awaiting payment, uncollectible is written off. One of: draft, open, paid, uncollectible, void.
   * - ``subscription``
     - text
     - No
     - Only invoices of this subscription id (sub\_...); Subscription getMany returns it. Example: sub\_1QzT2bLkdIwHu7ixAbCdEfGh.
   * - ``collectionMethod``
     - text
     - No
     - Only invoices paid automatically from a saved payment method, or only those emailed for the customer to pay. One of: charge\_automatically, send\_invoice.
   * - ``createdAfter``
     - whole number
     - No
     - Only invoices created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only invoices created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``pageSize``
     - whole number
     - No
     - How many invoices Stripe returns in its single page, 1 to 100; Stripe's own default is 10, so keep it at or above limit. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many invoices to return at most, up to 100, since one call reads a single Stripe page. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **list** in the **Invoice** row. The model sees it as ``stripe_invoice_getmany``.

Other Invoice tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="invoice-get.html">Get an invoice</a></div>
